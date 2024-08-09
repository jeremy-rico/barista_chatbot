# Virtual Barista Chatbot

## Description
This project consists of a simple LLM based chatbot with adheres to a few rules and behaviors as designated by the assignment. The architecture is composed a simple front end in which a user can send and recieve messages to the chatbot. The backend filters messages, perofmring profanity filtering and some light preprocessing before sending the query via API call to an LLM. The goal of this project is to have the LLM act as a barista with access to a "menu" of drinks which it can deliver information on and make reccommendations. 

## Tech Stack
- Front end: HTML, CSS, JavaScript
- Back end: Python, Flask, scikit-learn
- Language Model: gpt-4o-mini

## To Run
Since this model uses an OpenAI model you will need to install the OpenAI client and obtain an OpenAI API Key. You can learn how to do that here: https://platform.openai.com/docs/quickstart

Once you have obtained a key you can run the full pipeline with the simple command:
```
docker compose -f docker-compose-dev.yaml up
```
