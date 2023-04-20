#!/usr/bin/env python
import os
import csv
import uuid
import requests
from datetime import datetime
import xml.etree.ElementTree as ET
import argparse
import logging

# Set up logger
logger = logging.getLogger(__name__)
lh = logging.StreamHandler()
logger.addHandler(lh)
formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt='%H:%M:%S')
lh.setFormatter(formatter)

# Set up argument parser
parser = argparse.ArgumentParser(description='Extract Google dorks from the official Google Hacking Database (GHDB) and save them in various file formats.')
parser.add_argument('-xml', action='store_true', dest='export_xml', help='Export data in a .xml-file')
parser.add_argument('-csv', action='store_true', dest='export_csv', help='Export data in a .csv-file')
parser.add_argument('-txt', action='store_true', dest='export_txt', help='Export data in a .txt-file')
parser.add_argument('-sqlite', action='store_true', dest='export_sqlite', help='Export data to a SQLite database')
results = parser.parse_args()

# Set logger level based on export flags
if any([results.export_xml, results.export_csv, results.export_txt, results.export_sqlite]):
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

class color:
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

    @staticmethod
    def log(lvl, col, msg):
        logger.log(lvl, col + msg + color.END)

# Print header
print(color.BOLD + color.RED + """

▄▄▄█████▓ ██░ ██ ▓█████    ▓█████ ▒██   ██▒▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄  ▄▄▄█████▓ ▒█████   ██▀███  
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█   ▀ ▒▒ █ █ ▒░▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒███   ░░  █   ░▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓█  ▄  ░ █ █ ▒ ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒████▒▒██▒ ▒██▒  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░░ ▒░ ░▒▒ ░ ░▓ ░  ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
    ░     ▒ ░▒░ ░ ░ ░  ░    ░ ░  ░░░   ░▒ ░    ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒       ░      ░ ▒ ▒░   ░▒ ░ ▒░
  ░       ░  ░░ ░   ░         ░    ░    ░    ░        ░░   ░   ░   ▒   ░          ░      ░ ░ ░ ▒    ░░   ░ 
          ░  ░  ░   ░  ░      ░  ░ ░    ░              ░           ░  ░░ ░                   ░ ░     ░     
                                                                       ░                                   
Copyright (2008-24 ) S. Volkan Kücükbudak  
(Source: https://github.com/VolkanSah/The_Extractor.py)
The Extractor is a Python script that extracts Google dorks from the official Google Hacking Database (GHDB) and saves them in various file formats.
The script only extracts dorks that contain the "inurl:" operator because they are more specific and useful for targeted web scanning.
WARNING: The Extractor script is intended for educational and ethical purposes only. 
The extracted dorks should only be used for ethical hacking and web security testing. The author and the publisher of the script are not 
responsible for any misuse or illegal activities.
Createt for Poision Ivory
Usage: extractorpy <option> <filename>
""" + color.END)

# URL for the GHDB XML file
URL = "https://gitlab.com/exploit-database/exploitdb/-/raw/main/ghdb.xml"

# Check if internet connection is available
def is_internet_available():
    try:
        requests.get("https://github.com/VolkanSah")
        return True
    except:
        return False

# Download the GHDB XML file if internet is available
def download_xml():
    if is_internet_available():
        print("Internet connection available. Downloading GHDB XML file...")
        response = requests.get(URL)
        if response.status_code == 200:
            with open("ghdb.xml", "wb") as f:
                f.write(response.content)
        else:
            print(f"Failed to download GHDB XML file. Status code: {response.status_code}")
    else:
        print("Internet connection not available. Looking for local GHDB XML file...")
        if os.path.isfile("ghdb.xml"):
            print("Local GHDB XML file found.")
        else:
            print("Local GHDB XML file not found. Do you want to create a new one? (y/n)")
            answer = input()
            if answer.lower() == "y":
                with open("ghdb.xml", "w") as f:
                    f.write("<ghdb>\n</ghdb>")
                    print("New GHDB XML file created.")
            else:
                print("No GHDB XML file created. Exiting...")
                exit()

# Extract the relevant data from the GHDB XML file and write it to a CSV file
def extract_data():
    tree = ET.parse("ghdb.xml")
    root = tree.getroot()
    with open("extractor_data.csv", "w", newline="") as csvfile:
        fieldnames = ["id", "name", "query", "date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in root.findall("entry"):
            query = entry.find("query").text
            if "inurl:" in query:
                query = query.replace("inurl:", "")
                name = entry.find("shortDescription").text
                date = datetime.strptime(entry.find("date").text, "%Y-%m-%d")
                id = str(uuid.uuid4())
                writer.writerow({"id": id, "name": name, "query": query, "date": date})

# Main function
def main():
    download_xml()
    extract_data()

if __name__ == "__main__":
    main()
