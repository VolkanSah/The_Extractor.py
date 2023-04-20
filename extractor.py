import os
import csv
import uuid
import requests
from datetime import datetime
import xml.etree.ElementTree as ET
# URL for the GHDB XML file
URL = "https://gitlab.com/exploit-database/exploitdb/-/raw/main/ghdb.xml"

# Check if internet connection is available
def is_internet_available():
    try:
        requests.get("http://github.com/volkansah")
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
