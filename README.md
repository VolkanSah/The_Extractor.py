# The Extractor (GHDB) lite
<img src="extractor.png">
The Extractor is a Python script that extracts Google dorks from the official Google Hacking Database (GHDB) and saves them in a CSV-file. The script only extracts dorks that contain the "inurl:" operator because they are more specific and useful for targeted web scanning.

## Warning: 
The Extractor script is intended for educational and ethical purposes only. The extracted dorks should only be used for ethical hacking and web security testing. The authors of The Extractor do not condone illegal activities and are not responsible for any misuse of the extracted dorks. Always use the extracted dorks responsibly and in accordance with the law.

## Prerequisites
The script has been tested on Linux/Unix Bash-installed systems.
- Python 3.x
- requests module (you can install it via pip: pip install requests)
- CSV module (built-in module in Python)
- uuid module (built-in module in Python)
## Usage
- Download the GHDB XML file from the official GHDB repository: https://gitlab.com/exploit-database/exploitdb/-/tree/main/
- Save the file in the same directory as the Python script.
## Run the script:
```shell
python extractor.py 
```
or

```shell
python3 extractor.py
```



- The script will check if an Internet connection is available. If yes, it will download the latest GHDB XML file. If no, it will use the local file (if available) or ask if you want to create a local copy of the GHDB XML file.
- The script will extract the dorks and save them in the specified output format (CSV by default) in the same directory as the script.
## Note
- The Extractor script only extracts dorks that contain the "inurl:" operator because they are more specific and useful for targeted web scanning.
- The Extractor (Nemesis Version) is now included in
```
              .__                      .__                          
______   ____ |__| __________   ____   |__| __  _____________ ___.__.
\____ \ /  _ \|  |/  ___/  _ \ /    \  |  \  \/ /  _ \_  __ <   |  |
|  |_> >  <_> )  |\___ (  <_> )   |  \ |  |\   (  <_> )  | \/\___  |
|   __/ \____/|__/____  >____/|___|  / |__| \_/ \____/|__|   / ____|
|__|  nemesis v.2.5.23 \/           \/   © 2008-2023 Volkan Sah   \/   
```
## Disclaimer
The authors of The Extractor do not condone illegal activities and are not responsible for any misuse of the extracted dorks. Always use the extracted dorks responsibly and in accordance with the law.
## Copyright
S. Volkan Kücükbudak
## License
This project is licensed under the MIT - see the [LICENSE](LICENSE) file for details.
