from notion_utils import query_unbilled_entries
import pandas as pd
from datetime import datetime

def extract_data_to_df(results):
    rows = []
    for r in results:
        props = r["properties"]
        rows.append({
            "Ville": props["Ville"]["select"]["name"] if props["Ville"]["select"] else None,
            "École": props["Ecole"]["select"]["name"] if props["Ecole"]["select"] else None,
            "Classe": props["Classe"]["select"]["name"] if props["Classe"]["select"] else None,
            "Nombre_heures": props["Nombre heures"]["number"],
            "Tarif_horaire": props["Tarif horaire"]["number"],
            "Total": props["Total"]["formula"]["number"],
            "Date": props["Date de début"]["date"]["start"],
        })
    return pd.DataFrame(rows)

def run_analysis():
    # Appelle les données de juin 2025 (exemple)
    results = query_unbilled_entries("2025-06-01", "2025-06-30", a_ete_facture=False)
    print(f"Résultats récupérés : {len(results)} lignes")
    
    df = extract_data_to_df(results)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Mois"] = df["Date"].dt.to_period("M")

    print("\n Heures et montants par ville :")
    ville_stats = df.groupby("Ville").agg({
        "École": pd.Series.nunique,
        "Nombre_heures": "sum",
        "Total": "sum"
    }).rename(columns={"École": "Nb_écoles"})
    print(ville_stats)

    print("\n Heures et montants par école et classe :")
    ecole_classe_stats = df.groupby(["École", "Classe"]).agg({
        "Nombre_heures": "sum",
        "Total": "sum"
    })
    print(ecole_classe_stats)

    print("\n Heures par mois :")
    heures_par_mois = df.groupby("Mois")["Nombre_heures"].sum()
    print(heures_par_mois)

if __name__ == "__main__":
    run_analysis()
