import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, AdamW
from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pad_sequence

# Define your dataset
dataset = [
    {"prompt": "I have a headache", "response": "Consider taking some rest and drink plenty of water."},
    {"prompt": "I feel tired all the time", "response": "Ensure you are getting enough sleep and maintain a balanced diet."}
]

# Tokenize the dataset
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.add_special_tokens({'pad_token': '[PAD]'})

tokenized_datasets = tokenizer([item['prompt'] for item in dataset], truncation=True, padding=True, return_tensors='pt', max_length=128)

# Define a custom dataset class
class CustomDataset(Dataset):
    def __init__(self, tokenized_dataset, responses):
        self.tokenized_dataset = tokenized_dataset
        self.responses = responses

    def __len__(self):
        return len(self.tokenized_dataset["input_ids"])

    def __getitem__(self, idx):
        return {
            'input_ids': self.tokenized_dataset['input_ids'][idx],
            'attention_mask': self.tokenized_dataset['attention_mask'][idx],
            'labels': self.tokenized_dataset['input_ids'][idx],
            'response': torch.tensor(tokenizer.encode(self.responses[idx], truncation=True, padding=True))
        }

# Create DataLoader with collate function
def collate_fn(batch):
    input_ids = torch.stack([item['input_ids'].squeeze() for item in batch])
    attention_mask = torch.stack([item['attention_mask'].squeeze() for item in batch])
    labels = torch.stack([item['labels'].squeeze() for item in batch])

    # Pad the 'response' sequences to the same length
    responses_padded = pad_sequence([item['response'] for item in batch], batch_first=True, padding_value=tokenizer.pad_token_id)

    return {
        'input_ids': input_ids,
        'attention_mask': attention_mask,
        'labels': labels,
        'response': responses_padded
    }

# Create DataLoader
custom_dataset = CustomDataset(tokenized_datasets, [item['response'] for item in dataset])
dataloader = DataLoader(custom_dataset, batch_size=2, shuffle=True, collate_fn=collate_fn)

# Load pre-trained GPT-2 model
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Fine-tune the model
optimizer = AdamW(model.parameters(), lr=5e-5)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Fine-tuning loop
num_epochs = 3
for epoch in range(num_epochs):
    for batch in dataloader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        response = batch['response'].to(device)

        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

# Save the fine-tuned model
model.save_pretrained('./fine_tuned_model')

# Now, you can use the fine-tuned model to generate responses based on user input
fine_tuned_model = GPT2LMHeadModel.from_pretrained('./fine_tuned_model')
fine_tuned_model.to(device)
fine_tuned_model.eval()

def generate_response(user_input):
    input_ids = tokenizer.encode(user_input, return_tensors='pt').to(device)
    output_ids = fine_tuned_model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2)
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return response

# Example usage
user_input = "I have a headache"
response = generate_response(user_input)
print(response)
