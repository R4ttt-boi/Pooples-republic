import os
import re
import json

# Directory containing the HTML files
data_dir = "/home/admin/repos/Pooples-republic/src/data/raw_html"

# Output file for the extracted data
output_file = "/home/admin/repos/Pooples-republic/src/data/effects_raw/project_info.json"

def extract_project_info(html_content):
    # Initialize a list to store project information
    projects = []
    
    # Regular expression pattern to find project sections
    project_pattern = re.compile(r'<div class="title-row">.*?<div class="title ">(.*?)</div>.*?<div class="desc mb-1">(.*?)</div>.*?<ul class="finances mt-1">(.*?)</ul>.*?<ul class="effects mt-1">(.*?)</ul>', re.DOTALL)
    
    # Find all matches in the HTML content
    matches = project_pattern.finditer(html_content)
    
    # Process each match
    for match in matches:
        name = match.group(1).strip()
        description = match.group(2).strip()
        finance_html = match.group(3)
        effects_html = match.group(4)
        
        # Extract finance information
        finance_items = re.findall(r'<li>(.*?)</li>', finance_html)
        finance = [item.strip() for item in finance_items]
        
        # Extract effect information
        effect_items = re.findall(r'<li>(.*?)</li>', effects_html)
        effects = [item.strip() for item in effect_items]
        
        # Add the project information to the list
        projects.append({
            "name": name,
            "description": description,
            "finance": finance,
            "effects": effects
        })
    
    return projects

def process_html_files():
    # Initialize a list to store all project information
    all_projects = []
    
    # Iterate over each HTML file in the directory
    for filename in os.listdir(data_dir):
        if filename.endswith(".html"):
            file_path = os.path.join(data_dir, filename)
            
            # Read the HTML file
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
                
                # Extract project information from the HTML content
                projects = extract_project_info(html_content)
                
                # Add the projects to the list
                all_projects.extend(projects)
    
    # Write the extracted data to a JSON file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(all_projects, file, ensure_ascii=False, indent=2)
    
    print(f"Project information extracted and saved to {output_file}")

# Run the function to process the HTML files
if __name__ == "__main__":
    process_html_files()