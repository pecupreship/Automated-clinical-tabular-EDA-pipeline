import os
import uuid
import logging

from flask import (
    Flask,
    render_template,
    request
)

from werkzeug.utils import secure_filename

from eda.analysis import run_eda

from config import (
    UPLOAD_FOLDER,
    MAX_CONTENT_LENGTH,
    ALLOWED_EXTENSIONS
)

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# -------------------------
# HOME PAGE
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# ANALYZE ROUTE
# -------------------------
@app.route("/analyze", methods=["POST"])
def analyze():

    try:

        if "file" not in request.files:
            return render_template("error.html", error="No file uploaded")

        file = request.files["file"]

        if file.filename == "":
            return render_template("error.html", error="No file selected")

        if not allowed_file(file.filename):
            return render_template("error.html", error="Invalid file type")

        filename = secure_filename(
            f"{uuid.uuid4()}_{file.filename}"
        )

        filepath = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        file.save(filepath)

        # RUN EDA
        report = run_eda(filepath)

        return render_template(
            "report.html",
            report=report
        )

    except Exception as e:
        logging.error(str(e))
        return render_template("error.html", error=str(e))


# -------------------------
# RUN APP (ONLY HERE)
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)