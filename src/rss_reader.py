import feedparser
import yaml


def charger_sources():
    with open("config/feeds.yaml", "r", encoding="utf-8") as fichier:
        config = yaml.safe_load(fichier)

    return config["feeds"]


def recuperer_articles(source):
    flux = feedparser.parse(source["url"])

    articles = []

    for article in flux.entries[:5]:
        articles.append({
            "source": source["name"],
            "titre": article.get("title", ""),
            "lien": article.get("link", ""),
            "date": article.get("published", ""),
            "resume_rss": article.get("summary", "")
        })

    return articles