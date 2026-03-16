#CodeAlpha AI Internship Projects

This repository contains the tasks completed as part of my **AI Internship**.
Each task demonstrates a different application of Artificial Intelligence and Python programming.



# Task 1: Language Translation Tool

## Description

The Language Translation Tool allows users to translate text from one language to another using a simple user interface. The application sends user input to a translation API and displays the translated output.

## Features

* User-friendly interface
* Select source and target languages
* Real-time text translation
* Optional text-to-speech functionality for translated text

## Technologies Used

* Python
* Streamlit
* Deep Translator API
* gTTS (Google Text-to-Speech)

## How to Run

Navigate to the folder and run:

py -m streamlit run app.py


# Task 2: FAQ Chatbot

## Description

The FAQ Chatbot answers user questions based on a predefined FAQ dataset. It uses Natural Language Processing techniques to match the user's query with the most similar question in the dataset.

## Features

* NLP-based text preprocessing
* TF-IDF vectorization
* Cosine similarity matching
* Similarity threshold to avoid incorrect responses
* Simple interactive interface

## Technologies Used

* Python
* Streamlit
* scikit-learn
* Natural Language Processing (NLP)

## How to Run

py -m streamlit run app.py


# Task 3: AI Music Generator

## Description

The AI Music Generator creates new musical sequences based on patterns learned from a dataset of MIDI files. The program extracts musical notes from the dataset and generates a new sequence that is saved as a MIDI file.

## Features

* MIDI dataset processing
* Musical note extraction
* Pattern-based music generation
* Automatic creation of a new MIDI file

## Technologies Used

* Python
* music21 library
* MIDI dataset

## How to Run


py music_generator.py


The generated music will be saved as:

generated_music.mid


# Project Structure

AI_INTERNSHIP
│
├── Task1-LanguageTranslator
│   └── app.py
│
├── Task2-FAQ-Chatbot
│   └── app.py
│
└── Task3-MusicGenerator
    ├── midi_dataset
    ├── music_generator.py
    └── generated_music.mid


# Author

Intern: Poojitha
AI Internship Project
