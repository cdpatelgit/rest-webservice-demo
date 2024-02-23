from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Sample data (employee ID and name pairs)
employee_data = [
    {"id": "001", "name": "John Doe"},
    {"id": "002", "name": "Jane Smith"},
    # Add more data as needed
]

# Preparing data for BERT
texts = [f"Employee ID: {data['id']} Employee Name: {data['name']}" for data in employee_data]
labels = [int(data['id']) for data in employee_data]  # Using employee ID as labels

# Load BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(employee_data))

# Tokenize input texts
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

# Convert labels to tensor
labels = torch.tensor(labels)

# Fine-tune BERT model
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
model.train()
optimizer.zero_grad()

outputs = model(**inputs, labels=labels)
loss = outputs.loss
loss.backward()
optimizer.step()

# Save the fine-tuned model
model.save_pretrained("fine_tuned_bert_employee_model")
