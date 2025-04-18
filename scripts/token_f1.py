import numpy as np
from collections import Counter
import re

def tokenize_text(text):
    """Tokenize text into words, removing punctuation and converting to lowercase."""
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())
    # Split into words
    return text.split()

def compute_precision(pred_tokens, gt_tokens):
    """Calculate precision between predicted and ground truth tokens."""
    label_counter = Counter(gt_tokens)
    predict_counter = Counter(pred_tokens)
    common = label_counter & predict_counter
    true_positive = sum(common.values())

    if len(pred_tokens) > 0:
        return true_positive / len(pred_tokens)
    else:
        return 0.0

def compute_recall(pred_tokens, gt_tokens):
    """Calculate recall between predicted and ground truth tokens."""
    label_counter = Counter(gt_tokens)
    predict_counter = Counter(pred_tokens)
    common = label_counter & predict_counter
    true_positive = sum(common.values())

    if len(gt_tokens) > 0:
        return true_positive / len(gt_tokens)
    else:
        return 0.0

def compute_f1(pred_tokens, gt_tokens):
    """Calculate F1 score between predicted and ground truth tokens."""
    precision = compute_precision(pred_tokens, gt_tokens)
    recall = compute_recall(pred_tokens, gt_tokens)
    
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)

def calculate_token_f1(predictions, labels):
    """Calculate token-level F1 scores for a list of predictions and labels."""
    f1_scores = []
    
    for pred, label in zip(predictions, labels):
        pred_tokens = tokenize_text(pred)
        label_tokens = tokenize_text(label)
        f1 = compute_f1(pred_tokens, label_tokens)
        f1_scores.append(f1)
    
    return np.mean(f1_scores)

if __name__ == "__main__":
    # Example usage
    predictions = ["The quick brown fox", "jumps over the lazy dog"]
    labels = ["The quick brown fox", "jumps over the lazy dog"]
    
    f1_score = calculate_token_f1(predictions, labels)
    print(f"Token-level F1 score: {f1_score:.4f}") 