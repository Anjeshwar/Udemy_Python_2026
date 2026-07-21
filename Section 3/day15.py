# Project 1 - Movies Collection app

# Trial 1

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

user_input = input("Enter (movie name/ director name/ year/ hero name : )").strip()

def movie_details(search):
    found = False
    
    for movie in movies:
        if(
            search.lower() == movie["movie_name"].lower()
            or search.lower() == movie["director"].lower()
            or search.lower() == str(movie["year"])
            or search.lower() == movie["hero"].lower()
        ):
            print("\n Movie Details Found: ")
            print(f"Movie name: {movie["movie_name"]}")
            print(f'Director: {movie["director"]}')
            print(f'Released year: {movie["year"]}')
            print(f'Hero: {movie['hero']}')



movie_details(user_input)