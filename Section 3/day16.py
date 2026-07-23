# Milestone Project - 1 (A Movie Collection App)

Menu_Prompt = "\n Enter \n'1' to add movie \n'2' to see movies \n'3' to find a movie \n'4' to quit: \n"
movies = []     # List to store movies

def add_movies():
    title = input("Enter movie name: ").lower()
    director = input("Enter director name: ").lower()
    year = input("Enter released year: ")

    # Adding movies to the list - movies
    movies.append(
        {
            'title': title,
            'director': director,
            'year': year
        }
    )

def print_movies(movie):
    print(f"Movie Title: {movie['title']}")
    print(f"Movie Director: {movie['director']}")
    print(f"Released Year: {movie['year']}")
        

def show_movies():
    for movie in movies:
        print_movies(movie)


def find_movies():
    search_title = input("Enter the movie name you are searcing for: ").lower()
    
    for movie in movies:
        if movie['title'] == search_title:
            print_movies(movie)


# First class functions - in order to simplify code instead of using multiple conditional statements
user_options = {
    '1': add_movies,
    '2': show_movies,
    '3': find_movies
}

def user_menu():
    user_input = input(Menu_Prompt)
    
    while user_input != 'q':
        if user_input in user_options:
            selected_option = user_options[user_input]
            selected_option()    
        else:
            print("Enter a valid command!!")
            
        user_input = input(Menu_Prompt)

user_menu()