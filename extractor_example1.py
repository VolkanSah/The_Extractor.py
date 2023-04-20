# Import necessary modules
import argparse
import logging




# Set up logger
logger = logging.getLogger(__name__)
lh = logging.StreamHandler()
logger.addHandler(lh)
formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt='%H:%M:%S')
lh.setFormatter(formatter)

# Set up argument parser
parser = argparse.ArgumentParser()

# Add argument for exporting data as XML
parser.add_argument('-xml', action='store_true', dest='export_xml',
                    help='Export data in a .xml-file')

# Add argument for exporting data as CSV
parser.add_argument('-csv', action='store_true', dest='export_csv',
                    help='Export data in a .csv-file')

# Add argument for exporting data as TXT
parser.add_argument('-txt', action='store_true', dest='export_txt',
                    help='Export data in a .txt-file')

# Add argument for exporting data to SQLite database
parser.add_argument('-sqlite', action='store_true', dest='export_sqlite',
                    help='Export data to a SQLite database')

# Parse arguments
results = parser.parse_args()

# Set logger level based on verbosity flag
logger.setLevel(logging.DEBUG if results.verbose else logging.INFO)
