import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:1.7b"


def analyser_article(article):
    texte = article["resume_rss"]

    if not texte:
        return "Pas assez de contenu pour analyser cet article."

    prompt = f"""
Tu es un agent de veille technologique.

Article :
Titre : {article["titre"]}
Source : {article["source"]}
Contenu : {texte}

Donne :
1. Un résumé en français en 2 phrases maximum.
2. Une catégorie.
3. Un score d'intérêt sur 10.
"""

    reponse = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "think": False
        },
        timeout=120
    )

    reponse.raise_for_status()

    return reponse.json()["response"]