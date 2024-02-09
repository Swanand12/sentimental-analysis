import feedparser

def google_news_scrape(query):

    url = f'https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en'
    feed = feedparser.parse(url)
    count = 0
    for entry in feed.entries:
        count = count + 1
        title = entry.title
        pubdate = entry.published
        source = entry.source.title
        print(f"{count}\nTitle: {title}\nPublished_Date: {pubdate}\nSource: {source}\n")
 
query = 'india%20budget%202024'
google_news_scrape(query)