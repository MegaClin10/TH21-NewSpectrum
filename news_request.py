from newsapi import NewsApiClient
import json
jsonsecrets = json.load(open("./secrets.json"))
newsapi = NewsApiClient(api_key=jsonsecrets["news-api-key"])
#sources = newsapi.get_sources()
top_headlines = newsapi.get_everything(q="bitcoin",sort_by="relevancy")
with open("searchResults.json","w") as searchResults:
    json.dump(top_headlines,searchResults)