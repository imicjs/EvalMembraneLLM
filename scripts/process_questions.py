import json

def process_line(line):
    # Parse the JSON line
    data = json.loads(line)
    
    # Get the original content
    original_question = data['question']
    explanation = data.get('explanation', '')
    consideration = data.get('consideration', '')
    
    # Construct the new question
    new_question = original_question
    if explanation:
        new_question += f"\nYou can refer to the following content: {explanation}"
    if consideration:
        new_question += f"\n{consideration}"
    
    # Update the question field
    data['question'] = new_question
    
    # Remove the explanation and consideration fields
    if 'explanation' in data:
        del data['explanation']
    if 'consideration' in data:
        del data['consideration']
    
    return json.dumps(data, ensure_ascii=False)

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            processed_line = process_line(line.strip())
            f_out.write(processed_line + '\n')

if __name__ == "__main__":
    input_file = "data/nfqa_rag/input/nfqa_rag_input.jsonl"
    output_file = "data/nfqa_rag/input/nfqa_rag_input_processed.jsonl"
    process_file(input_file, output_file) 