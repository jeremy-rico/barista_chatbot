# Virtual Barista Chatbot

## Description
This project consists of a simple LLM based chatbot with adheres to a few rules and behaviors as designated by the assignment. The architecture is composed a simple front end in which a user can send and recieve messages to the chatbot. The back end filters messages, performring profanity filtering and some light preprocessing before sending the query via API call to an LLM. The goal of this project is to have the LLM act as a barista with access to a "menu" of drinks which it can deliver information on and make reccommendations.

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
>Also note you will need to export the variable for it to be accessible to Docker
>```export OPENAI_APIKEY=your_api_key```

If you have to run docker using root privledges run this line:
```
sudo -E docker compose -f docker-compose-dev.yaml up
```

If you do not need root privledges to run docker than run this line:
```
docker compose -f docker-compose-dev.yaml up
```
