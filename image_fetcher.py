"""
Ubuntu-Inspired Image Fetcher (Enhanced Version)
The Wisdom of Ubuntu: "I am because we are"

This program fetches one or multiple images from given URLs and saves them
into a directory called 'Fetched_Images'. It includes safeguards for handling
unknown sources, avoids duplicates, and checks HTTP headers before saving.

Ubuntu Principles:
- Community: Connects to the web to fetch shared images
- Respect: Handles errors gracefully
- Sharing: Organizes images for later access
- Practicality: Provides a useful real-world tool
"""

import os
import requests
from urllib.parse import urlparse
import hashlib

# Directory to store images
FOLDER_NAME = "Fetched_Images"
os.makedirs(FOLDER_NAME, exist_ok=True)

def get_filename_from_url(url):
    """Extract filename from URL or generate a default one."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:  # If no filename found
        filename = "downloaded_image.jpg"
    return filename

def is_duplicate(content):
    """Check if image already exists by comparing file hashes."""
    new_hash = hashlib.md5(content).hexdigest()
    for file in os.listdir(FOLDER_NAME):
        filepath = os.path.join(FOLDER_NAME, file)
        if os.path.isfile(filepath):
            with open(filepath, "rb") as f:
                existing_hash = hashlib.md5(f.read()).hexdigest()
                if new_hash == existing_hash:
                    return True
    return False

def fetch_image(url):
    """Fetch and save an image from a URL with safety checks."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes

        # Check headers before saving
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"Skipping {url} (not an image, Content-Type: {content_type})")
            return

        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > 5_000_000:  # 5 MB limit
            print(f"Skipping {url} (file too large)")
            return

        # Check for duplicates
        if is_duplicate(response.content):
            print(f"Duplicate image skipped: {url}")
            return

        # Extract filename
        filename = get_filename_from_url(url)
        filepath = os.path.join(FOLDER_NAME, filename)

        # Save file
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"Image saved: {filepath}")

    except requests.exceptions.MissingSchema:
        print(f"Invalid URL: {url}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error for {url}: {http_err}")
    except requests.exceptions.ConnectionError:
        print(f" Connection problem for {url}")
    except requests.exceptions.Timeout:
        print(f" Timeout error for {url}")
    except Exception as err:
        print(f"Unexpected error for {url}: {err}")

def main():
    # Prompt user for one or multiple URLs
    urls = input("Enter one or more image URLs (separated by commas): ").strip().split(",")

    for url in urls:
        url = url.strip()
        if url:
            fetch_image(url)

if __name__ == "__main__":
    main()
