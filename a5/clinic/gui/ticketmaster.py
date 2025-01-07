import requests
from requests.auth import HTTPBasicAuth
import time
import hashlib

def get_website_content(url, auth=None, headers=None):
    """
    Fetch the content of a password-protected website.
    """
    try:
        response = requests.get(url, auth=auth, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

def hash_content(content):
    """
    Generate a hash of the website content for comparison.
    """
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def monitor_website(url, username, password, check_interval=60, headers=None):
    """
    Monitor a password-protected website for changes.
    """
    print(f"Monitoring {url} every {check_interval} seconds...")
    auth = HTTPBasicAuth(username, password)
    previous_hash = None
    
    while True:
        content = get_website_content(url, auth=auth, headers=headers)
        if content is None:
            time.sleep(check_interval)
            continue
        
        current_hash = hash_content(content)
        
        if previous_hash and current_hash != previous_hash:
            print(f"Change detected on {url} at {time.ctime()}!")
        elif not previous_hash:
            print(f"Monitoring started for {url}. No changes yet.")
        
        previous_hash = current_hash
        time.sleep(check_interval)

if __name__ == "__main__":
    # Replace these with your credentials and URL
    website_url = "https://www.ticketmaster.ca/taylor-swift-tickets/artist/1094215"
    username = "makenadyck05@gmail.com"
    password = "kappaalphatheta4ever"
    monitor_interval = 60  # Check every 60 seconds

    monitor_website(website_url, username, password, monitor_interval)