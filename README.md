📸 Ubuntu-Inspired Image Fetcher

“I am because we are” — Ubuntu Philosophy

This project is a Python program that connects to the internet, fetches one or more images from given URLs, and saves them into a local folder. It demonstrates values of community, respect, sharing, and practicality through careful design and error handling.


🎯 Features

Accepts one or multiple image URLs at once (comma-separated).

Creates a Fetched_Images folder automatically if it doesn’t exist.

Validates that the resource is a proper image before saving.

Prevents saving duplicate images by checking file contents.

Skips overly large files to avoid unsafe downloads.

Handles errors gracefully (invalid URLs, connection problems, timeouts).


🛠️ Requirements

Python 3.x installed


requests
 library


You can install requests by running:

pip install requests


🚀 How to Use

Run the program in your terminal or command prompt:

python image_fetcher.py



When prompted, enter one or more image URLs, separated by commas.
Example:

https://www.python.org/static/community_logos/python-logo.png



The program will:

Fetch each image

Validate that it is safe and correct

Save it inside the Fetched_Images folder

Open the Fetched_Images folder in your project directory to view your downloaded images.


✅ Example Run
Enter one or more image URLs (separated by commas): https://www.python.org/static/community_logos/python-logo.png

✅ Image saved: Fetched_Images/python-logo.png


📂 Output Folder Structure
Fetched_Images/
  ├── python-logo.png


🔒 Safety Precautions Implemented

Content-Type check: Only saves valid images (image/png, image/jpeg, etc.).

File size limit: Skips files larger than 5 MB.

Duplicate check: Uses file hashing to avoid saving duplicates.


✨ Ubuntu Principles in Action

Community → Fetches from shared resources on the internet

Respect → Handles errors gracefully and avoids unsafe actions

Sharing → Organizes images for later use in a dedicated folder

Practicality → Provides a simple, useful real-world utility

This program is both a technical tool and a reflection of Ubuntu values: building tools that serve people respectfully and responsibly.
