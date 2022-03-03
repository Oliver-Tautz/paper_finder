import csv
import subprocess
from os import makedirs
from utils import papers_read_from_csv

INPUT_CSV_NAME = "papers.csv"
OUTPUT_CSV_NAME = "papers_downloaded.csv"
OUTPUT_DIR =  "downloaded_papers"


papers = papers_read_from_csv(INPUT_CSV_NAME)
makedirs(OUTPUT_DIR,exist_ok=True)


for p in papers:
    process = subprocess.run(['sopaper',f'\"{p.title}\"','-d',OUTPUT_DIR])
    print(process)

