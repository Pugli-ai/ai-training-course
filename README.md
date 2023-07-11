# Langchain in Django

## Hackathon Guid
*Obiettivo*: Creare un'app Django che permetta agli utenti di fare domande su articoli molto tecnici su ChatGPT e su varie tecniche di prompting.

Inizia dall'app Django già implementata durante questa lezione modificando la funzione `handle_message` in `django_langchain_app/chat_bot.py` per aggiungere la logica per gestire le domande sugli articoli.

Gli articoli si trovano nella cartella `documents/hackathon`.

## Configurazione ambiente di sviluppo

Requisiti:
- Python 3.8 (https://www.python.org/downloads/)
- Git (https://git-scm.com/downloads)
- Node and npm (https://nodejs.org/en/download/) or Docker with docker compose (https://docs.docker.com/get-docker/)

### 1. Clonare la repository

```bash
git clone https://github.com/Pugli-ai/ai-training-course.git
cd ai-training-course
```

### 2. Creare il file .env
- Rinominare il file `.env.example` in `.env`.

- Modificare il file `.env` con le proprie credenziali.

### 3. Creare un ambiente virtuale
- Creare un ambiente virtuale con il seguente comando:

```bash
python3 -m venv django_langchain_env
source django_langchain_env/bin/activate  # For Linux/Mac
.\django_langchain_env\Scripts\activate   # For Windows
```

### 4. Installare i requisiti
- Installare i requisiti con il seguente comando:

```bash
pip install -r requirements.txt
```