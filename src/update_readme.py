import json
import os
import logging

if not os.path.exists("./logs"):
    os.makedirs("./logs")
logging.basicConfig(
    force=True,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler("./logs/update_readme.log"),  # Logs to file
        logging.StreamHandler()  # Logs to console
    ]
)

def load_jsonl(file_path):
    """
    Load a .jsonl file and return a list of JSON objects.
    Each line in the file contains one JSON object.
    """
    papers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                papers.append(json.loads(line.strip()))
    except FileNotFoundError:
        logging.error(f"Error: The file '{file_path}' was not found. Maybe there is no paper today.")
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return papers

def update_readme_with_table(papers, readme_path="README.md"):
    """
    Updates the README.md file with a markdown table of papers.
    Deletes previous content under ## Papers before appending new content.
    :param papers: List of paper objects (from the jsonl file).
    :param readme_path: Path to the README.md file.
    """
    table_header = "| Topic | Branch | Papers |\n| --- | --- | --- |\n"
    table_rows = ""
    
    for paper in papers:
        logging.info(json.dumps(paper, indent=4))
        title = paper.get('title', 'No Title')
        title = bytes(title, "utf-8").decode("unicode_escape").encode("latin1").decode("utf-8")
        link = paper.get('link', '#')
        
        first_labels = paper.get('first_label', [])
        second_labels = paper.get('second_label', [])
        
        # Join labels as comma-separated strings
        first_labels_str = ', '.join(first_labels) if first_labels else ""
        second_labels_str = ', '.join(second_labels) if second_labels else ""
        
        table_rows += f"| {first_labels_str} | {second_labels_str} | [{title}]({link}) |\n"
    
    # Read the existing content of the README.md file
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as readme_file:
            lines = readme_file.readlines()
        
        # Find the start and end of the ## Papers section
        new_lines = []
        in_papers_section = False
        for line in lines:
            if line.startswith("## Papers"):
                in_papers_section = True
                continue  # Skip the previous content
            
            if in_papers_section and line.strip() == "":
                continue  # Skip empty lines under the Papers section
            
            if in_papers_section and not line.startswith("|"):
                in_papers_section = False  # Exit the papers section on non-table lines
            
            if not in_papers_section:
                new_lines.append(line)

        # Write the updated README.md file with the new papers section
        with open(readme_path, 'w') as readme_file:
            readme_file.writelines(new_lines)
            readme_file.write("## Papers\n\n")
            readme_file.write(table_header)
            readme_file.write(table_rows)
    else:
        # If README.md does not exist, create it and write the content
        with open(readme_path, 'w') as readme_file:
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
