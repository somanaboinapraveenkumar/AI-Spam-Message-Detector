import pickle
import tkinter as tk
from tkinter import messagebox

# Load model and vectorizer
model = pickle.load(open("MODEL/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("MODEL/vectorizer.pkl", "rb"))

MODEL_ACCURACY = "97.85%"  # You can change if needed


def check_message():
    message = text_entry.get("1.0", tk.END).strip()
    
    if message == "":
        messagebox.showwarning("Warning", "Please enter a message!")
        return
    
    message_tfidf = vectorizer.transform([message])
    prediction = model.predict(message_tfidf)

    if prediction[0] == 1:
        result = "🚨 SPAM"
        result_label.config(text=result, fg="#ff4d4d")
    else:
        result = "✅ NOT SPAM"
        result_label.config(text=result, fg="#4CAF50")

    # Add to history
    history_box.insert(tk.END, f"{message}  -->  {result}\n\n")
    history_box.see(tk.END)


def clear_fields():
    text_entry.delete("1.0", tk.END)
    result_label.config(text="")



window = tk.Tk()
window.title("AI Spam Detector")
window.geometry("500x550")
window.config(bg="#1e1e2f")  # Dark background



title_label = tk.Label(
    window, 
    text="AI Spam Message Detector",
    font=("Helvetica", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title_label.pack(pady=10)

# Accuracy Display
accuracy_label = tk.Label(
    window,
    text=f"Model Accuracy: {MODEL_ACCURACY}",
    font=("Helvetica", 10),
    bg="#1e1e2f",
    fg="#00ccff"
)
accuracy_label.pack(pady=5)


text_entry = tk.Text(
    window,
    height=4,
    width=50,
    font=("Helvetica", 11),
    bg="#2e2e3f",
    fg="white",
    insertbackground="white"
)
text_entry.pack(pady=10)



button_frame = tk.Frame(window, bg="#1e1e2f")
button_frame.pack(pady=5)

check_button = tk.Button(
    button_frame,
    text="Check Message",
    command=check_message,
    bg="#00ccff",
    fg="black",
    width=15
)
check_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    bg="#ff4d4d",
    fg="white",
    width=10
)
clear_button.grid(row=0, column=1, padx=10)



result_label = tk.Label(
    window,
    text="",
    font=("Helvetica", 14, "bold"),
    bg="#1e1e2f"
)
result_label.pack(pady=10)



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
    height=10,
    width=60,
    font=("Helvetica", 9),
    bg="#2e2e3f",
    fg="white"
)
history_box.pack(pady=5)

window.mainloop()