import tmdbsimple as tmdb
tmdb.API_KEY = 'bb76d810eac6dda796c6389702e136b2'
import requests
import json

# tried to use TMDB3 package but it doesn't support python 3 :(
# movie = tmdb.Movies(603)
# response = movie.info()
# print(movie.title) 


url = "https://api.themoviedb.org/3/person/popular?language=en-US&page=1"

# last index of the url to access the page numbers
page_number = url[64]


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYjc2ZDgxMGVhYzZkZGE3OTZjNjM4OTcwMmUxMzZiMiIsInN1YiI6IjY1YzgyMDM4YWFkOWMyMDE3ZGI3N2E1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Leg6ljhB2dwm5KLzNpx_9BNBpNb6yfwDnazIkZ0orSI"
}

response = requests.get(url, headers=headers)

response_json = json.loads(response.text)


# page and results are keys
# results of the dictionary
results = response_json['results']

# actors we want with IMDB's characteristics
top_actors = ['Tom Hanks','Meryl Streep', 'Denzel Washington', 'Scarlett Johansson', 'Leonardo DiCaprio', 'Viola Davis', 'Brad Pitt', 'Sandra Bullock', 'Morgan Freeman', 'Jennifer Lawrence']
top_actor_characteristics = []

# count amount of actors until 20 to move onto next page)
count = 0


# get the first person's name on the top of the list
# person_name = results[0]['name']
# print(results[2])

while len(top_actor_characteristics) != 10:
    for i in range(20):
        if results[i]['name'] in top_actors:
            top_actor_characteristics.append(results[i]['name'])
            top_actors.remove(results[i]['name'])
    count += 1
    url = "https://api.themoviedb.org/3/person/popular?language=en-US&page=1"
    s = list(url)
    s[64] = str(count)
    url = ''.join(s)
    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    results = response_json['results']

print(top_actor_characteristics)

# print the first 10 people
# for i in range(10):
#     print(results[i]['name'])






# Tom Hanks
# Meryl Streep
# Denzel Washington
# Scarlett Johansson
# Leonardo DiCaprio
# Viola Davis
# Brad Pitt
# Sandra Bullock
# Morgan Freeman
# Jennifer Lawrence