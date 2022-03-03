import re

class Paper:
    def __init__(self,paper_id,title,authors,year,peer_reviewed,doi=None,filename=None):
        self.title = title.lstrip().rstrip()
        self.authors = authors.lstrip().rstrip()
        self.year = year
        self.doi = doi
        self.paper_id = paper_id
        self.filename = filename
        self.peer_reviewed = peer_reviewed
    

    @classmethod
    def from_dict(cls,d):
        print(bool(d['peer_reviewed']))
        return cls(d['id'],d['title'],d['authors'],d['year'],bool(d['peer_reviewed']),d['doi'],d['filename'])
    
    @classmethod
    def from_text(cls,paper_id_text,year,text):
        regex_id = r'\d{1,3}'
        regex_title = r'((“|"|“|”).*(”|"|“|”))'
        regex_peer = r'\*'

        # find title and authors

        match_title = re.split(regex_title,text)
        if match_title:
            authors = match_title[0]
            title=match_title[1][1:-1]
        if not match_title:
            title=None
            authors=None

        # find id
        paper_id = re.match(regex_id,paper_id_text).group(0)

        # find peer
        if re.search(regex_peer,paper_id_text):
            peer = True
        else:
            peer = False

#        print(paper_id,peer,year,authors)
        return cls(paper_id,title,authors,year,peer)

    def __str__(self):
        return f"id: {self.paper_id}, peer_reviewed: {self.peer_reviewed}, year: {self.year} \n\
                title: {self.title} \n\
                authors: {self.authors}\n"
    def __repr__(self):
        return self.__str__()
    def to_dict(self):
        d = {   'id':self.paper_id,
                'title': self.title,
                'authors':self.authors,
                'year':self.year,
                'doi':self.doi,
                'filename':self.filename,
                'peer_reviewed':self.peer_reviewed
            }
        return d

