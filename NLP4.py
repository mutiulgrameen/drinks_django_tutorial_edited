# Define included_entities
include_entities = ['DATE', 'ORG', 'PERSON']
import spacy
nlp = spacy.load("en_core_web_md")

# Define extract_entities()
def extract_entities(message):
    # Create a dict to hold the entities
    ents = dict.fromkeys(include_entities)
    # Create a spacy document
    doc = nlp(message)
    for ent in doc.ents:
        if ent.label_ in include_entities:
            # Save interesting entities
            ents[ent.label_] = ent.text
    return ents

#print(extract_entities('Joseph called Mary who have worked at Google since 2010'))
#print(extract_entities('Iqbal who graduated from MIT in 1999'))
print(extract_entities('Uruguay graduated from Islamic University Technology in 2022 and is currently working at Grameen'))