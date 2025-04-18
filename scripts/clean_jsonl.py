import json
import re

input_file = 'data/nfqa_open/input/nfqa_open_input.jsonl'
output_file = 'data/nfqa_open/input/nfqa_open_input_cleaned.jsonl'

def clean_question(question):
    # Find the position of the text to remove
    start_text = "You can refer to the following context for your answer:"
    if start_text in question:
        # Split by the start text and get the first part
        parts = question.split(start_text)
        return parts[0].strip()
    return question

# Process the file
with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
    for line in fin:
        # Parse JSON object
        data = json.loads(line.strip())
        
        # Clean the question field
        data['question'] = clean_question(data['question'])
        
        # Write the modified JSON object
        fout.write(json.dumps(data, ensure_ascii=False) + '\n')

print("Processing complete. Output written to:", output_file) 