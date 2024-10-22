import json

def load_jsonl(file_path):
    """
    Load a .jsonl file and return a list of JSON objects.
    Each line in the file contains one JSON object.
    """
    papers = []
    with open(file_path, 'r') as file:
        for line in file:
            papers.append(json.loads(line.strip()))
    return papers

def update_readme_with_table(papers, readme_path="README.md"):
    """
    Updates the README.md file with a markdown table of papers.
    :param papers: List of paper objects (from the jsonl file).
    :param readme_path: Path to the README.md file.
    """
    table_header = "| Papers |\n| --- |\n"
    table_rows = ""
    
    for paper in papers:
        title = paper.get('title', 'No Title')
        title = bytes(title, "utf-8").decode("unicode_escape").encode("latin1").decode("utf-8")
        link = paper.get('link', '#')
        table_rows += f"| [{title}]({link}) |\n"
    
    # Update README.md file
    with open(readme_path, 'a') as readme_file:
        readme_file.write("\n## Papers\n\n")
        readme_file.write(table_header)
        readme_file.write(table_rows)

if __name__ == "__main__":
    # Path to your .jsonl file
    jsonl_file_path = 'data/papers.jsonl'
    
    # Load the papers from jsonl file
    papers = load_jsonl(jsonl_file_path)
    
    # Update the README.md file
    update_readme_with_table(papers)
