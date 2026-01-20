import requests
import pandas as pd
import os

def scrape_dentist_data_ny():
    """
    Automated scraper to extract dentist contact information 
    from the official NPI Registry API.
    """
    print("--- Connecting to NPI Registry Server (Target: New York Dentists) ---")
    
    # API endpoint with filters: New York City, Taxonomy: Dentist
    api_url = "https://npiregistry.cms.hhs.gov/api/?version=2.1&city=NEW%20YORK&taxonomy_description=DENTIST&limit=10"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(api_url, headers=headers, timeout=20)
        json_data = response.json()
        
        # Checking result count from the server response
        result_count = json_data.get('result_count', 0)
        print(f"Server Responded. Found {result_count} records.")

        results = json_data.get('results', [])

        if not results:
            print("Server connected, but search results are empty.")
            return

        formatted_data = []
        for item in results:
            basic_info = item.get('basic', {})
            
            # Logic to handle organization name or personal name
            name = basic_info.get('organization_name') or f"{basic_info.get('first_name', '')} {basic_info.get('last_name', '')}"
            
            addresses = item.get('addresses', [])
            addr = addresses[0] if addresses else {}
            
            # Building structured address string
            full_address = f"{addr.get('address_1', '')}, {addr.get('city', '')}, {addr.get('state', '')} {addr.get('postal_code', '')}"
            phone = addr.get('telephone_number', 'N/A')

            formatted_data.append({
                "Contractor Name": name.strip().upper(),
                "Full Address": full_address.strip(),
                "Phone Number": phone
            })

        # Save to Excel
        df = pd.DataFrame(formatted_data)
        filename = "NY_Dentist_Leads.xlsx"
        df.to_excel(filename, index=False)
        
        print(f"--- SUCCESS ---")
        print(f"File '{filename}' has been generated in your workspace.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_dentist_data_ny()