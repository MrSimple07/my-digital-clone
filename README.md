# my-digital-clone

This project implements a personalized chatbot using a fine-tuned GPT-2 model with telegram messages and Streamlit for the user interface.

## Features

- Web-based chat interface
- Personalized responses based on a fine-tuned GPT-2 model
- Easy to deploy and use

## Installation

1. Clone this repository:
```bash
git clone [https://github.com/yourusername/personalized-chatbot.git](https://github.com/MrSimple07/my-digital-clone)
```
2. Install the required packages:
```bash
pip install streamlit transformers torch
```

## Usage

Run the Streamlit app:
```bash
streamlit run streamlit_app.py
```

Then open your web browser and go to `http://localhost:8501`.

## Files

- `streamlit_app.py`: The main application file containing the Streamlit interface and chatbot logic.
- `requirements.txt`: List of Python packages required for this project.

## Model

This chatbot uses a fine-tuned GPT-2 model. The model is loaded from the Hugging Face model hub: "MrSimple07/my-gpt2-model".

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache License.
