from notion_utils import get_database_properties
from config import DB_INTERVENTIONS_ID

props = get_database_properties(DB_INTERVENTIONS_ID)

for prop_name, prop_data in props["properties"].items():
    print(f"{prop_name}: type = {prop_data['type']}")
