from __future__ import annotations

import csv
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "url" / "url.json"
OUTPUT_FILE = BASE_DIR / "url" / "csv_url.csv"

# Capture le texte entre \x1b[49m et le prochain \x1b
PATTERN = re.compile(r"\x1b\[49m(.*?)\x1b", re.DOTALL)


def extract_url_from_line(line: str) -> str:
    if not line:
        return ""
    match = PATTERN.search(line)
    return match.group(1).strip() if match else ""


def main() -> None:
    with INPUT_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(["url", "status_code"])

        for item in data.get("processed", []):
            raw_line = item.get("line", "")
            url = extract_url_from_line(raw_line)
            writer.writerow([url, item.get("status_code", "")])

    print(f"CSV généré: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
