# my-digital-clone

# Project description

This project implements a personalized chatbot using a fine-tuned GPT-2 model with telegram messages and Streamlit for the user interface. 
The objective of this project is to create a digital clone of myself using the Telegram API to collect all the messages I've sent. By leveraging these messages, I fine-tuned a GPT-2 model to generate responses that emulate my communication style. This digital clone can be used for various applications, such as:

- Automated personal messaging: The chatbot can reply to messages in a way that sounds like me, which can be useful for managing large volumes of communication.
- Digital assistant: The chatbot can serve as a personal assistant, providing information and performing tasks in a manner that feels personal.
- Archiving conversations: The chatbot can recreate and respond in a style similar to past conversations, preserving the essence of my communication over time.

## Features

- Web-based chat interface
- Personalized responses based on a fine-tuned GPT-2 model
- Easy to deploy and use

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MrSimple07/my-digital-clone
```
2. Install the required packages:
```bash
pip install streamlit transformers torch
```

## Usage

Run the Streamlit app:
```bash
streamlit run appStreamlit.py
```

Then open your web browser and go to `http://localhost:8501`.

## Model

This chatbot uses a fine-tuned GPT-2 model. The model is loaded from the Hugging Face model hub: "MrSimple07/my-gpt2-model-for-clone".

# Repository Structure

Here is an overview of the files included in this repository:

data/: This directory contains the preprocessed Telegram messages used for fine-tuning the GPT-2 model.
telegramAPI/: This directory includes scripts and utilities for interacting with the Telegram API and extracting message data. And also the fine- tuning process which was done on Kaggle platform.
LICENSE: The license file for this project.
README.md: The readme file providing an overview and instructions for the project.
appStreamlit.py: The main Streamlit app file that creates the web interface and handles user interactions.
tg_getting_data.py: A script for collecting and preprocessing Telegram messages using the Telegram API.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache License.
