import tkinter as tk
from tkinter import messagebox, ttk
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import threading

# === 1. Load model and tokenizer ===
try:
    model_path = 'depression_detection/model/bert_depression_model'
    tokenizer_path = 'depression_detection/model/bert_tokenizer'

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    model = BertForSequenceClassification.from_pretrained(model_path)
    tokenizer = BertTokenizer.from_pretrained(tokenizer_path)
    model.to(device)
    model.eval()
    model_loaded = True
    print("Model and tokenizer loaded successfully.")
except Exception as e:
    model_loaded = False
    print(f"Error loading model/tokenizer: {e}")

# === 2. Class Names ===
class_names = ['No Depression', 'Mild', 'Moderate', 'Severe']

# === 3. Prediction Function ===
def predict_depression(text):
    try:
        encoding = tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=128,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )

        input_ids = encoding['input_ids'].to(device)
        attention_mask = encoding['attention_mask'].to(device)

        with torch.no_grad():
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)

        logits = outputs.logits
        probs = torch.softmax(logits, dim=1)
        confidence, idx = torch.max(probs, dim=1)

        return class_names[idx.item()], confidence.item()
    except Exception as e:
        raise e

# === 4. GUI Prediction Thread Logic ===
def run_prediction_thread(text):
    try:
        result, confidence = predict_depression(text)
        root.after(0, update_result_label, result, confidence)
    except Exception as e:
        root.after(0, show_prediction_error, e)
    finally:
        root.after(0, reset_ui_state)

def on_submit():
    user_input = text_entry.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showwarning("Input Required", "Please enter some text.")
        return

    submit_button.config(state=tk.DISABLED)
    result_label.config(text="")
    progress_bar.start(10)

    thread = threading.Thread(target=run_prediction_thread, args=(user_input,), daemon=True)
    thread.start()

def update_result_label(result, confidence):
    result_label.config(
        text=f"Predicted Severity: {result} (Confidence: {confidence:.2f})"
    )

def show_prediction_error(error):
    messagebox.showerror("Prediction Error", f"An error occurred during prediction:\n{error}")

def reset_ui_state():
    progress_bar.stop()
    submit_button.config(state=tk.NORMAL)

# === 5. Build GUI ===
root = tk.Tk()
root.title("Depression Severity Detector")
root.geometry("750x500")
root.minsize(600, 400)

style = ttk.Style()
style.configure("TLabel", padding=6, font=("Segoe UI", 12))
style.configure("TButton", padding=6, font=("Segoe UI", 12))

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(expand=True, fill=tk.BOTH)

ttk.Label(main_frame, text="Describe your thoughts:", font=("Segoe UI", 14, "bold")).pack(pady=(0, 8))

# === Text Area with Scrollbar ===
text_frame = ttk.Frame(main_frame)
text_frame.pack(fill=tk.BOTH, expand=True)

text_entry = tk.Text(
    text_frame, wrap=tk.WORD, font=("Segoe UI", 11), relief=tk.GROOVE, borderwidth=2
)
scrollbar = ttk.Scrollbar(text_frame, command=text_entry.yview)
text_entry.config(yscrollcommand=scrollbar.set)

text_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# === Predict Button ===
submit_button = ttk.Button(main_frame, text="Predict", command=on_submit)
submit_button.pack(pady=15)

# === Progress Bar ===
progress_bar = ttk.Progressbar(main_frame, mode='indeterminate')
progress_bar.pack(fill=tk.X, padx=20, pady=5)

# === Result Label ===
result_label = ttk.Label(
    main_frame, text="", font=("Segoe UI", 14, "bold"), anchor=tk.CENTER
)
result_label.pack(pady=10)

# === Disable prediction if model failed ===
if not model_loaded:
    submit_button.config(state=tk.DISABLED)
    error_msg = ttk.Label(main_frame, text="Model not loaded. Please check your model path.", foreground="red", font=("Segoe UI", 11))
    error_msg.pack(pady=10)

# === Start GUI ===
root.mainloop()
