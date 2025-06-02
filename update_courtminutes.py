import os
from pyairtable import Api, Table

# Airtable setup
api_key = os.environ.get("KEY")  # Set this secret in GitHub Actions later
base_id = "appwbCU6BAWOA1AQX"  # High Profile Cases base
table_id = "tblb0yIYr91PzghXQ"

# Field IDs
SUSPECT_FIELD = "fldSksphlpQbNoPG9"
CASE_FIELD = "fldHbD4I1ulAn3r00"
COURTMINUTES_FIELD = "fldt5zLdVdCogoqtR"

def main():
    api = Api(api_key)
    table = Table(api_key, base_id, table_id)
    
    records = table.all(view="Grid view", fields=["Suspect Name", "Case #"])
    
    for record in records:
        fields = record.get("fields", {})
        case_number = fields.get("Case #")
        if case_number:
            link = f"https://www.superiorcourt.maricopa.gov/docket/CriminalCourtCases/caseInfo.asp?caseNumber={case_number}"
            table.update(record["id"], { "Courtminutes": link })
            print(f"Updated {fields.get('Suspect Name')} with link: {link}")

if __name__ == "__main__":
    main()
