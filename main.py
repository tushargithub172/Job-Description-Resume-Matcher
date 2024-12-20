from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import PyPDF2
import docx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Flask App Initialization
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_text_from_file(filepath):
    """Extract text from PDF, DOCX, or TXT file."""
    _, file_extension = os.path.splitext(filepath)
    text = ""

    if file_extension.lower() == ".pdf":
        with open(filepath, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()
    elif file_extension.lower() == ".docx":
        doc = docx.Document(filepath)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    elif file_extension.lower() == ".txt":
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
    return text

def match_resumes(job_description, resumes_texts):
    """Compute similarity scores between job description and resumes."""
    texts = [job_description] + resumes_texts
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    return cosine_similarities.flatten()

@app.route("/", methods=["GET"])
def index():
    """Render the HTML page."""
    return render_template("index.html")

@app.route("/matcher", methods=["POST"])
def matcher():
    """Handle file uploads and match resumes."""
    job_description = request.form.get("job_description")
    uploaded_files = request.files.getlist("resumes")

    if not job_description or not uploaded_files:
        return jsonify({"error": "Job description and resumes are required."}), 400

    resumes_texts = []
    filenames = []

    # Process each uploaded file
    for file in uploaded_files:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)
        filenames.append(filename)
        resumes_texts.append(extract_text_from_file(filepath))

    # Match resumes with job description
    scores = match_resumes(job_description, resumes_texts)

    # Prepare results
    results = [{"filename": filenames[i], "score": round(float(scores[i]) * 100, 2)} for i in range(len(scores))]
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return render_template("results.html", results=results)

@app.route("/results")
def results():
    """Display results."""
    return jsonify({"message": "Results Page"})

if __name__ == "__main__":  # Corrected the conditional statement
    app.run(debug=True)
