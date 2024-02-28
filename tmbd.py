import tmdbsimple as tmdb
import requests
import json

#api key
tmdb.API_KEY = 'e4194ed7bb70d235c3f504a4165912d3'

#looks for a timeout
tmdb.REQUESTS_TIMEOUT = 5  # seconds, for both connect and read

#trying to get popular ppl list
url = "https://api.themoviedb.org/3/person/popular?language=en-US&page=1"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNDE5NGVkN2JiNzBkMjM1YzNmNTA0YTQxNjU5MTJkMyIsInN1YiI6IjY1ZGViYjdmYjc2Y2JiMDE3ZGQ4MmU1NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oDFY-ZXo3kpelC1epuW_fNyIKL5X1aYQmcyWsCNIDB0"
}


#getting a list of popular people 
response = requests.get(url, headers=headers)
data = response.json()

names_list = []

# Iterate over the items in the 'results' list
for item in data['results']:
    # Extract the name of each person and append it to the names_list
    names_list.append(item['name'])

print(names_list)

for person in names_list:
    



'''
#movie = tmdb.Movies(205)
search = tmdb.Search()
response = search.person(query='Denzel Washington')
response = search.popular()

#response = movie.info()
print(response)
'''