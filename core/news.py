import requests
import cohere
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def get_news(category='general', count=3):
    api_key = '913676556ca74622a485f609c48f7f06'  # Replace with your NewsAPI key
    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={api_key}'
    
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        # Filter out articles with no description
        filtered_articles = [
            {'title': article['title'], 'description': article['description']}
            for article in articles
            if article.get('description')
        ]
        return filtered_articles[:count]  # Return only the top `count` articles
    else:
        print("Failed to fetch news")
        return []


def summarize_text(text, sentences_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return " ".join([str(sentence) for sentence in summary])

def categorize_news(query):
    query = query.lower()
    
    if any(word in query for word in ["sport", "match", "football", "cricket", "tennis"]):
        return "sports"
    elif any(word in query for word in ["tech", "ai", "gadgets", "smartphone", "startup", "software"]):
        return "technology"
    elif any(word in query for word in ["business", "stock", "market", "finance", "investment", "economy"]):
        return "business"
    elif any(word in query for word in ["movie", "entertainment", "celebrity", "tv", "series", "hollywood", "bollywood"]):
        return "entertainment"
    elif any(word in query for word in ["health", "fitness", "medicine", "covid", "mental health", "disease"]):
        return "health"
    elif any(word in query for word in ["science", "research", "space", "nasa", "discovery", "experiment"]):
        return "science"
    elif any(word in query for word in ["politics", "election", "government", "policy", "modi", "biden", "parliament"]):
        return "politics"
    elif any(word in query for word in ["world", "international", "global", "foreign"]):
        return "world"
    elif any(word in query for word in ["crime", "law", "police", "arrest", "court"]):
        return "crime"
    elif any(word in query for word in ["education", "school", "college", "university", "exam", "result"]):
        return "education"
    elif any(word in query for word in ["travel", "tourism", "destination", "trip", "vacation", "holiday"]):
        return "travel"
    elif any(word in query for word in ["environment", "climate", "weather", "nature", "pollution", "disaster"]):
        return "environment"
    elif any(word in query for word in ["automobile", "car", "vehicle", "bike", "electric vehicle", "EV"]):
        return "automobile"
    elif any(word in query for word in ["real estate", "property", "housing", "home loan", "apartment"]):
        return "real estate"
    elif any(word in query for word in ["fashion", "style", "clothing", "makeup", "outfit"]):
        return "fashion"
    else:
        return "general"


    return response.classifications[0].prediction

# Example usage
if __name__ == "__main__":
    query = "Tell me about the latest technology news"
    category = categorize_news(query)
    news = get_news(category)
    for article in news:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        summary = summarize_text(article['description'])
        print(f"Summary: {summary}")
        print()
