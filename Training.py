import spacy
import random
import csv

# Load a blank English model
nlp = spacy.blank("en")

# Define the training data
TRAIN_DATA = []

# Load data from CSV file
with open('employees.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Assuming the CSV has columns: ID, Name, Email
        employee_id = row['ID']
        name = row['Name']
        email = row['Email']
        # For simplicity, concatenating ID, Name, and Email
        text = f"{employee_id} {name} {email}"
        # Defining the entities - here we consider everything as "Employee"
        entities = [(0, len(employee_id), "EMPLOYEE_ID"),
                    (len(employee_id)+1, len(name)+len(employee_id)+1, "NAME"),
                    (len(name)+len(employee_id)+2, len(email)+len(name)+len(employee_id)+2, "EMAIL")]
        TRAIN_DATA.append((text, {"entities": entities}))

# Add the named entity recognizer to the pipeline if it doesn't exist
if "ner" not in nlp.pipe_names:
    ner = nlp.create_pipe("ner")
    nlp.add_pipe(ner, last=True)
else:
    ner = nlp.get_pipe("ner")

# Add labels to the NER
for _, annotations in TRAIN_DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# Disable other pipelines during training
pipe_exceptions = ["ner"]
other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

# Training the model
with nlp.disable_pipes(*other_pipes):  # Only train NER
    optimizer = nlp.begin_training()
    for itn in range(10):  # Adjust the number of iterations as needed
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            nlp.update([text], [annotations], drop=0.5, sgd=optimizer, losses=losses)
        print(losses)
