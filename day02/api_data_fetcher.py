import requests # to make HTTP requests

random_joke_url = "https://official-joke-api.appspot.com/random_joke" # API endpoint for random joke
dad_joke_url = "https://api.lyrics.ovh/v1/:artist/:title"

# function to fetch and print a joke

def get_joke(url_type):
    response = requests.get(url=random_joke_url) # making a GET request to the joke API
    final_response = response.json() ["setup"] + response.json() ["punchline"]
    return final_response

mood = input ("Which type of Jokes you want to hear? (random/dad): ")
if mood == "random":
    final_response = get_joke(random_joke_url)
elif mood == "dad":
    final_response = get_joke(dad_joke_url)
else:
    print ("Invalid choice")

print (final_response)

file_name = "joke.json"
with open (file_name, "w") as file:
    file.write(final_response) # writing the joke to a file

print (f"Joke has been saved to {file_name}.......")


