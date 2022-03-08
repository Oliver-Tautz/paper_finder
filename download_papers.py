import csv
import subprocess
from os import makedirs,listdir
from utils import papers_read_from_csv,papers_write_to_csv
import re
import time 
from tqdm import tqdm
import argparse 

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--reverse', dest='accumulate', action='store_true', help='start with reverse list')

args = parser.parse_args()

CSV_NAME = "papers.csv"
OUTPUT_DIR =  "downloaded_papers"


papers = papers_read_from_csv(CSV_NAME)
if args.reverse:
    papers.reverse()


makedirs(OUTPUT_DIR,exist_ok=True)


for i,p in enumerate(tqdm(papers)):

    
    found = False
    downloaded_names =  listdir(OUTPUT_DIR)   
    for name in downloaded_names:
        if re.search(fr'"?{p.title}"?\.pdf',name,re.IGNORECASE):
            papers[i].filename = name
            found = True
    


    if not found:
        process = subprocess.run(['sopaper',f'\"{p.title}\"','-d',OUTPUT_DIR])
        time.sleep(60)
        papers[i].filename='not found'

if args.reverse:
    papers.reverse()
papers_write_to_csv(papers,CSV_NAME)
