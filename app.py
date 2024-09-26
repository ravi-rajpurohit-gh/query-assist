# import libraries
import streamlit as st
import re
from collections import Counter
import random

# Predefined dataset of questions and answers
qa_data = [
    {
        "question": "What does the eligibility verification agent (EVA) do?",
        "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    },
    {
        "question": "What does the claims processing agent (CAM) do?",
        "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    },
    {
        "question": "How does the payment posting agent (PHIL) work?",
        "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
    },
    {
        "question": "Tell me about Thoughtful AI's Agents.",
        "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
    },
    {
        "question": "What are the benefits of using Thoughtful AI's agents?",
        "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
    }
]

# List of fallback responses
fallback_responses = [
    "I'm sorry, I don't have an answer to that. Can you please clarify your question?",
    "Hmm, I couldn't find the exact answer. Could you try asking in a different way?",
    "I'm not sure about that. Can you provide more details?",
    "I don't have that information right now, but I'm here to help with anything else!"
]

# Tokenizer: function to convert a sentence into a list of words
def tokenize(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\W+', ' ', text)  # Remove non-word characters
    return text.split()

# Find the best matching question based on token similarity
def get_best_match(user_query):
    user_tokens = Counter(tokenize(user_query))
    max_score = 0
    best_answer = None
    
    for qa in qa_data:
        question_tokens = Counter(tokenize(qa["question"]))
        # Calculate similarity score (number of matching tokens)
        match_score = sum((user_tokens & question_tokens).values())
        
        if match_score > max_score:
            max_score = match_score
            best_answer = qa["answer"]
    
    if best_answer:
        return best_answer
    else:
        return random.choice(fallback_responses)


# Lets create a streamlit UI
def main():
    st.title("Thoughtful AI - Customer Support Agent")
    
    # Input from the user
    user_input = st.text_input("Ask me a question about Thoughtful AI:")

    if user_input:
        # Get the response
        answer = get_best_match(user_input)
        
        # Display the response
        st.write(f"**AI Agent:** {answer}")

if __name__ == "__main__":
    main()
