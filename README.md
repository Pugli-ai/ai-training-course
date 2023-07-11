# Langchain in Django

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