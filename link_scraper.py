from pyairtable import Api
import os

api_key = os.environ["AIRTABLE_API_KEY"]
BASE_ID = "appwbCU6BAWOA1AQX"
TABLE_ID = "tblb0yIYr91PzghXQ"

# Proper method using .table()
api = Api(api_key)
table = api.table(BASE_ID, TABLE_ID)

records = table.all(fields=["Suspect Name", "Case #"])

for record in records:
    fields = record.get("fields", {})
    case_number = fields.get("Case #")
    if case_number:
        url = f"https://www.superiorcourt.maricopa.gov/docket/CriminalCourtCases/caseInfo.asp?caseNumber={case_number}"
        table.update(record["id"], {"Court Docket": url})
        print(f"Updated {fields.get('Suspect Name')} → {url}")
