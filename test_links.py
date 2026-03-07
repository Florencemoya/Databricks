from __future__ import annotations

from datetime import datetime
from pathlib import Path
import os

import pandas as pd
import requests
from tqdm import tqdm


if "__file__" in globals():
    BASE_DIR = Path(__file__).resolve().parent
else:
    BASE_DIR = Path("/Workspace/Users/yaomoya95@gmail.com/Databricks")

INPUT_FILE = BASE_DIR / "url" / "csv_url.csv"
OUTPUT_DIR = BASE_DIR / "url"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def check_link(url: str) -> str:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code in [200, 403]:
            return "✅ Fonctionnel"
        return f"⚠️ Problème ({response.status_code})"
    except requests.RequestException:
        return "❌ Inaccessible"


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Fichier introuvable : {INPUT_FILE}")

    liens = pd.read_csv(INPUT_FILE, sep=",", encoding="utf-8")
    liens = liens.iloc[1:10]  # garde les lignes 1 à 9

    results = []
    with tqdm(total=len(liens), desc="Vérification des liens", unit=" lien") as pbar:
        for _, row in liens.iterrows():
            url = row["url"]
            status = check_link(url)
            tested_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            results.append((url, status, tested_at))
            pbar.update(1)

    df_results = pd.DataFrame(results, columns=["url", "statut", "datetime"])
    output_file = OUTPUT_DIR / f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.csv"
    df_results.to_csv(output_file, index=False, encoding="utf-8")

    print(df_results)
    print(f"Résultats enregistrés dans : {output_file}")


if __name__ == "__main__":
    main()