# chatbot_logic.py

import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Common symptoms and advice
SYMPTOM_KEYWORDS = {
    "fever": "You might have a viral infection. Please rest and stay hydrated.",
    "cough": "It could be a cold, flu, or even COVID-19.",
    "headache": "It may be due to stress or dehydration.",
    "chest pain": "Chest pain can be serious. Please consult a doctor immediately.",
    "fatigue": "Take rest. Fatigue can result from overwork or illness.",
    "nausea": "Try light meals. May be stomach-related.",
    "sore throat": "Could be a throat infection. Warm liquids help.",
    "loss of taste": "May indicate a viral infection like COVID-19."
}

# Logic to generate chatbot reply
def get_response(user_input):
    user_input = user_input.lower()
    doc = nlp(user_input)
    responses = []

    for symptom, advice in SYMPTOM_KEYWORDS.items():
        if symptom in user_input:
            responses.append(f"<strong>{symptom.title()}:</strong> {advice}")

    if responses:
        return "<br>".join(responses)
    else:
        return "Sorry, I couldn't identify known symptoms. Please describe more."
