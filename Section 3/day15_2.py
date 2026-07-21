# Project 1 - Movies Collection app

# Includes Adding movies, Viewing all movies, Searching movies and exit

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


# Adding new movies
def add_movie():
    admin_password = "AnjeshMovies"
    
    password = input("Enter admin password: ")
    
    if password != admin_password:
        print("Access Denied!! Only admin can add movies..")
        return
    
    print("\n Enter New Movie Details: ")
    
    movie_name = input("Movie name: ").strip()
    director = input("Director name: ").strip()
    year = int(input("Released year: "))
    hero = input("Hero name: ").strip()
    
    new_movie = {
        "movie_name": movie_name,
        "director": director,
        "year": year,
        "hero": hero
    }
    
    movies.append(new_movie)
    
    print(f"{movie_name} added Successfully!")
    

# Searching movies
def search_movie():
    search = input("Enter Movie name/ Director/ Year/ Hero: ").strip().lower()
    
    found_movies = []
    
    for movie in movies:
        values = [str(value).lower() for value in movie.values()]
        
        if search in values:
            found_movies.append(movie)
            
    if found_movies:
        print("\n Movie Details Found: \n")
        
        for movie in found_movies:
            print(f"Movie Name: {movie['movie_name']}")
            print(f"Director Name: {movie['director']}")
            print(f"Released Year: {movie['year']}")
            print(f"Hero Name: {movie['year']}")
            
    else:
        print("\n Movie Not Found..\n")
        
        
# Viewing all movies
def view_all_movies():
    if not movies:
        print("No Movies Available. \n")
        return
    
    print("\n --------------- All Movies Collection ----------------\n")
    
    for index, movie in enumerate(movies, start=1):
        print(f"Movie {index}")
        print(f"Movie Name    : {movie['movie_name']}")
        print(f"Director Name : {movie['director']}")
        print(f"Released Year : {movie['year']}")
        print(f"Hero          : {movie['hero']}")
        print("-" * 45)
        
        
# Iterating the Loop & Selecting the choices
while True:
    print("\n====== MOVIE COLLECTION APP ======")
    print("1. Search Movie")
    print("2. View All Movies")
    print("3. Add Movie (Admin)")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        search_movie()
    elif choice == "2":
        view_all_movies()
    elif choice == "3":
        add_movie()
    elif choice == "4":
        print("Thank you for using Movie Collection App!")
        break
    else:
        print("Invalid choice! Please enter 1-4.\n")