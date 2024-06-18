# Web Scraping and Data Extraction Script

This Python script performs web scraping to extract email addresses, phone numbers, and addresses from web pages. It then saves the extracted data into an Excel file.

## Requirements

To run this script, you need to have the following installed:

- Python 3.x
- requests library
- beautifulsoup4 library
- pandas library
- openpyxl library

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/samwelnyandoro/Python-Script-For-Web-Scrapping.git
```

2. Navigate to the directory containing the script:

```bash
cd Python-Script-For-Web-Scrapping
```

3. Edit the script (`s.py`) and add the URLs you want to scrape in the `urls` list:

```python
if __name__ == "__main__":
    urls = [
        "http://example.com",
        "https://example.org",
        # Add more URLs here
    ]
```

4. Run the script:

```bash
python s.py
```

Make sure to replace `"http://example.com"` and `"https://example.org"` with the actual URLs you want to scrape.

## Note

- The script uses GET requests by default. You can change it to POST requests if needed by modifying the `method` variable in the `__main__` block.

- If the web pages use SSL certificates that are not valid or have issues, you may need to disable SSL verification by setting `verify=False` in the `requests.get` and `requests.post` calls. This is done in the `fetch_html_get` and `fetch_html_post` functions.

Feel free to modify the instructions as needed for your specific use case or repository structure.