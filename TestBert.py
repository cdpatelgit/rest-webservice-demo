import torch
from transformers import BertTokenizer, BertModel
from torch.utils.data import Dataset, DataLoader

# Sample dataset
class EmployeeDataset(Dataset):
    def __init__(self, ids, names, tokenizer, max_length=64):
        self.ids = ids
        self.names = names
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.ids)

    def __getitem__(self, idx):
        id_str = str(self.ids[idx])
        name = str(self.names[idx])
        inputs = self.tokenizer.encode_plus(
            id_str,
            name,
            add_special_tokens=True,
            max_length=self.max_length,
            padding='max_length',
            truncation=True
        )
        return {
            'input_ids': torch.tensor(inputs['input_ids'], dtype=torch.long),
            'attention_mask': torch.tensor(inputs['attention_mask'], dtype=torch.long)
        }

# Example data
employee_ids = [1, 2, 3, 4]
employee_names = ["John Doe", "Jane Smith", "Bob Johnson", "Alice Williams"]

# Initialize BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Create dataset and dataloader
dataset = EmployeeDataset(employee_ids, employee_names, tokenizer)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Dummy training loop (replace with your actual training loop)
for batch in dataloader:
    input_ids = batch['input_ids']
    attention_mask = batch['attention_mask']

    # Forward pass through the model
    outputs = model(input_ids, attention_mask=attention_mask)
    # Your training code goes here
