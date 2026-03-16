import streamlit as st
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download tokenizer (only first time)
nltk.download('punkt')

# -------------------------------
# FAQ DATA
# -------------------------------

faq_data = {
    "What is AI?": "AI stands for Artificial Intelligence, which enables machines to mimic human intelligence.",
    "What is machine learning?": "Machine learning is a subset of AI that allows systems to learn from data.",
    "What is deep learning?": "Deep learning is a type of machine learning using neural networks.",
    "What is Python used for?": "Python is used for web development, AI, data science, and automation.",
    "What is Streamlit?": "Streamlit is a Python library used to build interactive web applications."
}

questions = list(faq_data.keys())
answers = list(faq_data.values())

# -------------------------------
# PREPROCESSING FUNCTION
# -------------------------------

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

processed_questions = [preprocess(q) for q in questions]

# -------------------------------
# VECTORIZATION
# -------------------------------

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)

# -------------------------------
# STREAMLIT UI
# -------------------------------

st.title("🤖 FAQ Chatbot")
st.write("Ask any question related to the given FAQs.")

user_input = st.text_input("Enter your question:")

if user_input:
    processed_input = preprocess(user_input)
    user_vector = vectorizer.transform([processed_input])

    similarity = cosine_similarity(user_vector, faq_vectors)
    best_match_index = similarity.argmax()

    # Similarity threshold check
    if similarity[0][best_match_index] < 0.3:
        st.warning("❗ Sorry, I don't understand your question.")
    else:
        st.success("💬 Answer:")
        st.write(answers[best_match_index])