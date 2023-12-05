import json
import requests
from tinydb import TinyDB, Query


def get_orders(url):
    page = requests.get(url)
    results = page.json()

    db = TinyDB("eo.json")

    db.insert_multiple(reversed(results["results"]))

    return None if "next_page_url" not in results else results["next_page_url"]


url = "https://www.federalregister.gov/api/v1/documents.json?conditions%5Bcorrection%5D=0&conditions%5Bpresidential_document_type%5D=executive_order&conditions%5Btype%5D%5B%5D=PRESDOCU&fields%5B%5D=citation&fields%5B%5D=document_number&fields%5B%5D=end_page&fields%5B%5D=html_url&fields%5B%5D=pdf_url&fields%5B%5D=type&fields%5B%5D=subtype&fields%5B%5D=publication_date&fields%5B%5D=signing_date&fields%5B%5D=start_page&fields%5B%5D=title&fields%5B%5D=disposition_notes&fields%5B%5D=executive_order_number&fields%5B%5D=full_text_xml_url&fields%5B%5D=body_html_url&fields%5B%5D=json_url&order=executive_order&per_page=1222"

while url:
    print(url)
    url = get_orders(url)
