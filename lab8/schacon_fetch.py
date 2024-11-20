#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import json

# Read the JSON file
with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)

# Open the CSV file for writing
with open('chacon.csv', 'w') as csv_file:
    # Write the header (if needed)
    # csv_file.write("name,html_url,updated_at,visibility\n")

    # Loop through the first 5 repositories
    for repo in data[:5]:  # Limit to 5 lines
        # Extract the required fields
        name = repo.get('name')
        html_url = repo.get('html_url')
        updated_at = repo.get('updated_at')
        visibility = repo.get('visibility')

        # Create the CSV line
        csv_line = f"{name},{html_url},{updated_at},{visibility}\n"

        # Write the line to the CSV file
        csv_file.write(csv_line)

print("Data written to chacon.csv successfully.")
