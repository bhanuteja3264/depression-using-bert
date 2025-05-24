def explain_prediction(processed, prediction):
    label = prediction["label"].lower()
    depression_keywords = {"sad", "depressed", "hopeless", "unhappy", "worthless", "cry", "alone", "tired"}
    cause_tokens = [t for t in processed["tokens"] if t.lower() in depression_keywords]
    if label in ["sadness", "fear", "anger"]:
        if cause_tokens:
            return f"Key words contributing to the prediction: {', '.join(cause_tokens)}"
    return "The model's prediction was based on the linguistic and emotional content of your text."