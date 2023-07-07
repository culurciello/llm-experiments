import requests
from bs4 import BeautifulSoup
import trafilatura

headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }

def getSearchData(query, num_results=10):#, max_length=1500):
    search_req = "https://www.google.com/search?q="+query+"&gl=us&tbm=nws&num="+str(num_results)+""
    # print(bcolors.OKGREEN + "ANALYZING:", search_req, "..."+bcolors.ENDC)
    news_results = []
    
    # get webpage content
    response = requests.get(search_req, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    for el in soup.select("div.SoaBEf"):
        sublink = el.find("a")["href"]
        downloaded = trafilatura.fetch_url(sublink)
        html_text = trafilatura.extract(downloaded)
        # if html_text:
        #     sentences = tokenize.sent_tokenize(html_text)
        #     # truncate sentences that are too long
        #     for i,s in enumerate(sentences):
        #         if len(s)>max_length:
        #             sentences[i]=sentences[i][:max_length]

        #     sentiment = sentiment_analyzer(sentences)
        #     sum = 0
        #     neutrals = 0
        #     if len(sentiment) > 0:
        #         for r in sentiment: 
        #             sum += (r["label"] == "Positive")
        #             neutrals += (r["label"] == "Neutral")

        #         den = len(sentiment)-neutrals
        #         sentiment = sum/den if den > 0 else 1.0 # as all neutral

        #         news_results.append(
        #             {
        #                 "link": el.find("a")["href"],
        #                 "title": el.select_one("div.MBeuO").get_text(),
        #                 "snippet": el.select_one(".GI74Re").get_text(),
        #                 "date": el.select_one(".LfVVr").get_text(),
        #                 "source": el.select_one(".NUnG9d span").get_text(),
        #                 # "text": html_text,
        #                 "sentiment": sentiment,
        #             }
        #         )

    return html_text