from html.parser import HTMLParser
from .keywords import FIRST_LEVEL_KEYWORDS, SECOND_LEVEL_KEYWORDS, AUTHORS

class Paper:
    """
    Represents a research paper extracted from an email.
    """
    def __init__(self, ref):
        self.title = ''
        self.first_labels = []
        self.second_labels = []
        self.data = ''
        self.link = ''
        self.idx = ''
        self.ref = [ref]  # Email subjects (reference) where the paper was found
        self.author = []
        
    def __str__(self):
        return f"Title: {self.title}\n" \
               f"Data: {self.data}\n" \
               f"Link: {self.link}\n" \
               f"Author: {', '.join(self.author)}\n" \
               f"References: {', '.join(self.ref)}\n"
               
    def add_label(self, label: str):
        """
        Adds the label of the paper after processing.
        """
        if label in FIRST_LEVEL_KEYWORDS and label not in self.first_labels:
            self.first_labels.append(label)
        
        if label in SECOND_LEVEL_KEYWORDS  and label not in self.second_labels:
            self.second_labels.append(label)
               
    def _generate_label(self):
        title = self.title.lower()
            # Check first-level keywords
        for first_label, patterns in FIRST_LEVEL_KEYWORDS.items():
            for pattern in patterns:
                if pattern.lower() in title:
                    self.add_label(first_label)
        
        # Check second-level keywords
        for second_label, patterns in SECOND_LEVEL_KEYWORDS.items():
            for pattern in patterns:
                if pattern.lower() in title:
                    self.add_label(second_label)
    
    def add_title(self, data:str):
        """
        Adds the title of the paper after cleaning.
        """
        def clean_title(st):
            """
            Cleans and formats the title text by removing unwanted characters.
            """
            if st[0] == '[':
                st = st[st.find(']') + 1:]
            st = st.replace('\\xe2\\x80\\x8f', '')
            return st.strip()

        self.title += clean_title(data) + " "
        self.idx = self.title.strip().upper()
        self._generate_label()
        
    def add_data(self, data:str):
        """
        Adds metadata or content of the paper.
        """
        self.data += data + "\n"
        
    def add_ref(self, ref: str):
        """
        Adds a reference to the paper.
        """
        self.ref.append(ref)
        
    def to_dict(self):
        """
        Converts the paper object to a dictionary format for JSONL export.
        """
        return {
            "title": self.title.strip(),
            "first_label": self.first_labels,
            "second_label": self.second_labels,
            "data": self.data.strip(),
            "link": self.link,
            "author": self.author,
            "ref": self.ref
        }
    
    def add_author(self, author: str):
        """
        Adds an author to the paper.
        """
        self.author.append(author)

    def from_ref_to_author(self):
        """
        Converts a reference to an author name.
        """
        for ref in self.ref:
            for author in AUTHORS:
                if author.lower() in ref.lower():
                    self.add_author(author)
                    break

class PapersHTMLParser(HTMLParser):
    """
    Parses the HTML content of an email to extract paper details.
    """
    def __init__(self, author_ref: str):
        super().__init__()
        self.is_title = False
        self.papers: list[Paper] = []
        self.ref = author_ref
        
    def handle_starttag(self, tag:str, attrs:list[str]):
        """
        Handles the start of an HTML tag and checks for paper titles and links.
        """
        if tag == 'h3':  # h3 tag is assumed to indicate a new paper
            self.papers.append(Paper(self.ref))
            self.is_title = True
        if tag == 'a' and self.is_title:
            for attr in attrs:
                if attr[0].lower() == 'href':
                    self.papers[-1].link = attr[1]  # Set paper's link

    def handle_endtag(self, tag):
        """
        Handles the end of an HTML tag.
        """
        if tag == 'h3':
            self.is_title = False  # End of title section

    def handle_data(self, data: str):
        """
        Handles the raw text data within HTML tags.
        """
        if len(self.papers) > 0:
            if self.is_title:
                self.papers[-1].add_title(data)  # Add title
            else:
                self.papers[-1].add_data(data)  # Add other content

class PaperAggregator:
    """
    Aggregates and manages papers, ensuring no duplicates.
    """
    def __init__(self):
        self.paper_list = []
        
    def add(self, paper: Paper):
        """
        Adds a paper to the list, combining references for duplicates.
        """
        idx = self.exists_by_title(paper.title)
        
        if idx >= 0:
            self.paper_list[idx].add_ref(paper.ref[0])
        else:
            if len(paper.title) != 0:
                paper.from_ref_to_author()
                self.paper_list.append(paper)
            
    def remove(self, paper: Paper):
        """
        Removes a paper from the list.
        """
        try:
            idx = self.paper_list.index(paper)
            self.paper_list.pop(idx)
        except ValueError:
            pass

    def exists_by_title(self, title: str) -> bool:
        """
        Checks if a paper with the given title exists in the paper_list.

        Args:
            title (str): The title of the paper to search for.

        Returns:
            bool: True if a paper with the title exists, False otherwise.
        """
        index = 0
        for paper in self.paper_list:
            if paper.title == title:
                return index
            index += 1
        return -1
