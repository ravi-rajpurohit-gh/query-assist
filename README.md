# QueryAssist - Thoughtful AI Customer Support Agent

**QueryAssist** is a simple AI-powered customer support agent designed to answer basic user questions about Thoughtful AI. It retrieves the most relevant hardcoded responses for user queries and provides clear answers based on predefined information about Thoughtful AI's services and automation agents.

## Features

- User inputs a question in the text field, and the agent retrieves the most relevant predefined answer.
- If the query doesn't exactly match any predefined question, the agent will provide a fallback response from a list of generic replies.
- User can input different queries in the same text field repeatedly.

## How It Works

1. The user enters a question about Thoughtful AI.
2. The AI agent matches the question with predefined responses stored in a hardcoded dataset.
3. If a match is found, the most relevant answer is displayed.
4. If no match is found, the agent responds with a fallback message.

## Technologies Used

- **Streamlit**: For creating the web-based user interface.
- **Python**: To handle the backend logic for processing user queries and matching them with predefined responses.
- **Natural Language Processing**: A simple tokenization and word matching algorithm is used to find the best possible match for user queries.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ravi-rajpurohit-gh/query-assist.git
   cd queryassist
   ```

2. Install the required dependencies:

   ```bash
   pip install streamlit
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter a question related to Thoughtful AI (e.g., "What does the eligibility verification agent (EVA) do?").
2. The agent will respond with the most relevant predefined answer.
3. If the agent doesn’t have an exact answer, it will provide a fallback response asking for clarification or offering help.

### Example Queries:

- "What does the claims processing agent (CAM) do?"
- "EVA"
- "How does the payment posting agent (PHIL) work?"
- "payment"
- "What are the benefits of Thoughtful AI?"

## Future Enhancements

- Add conversation-like feel for a more interactive user experience.
- Expand the dataset to include more questions and answers.
- Improve the matching algorithm for better response accuracy.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
