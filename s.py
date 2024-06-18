import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook

# Function to make a GET request and fetch the HTML content
def fetch_html_get(url):
    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve {url}")
            return None
    except requests.exceptions.SSLError as e:
        print(f"SSL error for {url}: {e}")
        return None

# Function to make a POST request and fetch the HTML content
def fetch_html_post(url, data):
    try:
        response = requests.post(url, data=data, verify=False)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve {url} with POST data {data}")
            return None
    except requests.exceptions.SSLError as e:
        print(f"SSL error for {url} with POST data {data}: {e}")
        return None

# Function to extract email addresses
def extract_emails(html):
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    return email_pattern.findall(html)

# Function to extract phone numbers
def extract_phones(html):
    phone_pattern = re.compile(r'\+?[0-9]{1,4}?[-.\s]?[0-9]{2,3}[-.\s]?[0-9]{2,3}[-.\s]?[0-9]{4,6}')
    return phone_pattern.findall(html)

# Function to extract addresses
def extract_addresses(html):
    address_pattern = re.compile(r'\d{1,4} [\w\s]{1,20}, [\w\s]{1,20}, [A-Z]{2} \d{5}')
    return address_pattern.findall(html)

# Function to save data to an Excel file
def save_to_excel(url, emails, phones, addresses, filename='scraped_data.xlsx'):
    data = {
        'URL': [url] * max(len(emails), len(phones), len(addresses)),
        'Emails': emails,
        'Phone Numbers': phones,
        'Addresses': addresses
    }
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

    try:
        book = load_workbook(filename)
        writer = pd.ExcelWriter(filename, engine='openpyxl')
        writer.book = book
        writer.sheets = {ws.title: ws for ws in book.worksheets}
        reader = pd.read_excel(filename)
        df.to_excel(writer, index=False, header=False, startrow=len(reader)+1)
    except FileNotFoundError:
        writer = pd.ExcelWriter(filename, engine='openpyxl')
        df.to_excel(writer, index=False)
    
    writer.close()
    print(f"Data saved to {filename}")

# Main function to scrape a website
def scrape_website(url, method="GET", data=None):
    if method.upper() == "GET":
        html_content = fetch_html_get(url)
    elif method.upper() == "POST":
        html_content = fetch_html_post(url, data)
    else:
        print("Invalid method. Use 'GET' or 'POST'.")
        return
    
    if html_content:
        emails = extract_emails(html_content)
        phones = extract_phones(html_content)
        addresses = extract_addresses(html_content)
        
        print("Emails found:", emails)
        print("Phone numbers found:", phones)
        print("Addresses found:", addresses)
        
        save_to_excel(url, emails, phones, addresses)

# Example usage
if __name__ == "__main__":
    urls = [
        #"http://example.com",
    ]
    method = "GET"  # Change to "POST" if needed
    data = None  # Add POST data if needed, e.g., {'key': 'value'}
    
    for url in urls:
        scrape_website(url, method, data)
