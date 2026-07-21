# Project 1 - Movies Collection app

# Trial 2 - Modified with Trail 1

movies = [
    {
        "movie_name": "Chakram",
        "director": "Krishna Vamsi",
        "year": 2005,
        "hero": "Prabhas"
    },
    {
        "movie_name": "Surya S/O Krishnan",
        "director": "Gautham Vasudev Menon",
        "year": 2008,
        "hero": "Suriya"
    },
    {
        "movie_name": "Aarya 2",
        "director": "Sukumar",
        "year": 2009,
        "hero": "Allu Arjun"
    },
    {
        "movie_name": "Animal",
        "director": "Sandeep Reddy Vanga",
        "year": 2023,
        "hero": "Ranbir Kapoor"
    },
    {
        "movie_name": "Salaar",
        "director": "Prashanth Neel",
        "year": 2023,
        "hero": "Prabhas"
    },
    {
        "movie_name": "Athadu",
        "director": "Trivikram Srinivas",
        "year": 2005,
        "hero": "Mahesh Babu"
    }
]

user_input = input("Enter (movie name/ director name/ year/ hero name : )").strip().lower()


def movie_details(search):
    found_movies = []       # creating a list to store found movies
    
    for movie in movies:
        values = [str(value).lower() for value in movie.values()]     # store values from key:value pair of dictionaries and make them into strings & lowercase and stores in variable "values"
        
        if search in values:
            found_movies.append(movie)      # if the searched one is found in the values then that movie is appended to the list
            
    if found_movies:
        print("\n Movie Details Found: \n")
        
        for movie in found_movies:
            print(f"Movie Name: {movie['movie_name']}")
            print(f"Director Name: {movie['director']}")
            print(f"Released Year: {movie['year']}")
            print(f"Hero: {movie['hero']} \n")
    
    else:
        print("Movie Not Found!!")
    
    
movie_details(user_input)