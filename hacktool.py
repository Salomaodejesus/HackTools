import requests
from bs4 import BeautifulSoup
import re

# Define the target website
target_url = input("__")

def check_robots_txt(url):
    robots_url = url + "/robots.txt"
    try:
        response = requests.get(robots_url)
        if response.status_code == 200:
            print(f"[+] Found robots.txt at {robots_url}")
            print(response.text)
        else:
            print("[-] robots.txt not found")
    except Exception as e:
        print(f"[-] Error checking robots.txt: {e}")

def scan_forms(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        if forms:
            print(f"[+] Found {len(forms)} form(s) on {url}")
            for form in forms:
                print(f"Form action: {form.get('action')}")
                print(f"Form method: {form.get('method')}")
                print("Inputs:")
                for input_tag in form.find_all('input'):
                    print(f" - {input_tag.get('name')} (type: {input_tag.get('type')})")
        else:
            print("[-] No forms found")
    except Exception as e:
        print(f"[-] Error scanning forms: {e}")

def find_emails(url):
    try:
        response = requests.get(url)
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", response.text)
        if emails:
            print(f"[+] Found {len(emails)} email(s):")
            for email in emails:
                print(f" - {email}")
        else:
            print("[-] No emails found")
    except Exception as e:
        print(f"[-] Error finding emails: {e}")

def main():
    print(f"Starting scan on {target_url}\n")
    
    # Check for robots.txt
    check_robots_txt(target_url)
    
    # Scan for forms
    print("\nScanning for forms...")
    scan_forms(target_url)
    
    # Find email addresses
    print("\nFinding email addresses...")
    find_emails(target_url)

if __name__ == "__main__":
    main()
