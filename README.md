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
```

## 2. 📦 Install Requirements

```bash
pip install torch transformers scikit-learn matplotlib pandas tkinter
````


---

## 3. 📓 Train the Model

Open and run the provided Jupyter Notebook:

```bash
jupyter notebook train_model.ipynb
```

The notebook will:

* Load and preprocess the dataset
* Train a BERT model
* Save the model and tokenizer in the appropriate directories

---

## 4. ▶️ Run the GUI Application

Run the GUI using:

```bash
python main.py
```

The GUI will open, allowing you to enter text and view the predicted depression severity.

# 🧠 Input Example

Type journal entries, survey answers, or general thoughts in the GUI like:

> "I feel hopeless, have trouble sleeping, and lost interest in things I used to enjoy."

And get predicted severity like:

**Prediction:** _Moderately Severe_

---

## 💡 Future Improvements

- Add sentiment and emotion detection alongside severity  
- Export results to CSV or PDF  
- Deploy as a web app (Streamlit/Flask)  
- Mobile app integration  

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [PyTorch](https://pytorch.org/)
- [PHQ-9 Questionnaire](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1495268/)
- [BERT Paper (Devlin et al.)](https://arxiv.org/abs/1810.04805)

---

### ⚙️ Want Help With:

- ✅ GitHub Actions CI or badge integration  
- ✅ Deployment setup (Streamlit, Flask, Hugging Face Spaces)

Let me know — I'm happy to help!


