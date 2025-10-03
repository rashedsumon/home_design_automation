import json

def floorplan_to_json(texts, output_path):
    """
    Convert extracted text from floorplan into structured JSON.
    Currently stores each page as an item in JSON.
    """
    data = []
    for idx, page_text in enumerate(texts):
        page_data = {
            "page_number": idx + 1,
            "content": page_text.split("\n")  # split lines as example
        }
        data.append(page_data)
    
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)
    
    return output_path
