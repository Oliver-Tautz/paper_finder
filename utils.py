import csv
from paper import Paper


def papers_write_to_csv(papers,output_filename):
    with open(output_filename,'w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames = papers[0].to_dict().keys(),delimiter = ';')
        writer.writeheader()
    
        for paper in papers:
            writer.writerow(paper.to_dict())


        csvfile.close()

def papers_read_from_csv(filename):
    with open(filename,'r',newline='') as input_csv_file:
        reader = csv.DictReader(input_csv_file,delimiter=';')
        papers = [Paper.from_dict(p) for p in reader]
    input_csv_file.close()
    return papers


