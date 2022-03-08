import csv
import subprocess
from os import makedirs,listdir
from utils import papers_read_from_csv,papers_write_to_csv
import re
import time 
from tqdm import tqdm

CSV_NAME = "papers.csv"
OUTPUT_DIR =  "downloaded_papers"


papers = papers_read_from_csv(CSV_NAME)
papers.reverse()

makedirs(OUTPUT_DIR,exist_ok=True)


for i,p in enumerate(tqdm(papers)):
    if not p.filename or p.filename=="not found":
        process = subprocess.run(['sopaper',f'\"{p.title}\"','-d',OUTPUT_DIR])
        time.sleep(60)
    downloaded_names =  listdir(OUTPUT_DIR)   
    found = False
    for name in downloaded_names:
        if re.search(fr'"?{p.title}"?\.pdf',name,re.IGNORECASE):
            papers[i].filename = name
            found = True
    if not found:
        papers[i].filename='not found'


papers.reverse()
papers_write_to_csv(papers,CSV_NAME)
