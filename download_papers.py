import csv
import subprocess
from os import makedirs,listdir
from utils import papers_read_from_csv,papers_write_to_csv
import re

INPUT_CSV_NAME = "papers.csv"
OUTPUT_CSV_NAME = "papers_downloaded.csv"
OUTPUT_DIR =  "downloaded_papers"


papers = papers_read_from_csv(INPUT_CSV_NAME)
#papers.reverse()

makedirs(OUTPUT_DIR,exist_ok=True)


for i,p in enumerate(papers[0:10]):
    if not p.filename:
        process = subprocess.run(['sopaper',f'\"{p.title}\"','-d',OUTPUT_DIR])
    downloaded_names =  listdir(OUTPUT_DIR)   
    for name in downloaded_names:
        if re.search(fr'"?{p.title}"?\.pdf',name,re.IGNORECASE):
            papers[i].filename = name
papers_write_to_csv(papers,OUTPUT_CSV_NAME)
