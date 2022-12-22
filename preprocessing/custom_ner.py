import spacy
import random

# Create a blank model
nlp = spacy.blank("en")

# Define the entities you want to recognize
entity_types = ["ORG", "PERSON"]

# Create the pipeline to recognize these entities
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
for entity_type in entity_types:
    ner.add_label(entity_type)

# Load your training data
train_data = [("Who is Shaka Khan?", [(7, 17, "PERSON")]), 
              ("I like London and Berlin.", [(7, 13, "LOC"), (18, 24, "LOC")])]

# Start the training
nlp.begin_training()

# Loop for 10 iterations
for itn in range(10):
    # Shuffle the training data
    random.shuffle(train_data)
    # Create batches and iterate over them
    for batch in spacy.util.minibatch(train_data, size=2):
        # Split the batch into texts and annotations
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        # Update the model
        nlp.update(texts, annotations)

# Save the model to disk
nlp.to_disk("model")

# Test the model
test_text = "Do you like Barack Obama?"
doc = nlp(test_text)
for ent in doc.ents:
    print(ent.text, ent.label_)