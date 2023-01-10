Task 04: HTTP Request

import urllib.request


def open_url(url):
    try:
        # Establish a HTTP connection to the website and retrieve the html resource
        with urllib.request.urlopen(url) as response:
            html = response.read()

            # Print the first 200 characters of the html resource
            print(html[:200])
    except urllib.error.URLError:
        # Print an error message if there is an exception
        print("An error occurred while trying to connect to the website")
    except ValueError:
        # Print an error message if there is an exception
        print("Invalid URL")


# Test the function with an arbitrary URL
open_url("https://www.example.com")
