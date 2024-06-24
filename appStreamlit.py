import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

@st.cache_resource
def load_model():
    model = GPT2LMHeadModel.from_pretrained("MrSimple07/my-gpt2-model-for-clone")
    tokenizer = GPT2Tokenizer.from_pretrained("MrSimple07/my-gpt2-model-for-clone")
    return model, tokenizer

model, tokenizer = load_model()

def generate_response(prompt, max_length=100):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2)
    return tokenizer.decode(output[0], skip_special_tokens=True)

st.title("My Personalized Chatbot")

user_input = st.text_input("You:", "")
if st.button("Send"):
    if user_input:
        response = generate_response(user_input)
        st.text_area("Bot:", value=response, height=100, max_chars=None, key=None)
    else:
        st.warning("Please enter a message.")