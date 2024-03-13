import tmdbsimple as tmdb
import requests
import matplotlib.pyplot as plt
import tweepy


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
def peopleList():
    response = requests.get(url, headers=headers)
    data = response.json()

    names_list = []

    # Iterate over the items in the 'results' list
    for item in data['results']:
        # Extract the name of each person and append it to the names_list
        name_lowercased = item['name'].lower()
        names_list.append(name_lowercased)

    return (names_list)


#getting the ids of people
def idList():
    response = requests.get(url, headers=headers)
    data = response.json()

    names_list = []
    ids_list = []

    # Iterate over the items in the 'results' list
    for item in data['results']:
        # Extract the name of each person and append it to the names_list
        name_lowercased = item['name'].lower()
        names_list.append(name_lowercased)

        ids_list.append(item['id'])


    return (ids_list)


movie_counts = {}

# getting a dictionary of the 2 

def peopleAndId():
    movie_counts = {}
    for name, person_id in zip(peopleList(), idList()):
        credits_url = f"https://api.themoviedb.org/3/person/{person_id}/movie_credits?api_key=tmdb.API_KEY&language=en-US"
        credits_response = requests.get(credits_url, headers=headers)
        credits_data = credits_response.json()
        

        movie_counts[name] = len(credits_data['cast'])

    return(movie_counts)
