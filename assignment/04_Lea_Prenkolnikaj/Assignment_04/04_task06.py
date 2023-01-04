#Task 06: Download File

import logging
import urllib.request


def download_file(url, path):
    # Check if the URL points to a .txt file
    if not url.endswith(".txt"):
        # Log an error message
        logging.error("No text file found at given URL, download aborted!")
        return

    try:
        # Download the file from the URL and write it to the specified path
        urllib.request.urlretrieve(url, path)

    except Exception as e:
        # Log the error message
        logging.error(e)


# Test the function with the URL of a .txt file
download_file("https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt", "macbeth.txt")
