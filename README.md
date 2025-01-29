# Browse Use

## Overview
Browse Use is an advanced task automation tool that enables seamless interaction with websites through an AI-driven agent. 

The AI Web Bot is built on **Gradio**, providing a user-friendly interface for interacting with the browser agent. Additionally, it integrates various **Large Language Models (LLMs)** for AI-powered assistance.

## Features
- **Expanded LLM Support**: Supports multiple LLMs, including:
  - Gemini
  - OpenAI
  - Azure OpenAI
  - Anthropic
  - DeepSeek
  - Ollama
- **Persistent Browser Sessions**: Keeps the browser window open for continuous AI tasks.
- **User-Friendly Web UI**: Easily configure and interact with the AI agent.

## Prerequisites
Ensure that you have the following installed before running the project:

- **Python 3.12** → [Download Python](https://www.python.org/downloads/release/python-3120/)
- **GUI Toolkit: Tkinter** (included with Python 3.12)

## Installation & Setup
Follow these steps to set up and run AI Web Bot:

### 1. Clone the Repository
```sh
 git clone https://github.com/gouravgujariya/AI_WEB_BOT.git
```

### 2. Navigate to the Project Directory
```sh
 cd navigate_to_project_directory
```

### 3. Run the Setup Script
```sh
 python setup.py
```
A GUI window will open.

### 4. Install Dependencies
Click on the **Install Dependencies** button in the GUI. This will:
- Install all required dependencies.
- Create a `.bat` file for launching the server.

### 5. Start the Server
Navigate to the project folder in **File Explorer** and double-click the generated `.bat` file. The server will start and open in your default browser.

## API Key Setup for LLM Providers
To use different LLMs, users must select the provider, specify the model, and generate an API key. Below are the steps to generate API keys:

### OpenAI
1. Visit [OpenAI API](https://platform.openai.com/signup/).
2. Sign in or create an account.
3. Navigate to **API Keys** under your profile.
4. Generate a new key and copy it.

### Gemini (Google AI)
1. Go to [Gemini API](https://aistudio.google.com/app/apikey).
2. Sign in with your Google account.
3. Generate an API key from the API console.

### DeepSeek
1. Visit [DeepSeek API](https://api-docs.deepseek.com/).
2. Register and create an API key from the developer settings.

### Anthropic (Claude)
1. Go to [Anthropic API](https://console.anthropic.com/login?returnTo=%2F%3F).
2. Create an account.
3. Generate and copy the API key.

### Ollama
1. Visit [Ollama API](https://ollama.com/).
2. Register and retrieve the API key.

### Azure OpenAI
1. Log in to [Azure AI Portal](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service/).
2. Navigate to **Cognitive Services** and create a new OpenAI resource.
3. Copy the API key from the Azure portal.

## Running the AI Agent
Once the server is running:
1. Open the Browse Use.
2. Select an **LLM provider** and enter the corresponding **API key**.
3. Input a **prompt** in the RunAgent section.
4. Execute and interact with the AI-powered web agent.


---

Enjoy using AI Web Bot to automate your browser tasks with AI assistance!

