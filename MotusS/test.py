from val_package import process_company_info
import json

result = process_company_info("input_file.json")

print(result)

with open("output_file.json", 'w') as json_file:
    json.dump(result, json_file)
    


    
