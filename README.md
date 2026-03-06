# databricks

Projet prêt pour Databricks avec :

- `requirements.txt` pour les dépendances Python
- `databricks.yml` pour un Databricks Asset Bundle minimal
- `resources/jobs.yml` pour créer un job Databricks
- scripts Python adaptés aux chemins relatifs du bundle

## Fichiers principaux

- `json_to_csv.py` : convertit `url/url.json` en `url/csv_url.csv`
- `test_links.py` : teste les liens du CSV généré
- `scraping_scripts/scrap_script.py` : script Selenium de scraping

## Déploiement

1. Pousser le dépôt sur GitHub.
2. Configurer le Databricks CLI.
3. Depuis le dépôt local :

```bash
databricks bundle validate -t dev
```

4. Déployer en passant un cluster existant :

```bash
databricks bundle deploy -t dev --var="existing_cluster_id=<TON_CLUSTER_ID>"
```

5. Lancer le job :

```bash
databricks bundle run link_processing_job -t dev
```

## Remarque importante

Le job bundle fourni exécute `json_to_csv.py` puis `test_links.py`.
Le script Selenium (`scraping_scripts/scrap_script.py`) peut nécessiter une configuration spécifique du cluster si Chrome / ChromeDriver ne sont pas disponibles nativement.
