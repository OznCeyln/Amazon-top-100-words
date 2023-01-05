import requests
from bs4 import BeautifulSoup
import openpyxl

# Make a request to the Amazon website
response = requests.get("https://www.amazon.com/gp/most-gifted/")

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the div elements with the "sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col most-gifted-color-4" class
items = soup.find_all("div", class_="sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col most-gifted-color-4")

# Create a new Excel workbook
workbook = openpyxl.Workbook()

# Create a sheet for the data
sheet = workbook.active

# Add a header row
sheet.append(["Keyword"])

# Add the 100 most searched words to the sheet
for item in items:
    title = item.find("span", class_="a-size-medium a-color-base a-text-normal").text
    sheet.append([title])

# Save the workbook to a file
workbook.save("keywords.xlsx")
