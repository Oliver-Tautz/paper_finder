from odf.opendocument import load
from odf import text, teletype
from paper import Paper
import re
import csv        

# load odt
odt = load('AH Paper.doc.odt')

# get all lines in a list
lines = list(odt.getElementsByType(text.P))

# convert to text
lines = list([teletype.extractText(l) for l in lines])

# join (deleting linebreaks)
fulltext  = "".join(lines)


# regex pattern for date of the form "1982:". Use parenthesis to keep matches in list.
date_string_pattern = r'(\d{4}\:)'
date_pattern = re.compile(date_string_pattern)

# split the text at the dates. Now its a list with matches and non matches in order of appearence.
split_by_date = (re.split(date_pattern,fulltext)[1:])


# list of all papers
papers = []
# pattern for iderts of the form "128*?.\t"
id_string_pattern = r'(\d{1,3}\*?\.\t)'
id_pattern = re.compile(id_string_pattern)

# loop over matches.
for i,by_date in enumerate(split_by_date):
    if (re.match(date_pattern,by_date)):
        # we found a date so the next entry is the text of multiple papers.
        split_by_id = re.split(id_pattern,split_by_date[i+1])
        # loop over matches for ids.
        for j,by_id in enumerate(split_by_id):
            if re.match(id_pattern,by_id):
                new_paper = Paper.from_text(by_id,by_date[0:4],split_by_id[j+1])
                papers.append(new_paper)
         
with open('test.csv','w',newline='') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames = papers[0].to_dict().keys(),delimiter = ';')
    writer.writeheader()

    for paper in papers:
        writer.writerow(paper.to_dict())



