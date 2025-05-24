from transformers import BertTokenizer, BertForSequenceClassification
import torch

MODEL_PATH = "bert_depression_model"

tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)

LABEL_MAP = {
    0: "minimal",
    1: "mild",
    2: "moderate",
    3: "moderately severe",
    4: "severe"
}

def get_bert_prediction(processed):
    text = processed["text"]
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
        label_name = LABEL_MAP.get(predicted_class, str(predicted_class))
        score = float(torch.softmax(logits, dim=1).max().item())
        return {
            "label": label_name,
            "score": score
        }