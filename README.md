# Membrane Evaluation Framework

A comprehensive framework for evaluating language models on membrane-related tasks using various prompting strategies.

## Overview

This project provides a flexible framework for evaluating language models on membrane-related tasks using different prompting approaches, including:
- Zero-shot prompting
- Zero-shot Chain-of-Thought (CoT)
- Few-shot prompting

The framework supports both text-based and multimodal (text + image) inputs, making it suitable for a wide range of membrane-related evaluation tasks.

## Project Structure

```
.
├── config/              # Configuration files
│   ├── prompt_templates.py  # Prompt templates for different strategies
│   ├── dataset_info.json   # Dataset configuration
│   └── model_info.json     # Model configuration
├── data/               # Input data directory
├── outputs/           # Output directory for results
├── scripts/           # Utility scripts
├── source_data/       # Source data files
├── main.py           # Main evaluation script
└── requirements.txt   # Project dependencies
```

## Dependencies

The project requires the following Python packages:
- nltk==3.9.1
- openai==1.65.1
- numpy>=1.21.0
- pandas>=1.3.0
- tqdm>=4.62.0
- python-dotenv>=0.19.0
- requests>=2.26.0
- openrouter==0.1.1

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables in a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key
   OPENROUTER_API_KEY=your_api_key
   ```

## Usage

The main evaluation script can be run with various command-line arguments:

```bash
python main.py --task <task_name> --model <model_name> --prompting_type <type>
```

Available prompting types:
- `zero_shot_ao`: Zero-shot answer-only
- `zero_shot_cot`: Zero-shot Chain-of-Thought
- `few_shot`: Few-shot prompting

## Configuration

The framework is highly configurable through:
- `config/prompt_templates.py`: Define custom prompt templates
- `config/dataset_info.json`: Configure dataset-specific settings
- `config/model_info.json`: Configure model-specific parameters

## Output

Results are saved in the `outputs/` directory, including:
- Model predictions
- Evaluation metrics
- Detailed logs

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license information here]