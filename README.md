# 🧠 Depression Severity Detection using BERT

This project leverages a fine-tuned BERT model to classify the severity of depression based on user-written text, using the **PHQ-9 questionnaire** and diary-style inputs. It categorizes depression levels into:

- Minimal
- Mild
- Moderate
- Moderately Severe
- Severe

The model is integrated into a simple desktop application using `tkinter` for real-time inference.

---

## 🚀 Features

- ✅ BERT-based multi-class classifier
- ✅ Tkinter GUI for user input and predictions
- ✅ Evaluated using confusion matrix and classification report
- ✅ Clean architecture with modular code and reusable components

---

## 🔍 Dataset Overview

The model is trained using:
- PHQ-9 based labeled text entries
- Diary logs or self-expressed symptoms
- Labels mapped to five severity levels (`0` to `4`)

---

## 📈 Model Evaluation

### 📊 Confusion Matrix

![image](https://github.com/user-attachments/assets/3b995dd1-8cd5-4709-a4ac-81c3f4eb6964)


### 🧾 Classification Report

| **Severity Level**    | **Precision** | **Recall** | **F1-Score** | **Support** |
|-----------------------|---------------|------------|--------------|-------------|
| Minimal               | 1.00          | 1.00       | 1.00         | 8           |
| Mild                  | 1.00          | 1.00       | 1.00         | 9           |
| Moderate              | 1.00          | 0.67       | 0.80         | 9           |
| Moderately Severe     | 1.00          | 1.00       | 1.00         | 10          |
| Severe                | 0.82          | 1.00       | 0.90         | 14          |

**Overall Metrics**:
- **Accuracy:** `94%`
- **Macro Avg F1-score:** `94%`
- **Weighted Avg F1-score:** `94%`

---

## 🛠️ How to Run the Project

### 🔃 Clone the Repository

```bash
git clone https://github.com/yourusername/depression-detector.git
cd depression-detector
