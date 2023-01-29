import random

anime = {"Berserk":["seinen", "fantasy", "action", "adventure", "drama", "horror"], 
        "Chainsaw Man":["shounen", "action", "fantasy"], 
        "Clannad":["drama", "romance", "supernatural"], 
        "Cyberpunk: Edgerunners":["action", "sci-fi"], 
        "Vinland Saga":["action", "adventure", "drama"], 
        "Mob Psycho 100":["action", "comedy", "supernatural"], 
        "Jojo's Bizarre Adventure":["shounen", "action", "adventure", "supernatural"],
        "Hunter x Hunter":["shounen", "action", "adventure", "fantasy"],
        "Attack on Titan":["shounen", "action", "drama"],
        "Fullmetal Alchemist: Brotherhood": ["shounen", "action", "adventure", "drama", "fantasy"]}

# Picks a random anime from the anime dictionary
def randomAnime():
    print("-----Here is a random anime you should watch-----")
    # random.choice(list(***.keys())) picks a random key
    # random.choice(list(***.values())) picks a random value
    # random.choice(list(***.items())) picks a random key value pair as a tuple
    show = random.choice(list(anime.keys()))
    print("You should watch: {}!".format(show))

    # prints the value list
    print("Its genres are:", end=" ")
    for i in range(len(anime[show])-1):
        print(anime[show][i], end=", ")
    print(anime[show][len(anime[show])-1])

# Shows anime from the anime dictionary that belongs to the inputted genre
def genreSuggestion():
    print("-----What genre of anime would you want to watch?---")
    # creates a list of unique genres from the values of the anime dictionary
    genreLst=[]
    for item in anime:
        for i in range(len(anime[item])):
            if anime[item][i] not in genreLst:
                genreLst.append(anime[item][i])
    genreLst.sort()
    print("Here are the genres that you can pick from: {}".format(genreLst))

    # asks for a genre
    genre=""
    while True:
        genre = input("What genre would you like to watch?: ")
        genre = genre.lower()
        if genre not in genreLst:
            print("Please input a valid genre")
        else:
            break

    # prints a list of anime with the genre in its value list
    print("Here are some anime that are part of the {} genre: ".format(genre), end="")
    recommendedAnime=[]
    for item in anime:
        for i in range(len(anime[item])):
            if anime[item][i] == genre:
                recommendedAnime.append(item)
    print(recommendedAnime)

randomAnime()
genreSuggestion()