import requests

api_key = 'bee5a0ffe13c461eb537b5fc691941c3'
base_url = 'https://newsapi.org/v2/everything'

params = {
    'q':'india budget 2024',
    'language': 'en',
    'sortBy': 'publishedAt',
    # 'country': 'in',  
    # 'category': 'business',
    # 'pageSize': 10,
    'from': '2024-02-01T08:00:00',
    'to': '2024-02-01T12:19:00',
    # 'page': '5',
    # "category" :"sports",
    'apiKey': api_key,
}
        
response = requests.get(base_url, params=params)
data = response.json()
count = 0

for article in data['articles']:
        
        count = count + 1
        print(f"{count}\nTitle: {article['title']}" + "\n"
              + f"Published_At: {article['publishedAt']}" )
        print( f"Author: {article['author']}" )

        # below code is for country orgin identifier based on name of author

        name =article['author']
    
        if str(name) != "None":
            names = name.split()
            url = f'https://api.nationalize.io/?name={names[0]}'

            response = requests.get(url)
            names_data = response.json()
            print(names_data)
            for country_info in names_data["country"][0]:
                    country_id = country_info["country_id"]
                    print(f"Country: {country_id}\n")
        else:
            print("Country: None")

        #----
            
        print( f"Source: {article['source']['name']}" + "\n")
