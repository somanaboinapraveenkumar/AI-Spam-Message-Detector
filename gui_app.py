
import pickle
import csv
import tkinter as tk
from tkinter import messagebox, filedialog


# ==========================================
# LOAD MODEL AND VECTORIZER
# ==========================================

with open("MODEL/spam_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("MODEL/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

MODEL_ACCURACY = "97.85%"


# ==========================================
# GLOBAL VARIABLES
# ==========================================

prediction_history = []

total_count = 0
spam_count = 0
not_spam_count = 0


# ==========================================
# PREDICT MESSAGE
# ==========================================

def predict_message(message):
    message_features = vectorizer.transform([message])

    prediction = model.predict(message_features)[0]

    probabilities = model.predict_proba(message_features)[0]
    class_index = list(model.classes_).index(prediction)
    confidence = probabilities[class_index] * 100

    if prediction == 1:
        result = "SPAM"
    else:
        result = "NOT SPAM"

    return result, confidence


# ==========================================
# UPDATE STATISTICS
# ==========================================

def update_statistics(result):
    global total_count, spam_count, not_spam_count

    total_count += 1

    if result == "SPAM":
        spam_count += 1
    else:
        not_spam_count += 1

    total_label.config(text=f"Total: {total_count}")
    spam_label.config(text=f"SPAM: {spam_count}")
    not_spam_label.config(text=f"NOT SPAM: {not_spam_count}")


# ==========================================
# CHECK SINGLE MESSAGE
# ==========================================

def check_message():
    message = text_entry.get("1.0", tk.END).strip()

    if not message:
        messagebox.showwarning(
            "Warning",
            "Please enter a message!"
        )
        return

    try:
        result, confidence = predict_message(message)

        if result == "SPAM":
            result_label.config(
                text="🚨 SPAM",
                fg="#ff4d4d"
            )
        else:
            result_label.config(
                text="✅ NOT SPAM",
                fg="#4CAF50"
            )

        confidence_label.config(
            text=f"Confidence Score: {confidence:.2f}%",
            fg="#00ccff"
        )

        record = {
            "Message": message,
            "Prediction": result,
            "Confidence": f"{confidence:.2f}%"
        }

        prediction_history.append(record)
        update_statistics(result)

        history_box.insert(
            tk.END,
            f"{message}\n"
            f"--> {result} | Confidence: {confidence:.2f}%\n\n"
        )

        history_box.see(tk.END)

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Could not predict message:\n{e}"
        )


# ==========================================
# CLEAR INPUT FIELDS
# ==========================================

def clear_fields():
    text_entry.delete("1.0", tk.END)
    result_label.config(text="")
    confidence_label.config(text="")


# ==========================================
# SAVE HISTORY TO CSV
# ==========================================

def save_history():
    if not prediction_history:
        messagebox.showwarning(
            "Warning",
            "No prediction history to save!"
        )
        return

    file_path = filedialog.asksaveasfilename(
        title="Save Prediction History",
        defaultextension=".csv",
        initialfile="spam_history.csv",
        filetypes=[("CSV Files", "*.csv")]
    )

    if not file_path:
        return

    try:
        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Message",
                    "Prediction",
                    "Confidence"
                ]
            )
            writer.writeheader()
            writer.writerows(prediction_history)

        messagebox.showinfo(
            "Success",
            "Prediction history saved successfully!"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Could not save file:\n{e}"
        )


# ==========================================
# BULK CSV MESSAGE DETECTION
# ==========================================

def bulk_csv_detection():
    file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )

    if not file_path:
        return

    try:
        with open(
            file_path,
            "r",
            newline="",
            encoding="utf-8-sig"
        ) as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                messagebox.showwarning(
                    "Warning",
                    "The CSV file is empty or has no header row."
                )
                return

            message_column = next(
                (
                    column for column in reader.fieldnames
                    if column.strip().lower()
                    in ["message", "messages", "text", "sms"]
                ),
                None
            )

            if message_column is None:
                messagebox.showwarning(
                    "Missing Column",
                    "The CSV must contain a column named "
                    "'message', 'messages', 'text', or 'sms'."
                )
                return

            rows = list(reader)

        if not rows:
            messagebox.showwarning(
                "Warning",
                "The CSV file contains no messages."
            )
            return

        results = []

        for row in rows:
            message = (row.get(message_column) or "").strip()

            if not message:
                continue

            result, confidence = predict_message(message)

            record = {
                "Message": message,
                "Prediction": result,
                "Confidence": f"{confidence:.2f}%"
            }

            results.append(record)
            prediction_history.append(record)
            update_statistics(result)

        if not results:
            messagebox.showwarning(
                "Warning",
                "No valid messages were found in the CSV."
            )
            return

        history_box.insert(
            tk.END,
            f"--- BULK CSV RESULTS: {len(results)} messages ---\n\n"
        )

        for record in results:
            history_box.insert(
                tk.END,
                f"{record['Message']}\n"
                f"--> {record['Prediction']} | "
                f"Confidence: {record['Confidence']}\n\n"
            )

        history_box.see(tk.END)

        output_path = filedialog.asksaveasfilename(
            title="Save Bulk Prediction Results",
            defaultextension=".csv",
            initialfile="bulk_prediction_results.csv",
            filetypes=[("CSV Files", "*.csv")]
        )

        if output_path:
            with open(
                output_path,
                "w",
                newline="",
                encoding="utf-8-sig"
            ) as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=[
                        "Message",
                        "Prediction",
                        "Confidence"
                    ]
                )
                writer.writeheader()
                writer.writerows(results)

            messagebox.showinfo(
                "Success",
                f"Processed {len(results)} messages.\n"
                "Bulk results saved successfully!"
            )
        else:
            messagebox.showinfo(
                "Completed",
                f"Processed {len(results)} messages.\n"
                "Results are available in Message History."
            )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Could not process CSV file:\n{e}"
        )


# ==========================================
# CLEAR HISTORY AND RESET STATISTICS
# ==========================================

def reset_history():
    global total_count, spam_count, not_spam_count

    confirm = messagebox.askyesno(
        "Confirm Reset",
        "Are you sure you want to clear all history "
        "and reset statistics?"
    )

    if not confirm:
        return

    # Clear prediction history
    prediction_history.clear()

    # Reset counters
    total_count = 0
    spam_count = 0
    not_spam_count = 0

    # Reset dashboard
    total_label.config(text="Total: 0")
    spam_label.config(text="SPAM: 0")
    not_spam_label.config(text="NOT SPAM: 0")

    # Clear history and input
    history_box.delete("1.0", tk.END)
    text_entry.delete("1.0", tk.END)

    # Clear prediction and confidence
    result_label.config(text="")
    confidence_label.config(text="")

    messagebox.showinfo(
        "Reset Complete",
        "History and statistics have been reset successfully!"
    )


# ==========================================
# MAIN WINDOW
# ==========================================

window = tk.Tk()
window.title("AI Spam Message Detector")
window.geometry("700x850")
window.config(bg="#1e1e2f")


# ==========================================
# TITLE
# ==========================================

title_label = tk.Label(
    window,
    text="AI Spam Message Detector",
    font=("Helvetica", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title_label.pack(pady=10)


# ==========================================
# MODEL ACCURACY
# ==========================================

accuracy_label = tk.Label(
    window,
    text=f"Model Accuracy: {MODEL_ACCURACY}",
    font=("Helvetica", 11),
    bg="#1e1e2f",
    fg="#00ccff"
)
accuracy_label.pack(pady=5)


# ==========================================
# STATISTICS DASHBOARD
# ==========================================

stats_frame = tk.Frame(
    window,
    bg="#1e1e2f"
)
stats_frame.pack(pady=10)

total_label = tk.Label(
    stats_frame,
    text="Total: 0",
    font=("Helvetica", 12, "bold"),
    bg="#303044",
    fg="white",
    width=15,
    padx=5,
    pady=10
)
total_label.grid(row=0, column=0, padx=5)

spam_label = tk.Label(
    stats_frame,
    text="SPAM: 0",
    font=("Helvetica", 12, "bold"),
    bg="#303044",
    fg="#ff4d4d",
    width=15,
    padx=5,
    pady=10
)
spam_label.grid(row=0, column=1, padx=5)

not_spam_label = tk.Label(
    stats_frame,
    text="NOT SPAM: 0",
    font=("Helvetica", 12, "bold"),
    bg="#303044",
    fg="#4CAF50",
    width=15,
    padx=5,
    pady=10
)
not_spam_label.grid(row=0, column=2, padx=5)


# ==========================================
# MESSAGE INPUT
# ==========================================

text_entry = tk.Text(
    window,
    height=4,
    width=70,
    font=("Helvetica", 11),
    bg="#2e2e3f",
    fg="white",
    insertbackground="white"
)
text_entry.pack(pady=10)


# ==========================================
# BUTTONS
# ==========================================

button_frame = tk.Frame(
    window,
    bg="#1e1e2f"
)
button_frame.pack(pady=5)

check_button = tk.Button(
    button_frame,
    text="Check Message",
    command=check_message,
    bg="#00ccff",
    fg="black",
    width=15
)
check_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    bg="#ff4d4d",
    fg="white",
    width=10
)
clear_button.grid(row=0, column=1, padx=5)

bulk_button = tk.Button(
    button_frame,
    text="Upload CSV",
    command=bulk_csv_detection,
    bg="#9b59b6",
    fg="white",
    width=15
)
bulk_button.grid(row=0, column=2, padx=5)


# ==========================================
# SAVE HISTORY BUTTON
# ==========================================

save_button = tk.Button(
    window,
    text="Save History to CSV",
    command=save_history,
    bg="#4CAF50",
    fg="white",
    width=22
)
save_button.pack(pady=8)


# ==========================================
# RESET HISTORY BUTTON
# ==========================================

reset_button = tk.Button(
    window,
    text="Clear History & Reset Statistics",
    command=reset_history,
    bg="#ff4d4d",
    fg="white",
    width=30
)
reset_button.pack(pady=8)


# ==========================================
# PREDICTION RESULT
# ==========================================

result_label = tk.Label(
    window,
    text="",
    font=("Helvetica", 14, "bold"),
    bg="#1e1e2f"
)
result_label.pack(pady=10)


# ==========================================
# CONFIDENCE SCORE
# ==========================================

confidence_label = tk.Label(
    window,
    text="",
    font=("Helvetica", 12, "bold"),
    bg="#1e1e2f"
)
confidence_label.pack(pady=5)


# ==========================================
# MESSAGE HISTORY
# ==========================================

history_title = tk.Label(
    window,
    text="Message History",
    font=("Helvetica", 12, "bold"),
    bg="#1e1e2f",
    fg="white"
)
history_title.pack(pady=5)

history_box = tk.Text(
    window,
    height=15,
    width=80,
    font=("Helvetica", 9),
    bg="#2e2e3f",
    fg="white"
)
history_box.pack(pady=5)


# ==========================================
# RUN APPLICATION
# ==========================================

window.mainloop()