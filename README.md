# Mental Health Companion Agent

A supportive AI-powered mental health companion built with Streamlit, LangChain, and OpenAI. This application provides an empathetic chat interface where users can share their feelings, store personal reflections, and retrieve supportive notes to aid in emotional well-being.

## Features

- **Empathetic Chat Interface**: Interactive conversation with an AI agent designed to provide supportive, non-judgmental responses
- **Personal Reflection Storage**: Store thoughts, feelings, and reflections in a vector database for future reference
- **Supportive Note Retrieval**: Retrieve past reflections and supportive insights based on current conversations
- **Vector Database Integration**: Uses ChromaDB for efficient storage and retrieval of personal data
- **Streamlit Web App**: User-friendly web interface for easy access

## Prerequisites

- Python 3.9 or higher
- OpenAI API key (sign up at [OpenAI](https://platform.openai.com/))

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd AI-Agent-using-LangChain-OpenAI-API-main
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Access the application**:
   Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`)

3. **Start chatting**:
   - Share how you're feeling in the chat input
   - The agent will respond empathetically and may suggest storing reflections or retrieving supportive notes
   - Use the agent's tools to store personal insights or retrieve past reflections

## Configuration

- **Environment Variables**:
  - `OPENAI_API_KEY`: Your OpenAI API key (required)

- **Vector Database**:
  - The app automatically creates a `chroma_db` directory for storing vector embeddings
  - No additional configuration needed for the database

## Project Structure

```
.
├── app.py                 # Main Streamlit application
├── test.py                # CLI testing script for the agent
├── requirements.txt       # Python dependencies
├── config.yaml           # Authentication configuration (legacy)
├── TODO.md               # Project task list
├── chroma_db/            # Vector database directory (auto-generated)
├── .env                  # Environment variables (create this file)
└── README.md             # This file
```

## How It Works

The Mental Health Companion Agent uses:

- **LangChain & LangGraph**: For orchestrating the AI agent and tool interactions
- **OpenAI GPT-4o-mini**: As the underlying language model for empathetic responses
- **ChromaDB**: Vector database for storing and retrieving personal reflections
- **Streamlit**: Web framework for the user interface

The agent employs a ReAct (Reasoning + Acting) pattern, allowing it to:
1. Understand user input
2. Decide whether to respond directly or use tools
3. Store reflections or retrieve supportive notes as appropriate
4. Provide compassionate, helpful responses

## Testing

Run the CLI test version:
```bash
python test.py
```

This allows you to interact with the agent directly in the terminal for testing purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This application is not a substitute for professional mental health care. If you're experiencing mental health challenges, please consult with qualified healthcare professionals.
