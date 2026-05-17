import os

BASE_DIR = os.path.abspath(
    os.path.dirname(__file__)
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "data/uploads"
)

MAX_CONTENT_LENGTH = (
    20 * 1024 * 1024
)

ALLOWED_EXTENSIONS = {
    "csv",
    "xlsx",
    "xls"
}