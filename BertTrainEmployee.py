import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Sample input data
employee_names = ["John Doe", "Jane Smith", "Alice Johnson"]
employee_ids = ["001", "002", "003"]

# Tokenize input data
inputs = tokenizer(employee_names, padding=True, truncation=True, return_tensors="pt")

# Make predictions
with torch.no_grad():
    outputs = model(**inputs)

# Extract predicted probabilities
predictions = torch.softmax(outputs.logits, dim=1)

# Decode predictions
predicted_labels = [employee_ids[p.argmax().item()] for p in predictions]

# Output predictions
for name, employee_id in zip(employee_names, predicted_labels):
    print(f"Employee Name: {name}, Predicted Employee ID: {employee_id}")
