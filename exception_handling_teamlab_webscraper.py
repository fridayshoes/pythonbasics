# Team Lab:
# Build a simple web scraper using the requests module.
# 
# - The program should prompt the user for a URL. 
# - The team must implement comprehensive error handling to 
# catch potential requests.exceptions.RequestException 
# (e.g., invalid URL, no internet connection) and 
# print user-friendly error messages instead of crashing.


import requests

while True:
  try:
    url = input("Please enter your URL: ")
    response = requests.get(url) # reuest module scrapes the URL and gets a response code
    if response.status_code == 200:
      print("Great your URL is working!")
      break
    else:
      print(f"URL returned status code {response.status_code}. Please try again.")
  except requests.exceptions.MissingSchema:
    print("Not a valid URL format. Did you include 'http://' or 'https://' or '.com' or '.co.uk'?")
  except requests.exceptions.ConnectionError:
    print("Could not connect to the URL. Please check your internet connection or the URL itself.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")