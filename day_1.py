movies = [
    {"title": "Avatar", "price": 2500, "genre": "Sci-Fi", "time": "12:00 PM"},
    {"title": "Barbie", "price": 2000, "genre": "Fantasy/Comedy", "time": "1:30 PM"},
    {"title": "Fast X", "price": 3000, "genre": "Action", "time": "3:00 PM"},
    {"title": "Oppenheimer", "price": 3500, "genre": "Drama/History", "time": "4:30 PM"},
    {"title": "The Little Mermaid", "price": 1800, "genre": "Musical/Fantasy", "time": "6:00 PM"},
    {"title": "Mission Impossible", "price": 3200, "genre": "Action/Thriller", "time": "7:30 PM"},
    {"title": "John Wick 4", "price": 2800, "genre": "Action/Crime", "time": "9:00 PM"},
    {"title": "Spider-Man: No Way Home", "price": 2700, "genre": "Superhero/Sci-Fi", "time": "10:30 AM"},
    {"title": "Black Panther: Wakanda Forever", "price": 2600, "genre": "Superhero/Action", "time": "11:45 AM"},
    {"title": "The Batman", "price": 2900, "genre": "Superhero/Crime", "time": "2:15 PM"},
    {"title": "Super Mario Bros", "price": 2100, "genre": "Animation/Adventure", "time": "5:45 PM"},
    {"title": "Guardians of the Galaxy Vol. 3", "price": 3100, "genre": "Superhero/Comedy", "time": "8:00 PM"}
]
drink = [
    {"Name": "Coke", "Price": 2900, "Recommendation": 4.6, "Category": "Drinks"},
    {"Name": "Fanta", "Price": 3000, "Recommendation": 4.5, "Category": "Drinks"},
    {"Name": "Schweppes", "Price": 4000, "Recommendation": 4.6, "Category": "Drinks"},
    {"Name": "Action Bitters", "Price": 4700, "Recommendation": 4.6, "Category": "Drinks"},
    {"Name": "Smirnoff", "Price": 2900, "Recommendation": 4.6, "Category": "Drinks"},
    {"Name": "Popcorn", "Price": 2900, "Recommendation": 4.6, "Category": "Snacks"},
    {"Name": "Doughnut", "Price": 2900, "Recommendation": 4.6, "Category": "Snacks"},
    {"Name": "Fried Buns", "Price": 2900, "Recommendation": 4.6, "Category": "Snacks"},
]

booked_movies = []

drinks = []

def list_movies(movies, movie_name="None", type="all"):
    if type == "all":
        for movie in movies:
            print(f"Title: {movie["title"]}, Price: ${movie["price"]}, Genre: {movie["genre"]}, Time:{movie["time"]}")
    elif type == "filter":
        for movie in movies:
            if movie["title"].replace(" ", "").lower() == movie_name.replace(" ", "").lower():
               return movie
        else:
            return False


def book_a_movie():
    name = input("What is your name?: ")
    # Listing of movies
    print(f"{"--" * 24}\nWhat movie do you want to see?\n{"--" * 24}")
    list_movies(movies)

    # Searching a specific movie to book
    options = input(f"{"--" * 24}\nWrite the name of the movie you want to see: ")
    searched_movie = list_movies(movies, options, "filter")

    if searched_movie == False:
        print(f"{"--" * 24}\nWrong choice of movie. Try again\n{"--" * 24}")
        return True



    # Purchase movie
    print(f"{"--" * 24}\nThe movie {searched_movie["title"]} cost {searched_movie["price"]} at {searched_movie["time"]}.\n{"--" * 24}")
    choice = input("Do you want to purchase this movie? (Yes | No): ")
    
    if choice.lower() == "Yes".lower():
        booked_movies.append({"name": name,"extra": [],"movie": searched_movie})
        print(f"{"--" * 24}\nYou bought {searched_movie["title"]} for {searched_movie["price"]}. Thank you.\n{"--" * 24}")
    elif choice.lower() == "No".lower():
        return True
    return True



def main():
    print(f"{"--" * 24}\nWelcome to Genesis Cinema.\n{"--" * 24}")

    while True:
        options = input("1. Book a movie.\n2. View all movies.\n3. Exit\nChoose any options (1 | 2 | 3): ")
    
        if options == "1":
            book_a_movie()
        if options == "2":
            print("Option 2")
        if options == "3":
            print("Option 3")
        if options == "4":
            print("Option 4")
        if options == "5":
            break



main() # Running the program.
