







# Example arguments 
logger = logging.getLogger(__name__)
lh = logging.StreamHandler()  # Handler for the logger
logger.addHandler(lh)
formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt='%H:%M:%S')
lh.setFormatter(formatter)
# 5.2 parse your arguments
parser = argparse.ArgumentParser()

parser.add_argument('-xml', action='generate_xml', dest='export_xml',
                    help='Export data in a .xml-file')
parser.add_argument('-csv', action='generate_csv', dest='export_csv',
                    help='Export data in a .csv-file')
parser.add_argument('-txt', action='generate_txt', dest='export_txt',
                    help='Export data in a .txt-file')
parser.add_argument('-sqlite', action='generate_sqlite', dest='export_sqlite',
                    help='Space separated list of cookies',
                    nargs='+', default=[])
results = parser.parse_args()
logger.setLevel(logging.DEBUG if results.verbose else logging.INFO)
