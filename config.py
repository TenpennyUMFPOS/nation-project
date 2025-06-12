from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis .env
load_dotenv()

# Récupérer les valeurs
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DB_INTERVENTIONS_ID = os.getenv("DB_INTERVENTIONS_ID")
DB_INVOICES_ID = os.getenv("DB_INVOICES_ID")

# Headers de l'API Notion
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}