import json
import os

def transform_json_data(input_file, output_file):
    # Read the input JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Create new data structure
    new_data = []
    with open(output_file, 'w', encoding='utf-8') as f:

    # Process each item in the original data
        for i, item in enumerate(data, 1):
            # Create a new ID with the format test-00001, test-00002, etc.
            new_id = f"test-{i:05d}"
            
            # Combine query and context for the question
            question = item.get("query", "") + "\nYou can refer to the following context for your answer:\n" + item.get("context", "")
            
            # Get the expected output as the label
            label = item.get("expected_output", "")
            
            # Create new item with the required structure
            new_item = {
                "id": new_id,
                "question": question,
                "label": label
            }
            
            # Add the new item to our new data list
            f.write(json.dumps(new_item, ensure_ascii=False) + '\n')
    
    # Write the transformed data to the output file
    # with open(output_file, 'w', encoding='utf-8') as f:
    #     json.dump(new_data, f, indent=2, ensure_ascii=False)
    
    # print(f"Transformation complete. Output saved to {output_file}")

if __name__ == "__main__":
    input_file = "membrane_questions.json"
    output_file = "nfqa_open.jsonl"
    
    transform_json_data(input_file, output_file)