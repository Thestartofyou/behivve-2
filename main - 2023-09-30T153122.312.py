import sqlite3
import random

# Create a SQLite database connection
conn = sqlite3.connect('realestate_leads.db')

# Create a table to store leads
conn.execute('''
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY,
        name TEXT,
        zip_code TEXT
    )
''')

# Simulated data sources (replace with real data sources)
buyer_leads = [
    {"name": "Buyer 1", "zip_code": "90210"},
    {"name": "Buyer 2", "zip_code": "90210"},
    {"name": "Buyer 3", "zip_code": "94110"},
]

seller_leads = [
    {"name": "Seller 1", "zip_code": "90210"},
    {"name": "Seller 2", "zip_code": "94110"},
    {"name": "Seller 3", "zip_code": "90210"},
]

# Simulated CRM system (replace with a real CRM system integration)
crm_system = []

# Simulate CRM data with some random leads
for i in range(10):
    lead = random.choice(buyer_leads + seller_leads)
    crm_system.append(lead)
    # Insert the lead into the database
    conn.execute('INSERT INTO leads (name, zip_code) VALUES (?, ?)', (lead['name'], lead['zip_code']))

# Commit the changes to the database
conn.commit()

# Define the desired zip code
desired_zip_code = "90210"

# Retrieve leads from the database based on the desired zip code
cursor = conn.execute('SELECT name, zip_code FROM leads WHERE zip_code = ?', (desired_zip_code,))
filtered_leads = cursor.fetchall()

# Generate a report
print(f"Leads in Zip Code {desired_zip_code}:")
for lead in filtered_leads:
    print(f"Name: {lead[0]}, Zip Code: {lead[1]}")

# Close the database connection
conn.close()

