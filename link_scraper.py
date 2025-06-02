import os
from pyairtable import Api, Table

# Airtable credentials from GitHub Secrets
api_key = os.environ["AIRTABLE_API_KEY"]
BASE_ID = "appwbCU6BAWOA1AQX"
TABLE_ID = "tblb0yIYr91PzghXQ"

api = Api(api_key)
table = Table(api_key, BASE_ID, TABLE_ID)

records = table.all(fields=["Suspect Name", "Case #"])

for record in records:
    fields = record.get("fields", {})
    case_number = fields.get("Case #")
    if case_number:
        url = f"https://www.superiorcourt.maricopa.gov/docket/CriminalCourtCases/caseInfo.asp?caseNumber={case_number}"
        table.update(record["id"], {"Courtminutes": url})
        print(f"Updated {fields.get('Suspect Name')} → {url}")
