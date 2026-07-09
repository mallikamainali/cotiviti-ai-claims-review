import json

with open("data/clinical_guidelines.json", "r", encoding="utf-8") as f:
    guidelines = json.load(f)

#Retrieve the clinical guideline that matches the diagnosis code

def retrieve_guideline(diagnosis_code):
    for guideline in guidelines:
        if guideline["diagnosis"] == diagnosis_code:
            return guideline

    return None
