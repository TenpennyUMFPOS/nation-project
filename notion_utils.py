import requests
from datetime import datetime
from config import DB_INVOICES_ID, HEADERS

def create_invoice_page(client: str, interventions: list, total: float, invoice_number: str):
    mois = datetime.now().strftime("%B %Y")  # Exemple : "Juin 2025"

    # Création des blocs "paragraph" pour chaque ligne d'intervention
    children = []
    for item in interventions:
        props = item["properties"]
        cours = props["Cours"]["title"][0]["plain_text"] if props["Cours"]["title"] else "Sans titre"
        heures = props["Nombre heures"]["number"]
        tarif = props["Tarif horaire"]["number"]
        ligne = f"{cours} – {heures}h x {tarif}€/h = {heures * tarif}€"

        children.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": ligne}
                    }
                ]
            }
        })

    # Payload pour la page de facture
    payload = {
        "parent": {"database_id": DB_INVOICES_ID},
        "properties": {
            "Nom": {  # Titre de la facture
                "title": [
                    {"text": {"content": f"Facture {invoice_number} – {client}"}}
                ]
            },
            "Client": {
                "rich_text": [
                    {"text": {"content": client}}
                ]
            },
            "Mois": {
                "rich_text": [
                    {"text": {"content": mois}}
                ]
            },
            "Total": {
                "number": total
            }
        },
        "children": children
    }

    response = requests.post("https://api.notion.com/v1/pages", headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()


from config import DB_INTERVENTIONS_ID

def query_unbilled_entries(date_begin: str, date_end: str, a_ete_facture: bool):
    date_filter = [
        {"property": "Date de début", "date": {"on_or_after": date_begin}},
        {"property": "Date de début", "date": {"before": date_end}}
    ]

    if a_ete_facture is not None:
        date_filter.append({
            "property": "Facturé",
            "checkbox": {"equals": a_ete_facture}
        })

    query = {
        "filter": {
            "and": date_filter
        }
    }

    response = requests.post(
        f"https://api.notion.com/v1/databases/{DB_INTERVENTIONS_ID}/query",
        headers=HEADERS,
        json=query
    )
    response.raise_for_status()
    return response.json()["results"]
