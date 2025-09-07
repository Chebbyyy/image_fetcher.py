"""
Ubuntu-Inspired Image Fetcher
The Wisdom of Ubuntu: "I am because we are"

This program prompts the user for an image URL, fetches the image from
the internet, and saves it in a directory called 'Fetched_Images'.
It handles errors gracefully, following the Ubuntu values of community,
respect, sharing, and practicality.
"""

import os
import requests
from urllib.parse import urlparse

def fetch_image():
    # Prompt user for image URL
    url = input("Enter the image URL: ").strip()
    
    # Create directory if it doesn't exist
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename found, set a default
        if not filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join(folder_name, filename)

        # Save the image in binary mode
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"Image successfully saved as: {filepath}")

    except requests.exceptions.MissingSchema:
        print("Error: Invalid URL. Please enter a valid image link.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Connection problem. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Try again later.")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")


if __name__ == "__main__":
    fetch_image()
