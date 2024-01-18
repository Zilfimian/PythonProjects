import json

def process_company_info(input_file_path):
    # Read input JSON file
    with open(input_file_path, 'r') as input_file:
        data = json.load(input_file)

    # Extract company name and size
    company_name = data.get('company_name', 'Unknown Company')
    company_size = data.get('company_size', 'Unknown Size')

    # Create output string
    output_string = f"The company name is {company_name} and its size is {company_size}."

    return output_string
