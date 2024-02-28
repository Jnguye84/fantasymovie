import tmdbsimple as tmdb
import requests
import matplotlib.pyplot as plt

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
ids_list = []

# Iterate over the items in the 'results' list
for item in data['results']:
    # Extract the name of each person and append it to the names_list
    names_list.append(item['name'])
    ids_list.append(item['id'])

movie_counts = {}

for name, person_id in zip(names_list, ids_list):
    credits_url = f"https://api.themoviedb.org/3/person/{person_id}/movie_credits?api_key=tmdb.API_KEY&language=en-US"
    credits_response = requests.get(credits_url, headers=headers)
    credits_data = credits_response.json()
    
    #assums "cast" contains the movies they acted in idk 
    movie_counts[name] = len(credits_data['cast'])



print(names_list)
print(ids_list)
print(movie_counts)
    



#scatter plot
names = list(movie_counts.keys())
counts = list(movie_counts.values())

# Creating the scatter plot
plt.figure(figsize=(10, 8))
plt.scatter(names, counts, color='blue')
plt.title('Number of Movies per Actor')
plt.xlabel('Actor')
plt.ylabel('Number of Movies')
plt.xticks(rotation=90)
plt.show()


'''
#movie = tmdb.Movies(205)
search = tmdb.Search()
response = search.person(query='Denzel Washington')
response = search.popular()

#response = movie.info()
print(response)
'''
