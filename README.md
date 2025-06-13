# Notion Invoice Automation – Python Project

This project automates the generation of invoices from a Notion database containing freelance teaching interventions. It uses the Notion API and Python to filter, analyze, and create invoice pages.

---

## Project Structure

├──  data
    ├── screenshots
├── .env 
├── analyse.py # Script for data analysis with Pandas
├── notion_utils.py # Utility functions for interacting with Notion
├── config.py # Loads secrets and headers
├── README.md # Project documentation



## Step-by-Step Progress

### Step 0: Environment Setup

- Created a `.env` file with the following variables:

### Step 1: Define Notion API Headers

- Set up required headers for authentication and versioning:
    HEADERS = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }



### Step 2 (continued): Data Analysis with Pandas
 - Created analyse.py:

    Extracted data from Notion results into a DataFrame

    Performed the following aggregations:

    By City: number of schools, total hours, total amount

    By School and Class: hours and total billed

    By Month: hours taught



### Step 3: Create Invoice Page
- Created create_invoice_page(client, interventions, total, invoice_number):

    Adds a new page in the Factures database

    Populates fields:

    Client name

    Month

    Total

    Children blocks summarizing each intervention    



### Technologies Used
- Python 3

- Notion API

- requests

- pandas

- python-dotenv    



# FACTURE
Client : Université Lyon 1
Mois : 2025-06
--------------------------------------
## Détail des interventions
Cours | Heures | Tarif | Total
--- | --- | --- | ---
Python avancé | 4h | 80€ | 320€
ML appliquée | 3h | 90€ | 270€

Total à payer : 590 €
