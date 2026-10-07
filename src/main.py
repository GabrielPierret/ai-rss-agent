from rss_reader import charger_sources, recuperer_articles
from ai_analyzer import analyser_article

sources = charger_sources()

# OpenAI + MIT uniquement pour le test
for source in [sources[0], sources[2]]:
    articles = recuperer_articles(source)
    article = articles[0]

    print(f"\n--- {article['source']} ---")
    print(f"ARTICLE : {article['titre']}")

    print("\nANALYSE QWEN :")
    print(analyser_article(article))