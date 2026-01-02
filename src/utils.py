import json
from pathlib import Path

DATA_DIR = Path("src/utils.py").resolve().parent.parent / "data"

def load_json(filename):
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)