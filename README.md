# Virtual Barista Chatbot

## Description
This project consists of a full stack application for a LLM based barista chatbot. The front end includes a simple UI in which a user can input a text message and interact with the chatbot. The back end filters profanity and sends an API request to a text completion model. The model then provides a text response.

The chat model adheres to a few rules and behavior requirements as described in the assignment document. It's main goal is to provide detailed and professional information on a list of specific coffee drinks from a menu.

## Tech Stack
- Front end: HTML, CSS, JavaScript
- Back end: Python, Flask, scikit-learn 
- Language Model: gpt-4o-mini

## To Run
To run this application you will need two things:
1. Docker
>You can find Docker installation instructions here: https://docs.docker.com/engine/install/
2. An OPENAI_API_KEY environmental variable
>You will need to obtain an OpenAI API key and set it in your local shell environment. You can learn how to do that here: https://platform.openai.com/docs/quickstart

>Also note you will need to export the variable for it to be accessible to Docker ```export OPENAI_API_KEY=your_api_key```

If you have to run docker using root privledges, run this line:
```
sudo -E docker compose -f docker-compose-dev.yaml up
```

If you do not need root privledges to run docker, run this line:
```
docker compose -f docker-compose-dev.yaml up
```
