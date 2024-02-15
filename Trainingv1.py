import spacy
import random
import csv

# Load a blank English model
nlp = spacy.blank("en")

# Define a function to train the model
def train_model(train_data):
    # Create a new pipeline component for named entity recognition
    ner = nlp.create_pipe("ner")
    nlp.add_pipe(ner, last=True)

    # Define labels for named entity recognition
    ner.add_label("EMPLOYEE_ID")
    ner.add_label("NAME")
    ner.add_label("EMAIL_ADDRESS")

    # Disable other pipeline components for training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):
        # Initialize optimizer
        optimizer = nlp.begin_training()

        # Iterate through training data
        for itn in range(10):
            random.shuffle(train_data)
            losses = {}
            # Batch the examples and iterate over them
            for batch in spacy.util.minibatch(train_data, size=2):
                texts = [text for text, entities in batch]
                annotations = [entities for text, entities in batch]
                # Update the model with iterating examples
                nlp.update(texts, annotations, drop=0.5, losses=losses)
            print("Losses", losses)

# Load the CSV file
def load_csv(csv_file):
    data = []
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            text = row[1]  # Assuming the employee's name is in the second column
            entities = {"entities": [(0, len(row[0]), "EMPLOYEE_ID"), 
                                     (len(row[0]) + 1, len(row[0]) + len(row[1]), "NAME"), 
                                     (len(row[0]) + len(row[1]) + 2, len(row[0]) + len(row[1]) + len(row[2]), "EMAIL_ADDRESS")]}
            data.append((text, entities))
    return data

# Train the model
csv_file = "employees.csv"
train_data = load_csv(csv_file)
train_model(train_data)

# Save the model
nlp.to_disk("employee_ner_model")

# Testing the model
test_text = "John Doe's employee ID is 12345 and his email is john.doe@example.com"
nlp_loaded = spacy.load("employee_ner_model")
doc = nlp_loaded(test_text)
for ent in doc.ents:
    print(ent.text, ent.label_)
