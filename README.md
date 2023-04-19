# The Extractor (GHDB Version)
<img src="extractor.png">
The Extractor is a Python script that extracts Google dorks from the official Google Hacking Database (GHDB) XML file and saves them in a CSV file. The script only extracts dorks that contain the "inurl:" operator because they are more specific and useful for targeted web scanning. It is only for education & example!!!!

## Prerequisites
- Python 3.x
- requests module (you can install it via pip: pip install requests)
- CSV module (built-in module in Python)
- uuid module (built-in module in Python)
## Usage
- if you want: download the GHDB XML file from the official GHDB repository: https://gitlab.com/exploit-database/exploitdb/-/tree/main/
- Save the file in the same directory as the Python script.
- Run the script:
```shell
python gextractor.py
```
or
```shell
python3 gextractor.py
```
- The script will check if an Internet connection is available. If yes, it will download the latest GHDB XML file. If no, it will use the local file (if available) or ask if you want to create a local copy of the GHDB XML file.
- The script will extract the dorks and save them in a CSV file named extracted_dorks.csv in the same directory as the script.
## Note
**The Extractor script is intended for educational and ethical purposes only. The extracted dorks should only be used for ethical hacking and web security testing. The script only extracts dorks that contain the "inurl:" operator because they are more specific and useful for targeted web scanning**

## Disclaimer
The authors of The Extractor do not condone illegal activities and are not responsible for any misuse of the extracted dorks. Always use the extracted dorks responsibly and in accordance with the law.

## createt by
Volkan S. Kücükbudak
## License
This project is licensed under the MIT - see the [LICENSE](LICENSE) file for details.
