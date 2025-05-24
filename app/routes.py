from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import mongo
from .nlp_utils import preprocess_text
from .bert_model import get_bert_prediction
from .interpretability import explain_prediction
from bson import ObjectId

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/dashboard")
@login_required
def dashboard():
    user_texts = list(mongo.db.texts.find({"user_id": current_user.id}))
    return render_template("dashboard.html", user_texts=user_texts)

@main_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST":
        text = request.form["text"]
        processed = preprocess_text(text)
        prediction = get_bert_prediction(processed)
        explanation = explain_prediction(processed, prediction)
        text_id = mongo.db.texts.insert_one({
            "user_id": current_user.id,
            "raw_text": text,
            "tokens": processed["tokens"],
            "lemmas": processed["lemmas"],
            "entities": processed["entities"],
            "prediction": prediction,
            "explanation": explanation
        }).inserted_id
        flash("Text analyzed and prediction saved!")
        return redirect(url_for("main.result", text_id=text_id))
    return render_template("upload.html")

@main_bp.route("/result/<text_id>")
@login_required
def result(text_id):
    text_doc = mongo.db.texts.find_one({"_id": ObjectId(text_id), "user_id": current_user.id})
    if not text_doc:
        flash("Result not found.")
        return redirect(url_for("main.dashboard"))
    return render_template("result.html", text_doc=text_doc)