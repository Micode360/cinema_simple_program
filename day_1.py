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
refreshments = [
    {"Name": "Coke", "Price": 2900, "Recommendation": 4.6, "Category": "Drinks"},
    {"Name": "Fanta", "Price": 3000, "Recommendation": 4.5, "Category": "Drinks"},
    {"Name": "Schweppes", "Price": 4000, "Recommendation": 4.6, "Category": "Drinks"},
    {"Name": "Action Bitters", "Price": 4700, "Recommendation": 4.6, "Category": "Drinks"},
    {"Name": "Smirnoff", "Price": 9900, "Recommendation": 4.6, "Category": "Drinks"},
    {"Name": "Popcorn", "Price": 3900, "Recommendation": 4.6, "Category": "Snacks"},
    {"Name": "Doughnut", "Price": 2000, "Recommendation": 4.6, "Category": "Snacks"},
    {"Name": "Fried Buns", "Price": 1500, "Recommendation": 4.6, "Category": "Snacks"},
]

booked_movies_and_refreshments = []

# reusable functions
def list_movies_and_refreshments(movies_or_refreshments, movie_name="None",selected_refreshment = "None", type="all"):
    if type == "all":
        for movie in movies_or_refreshments:
            if "title" in movie:
                print(f"Title: {movie["title"]}, Price: ${movie["price"]}, Genre: {movie["genre"]}, Time:{movie["time"]}")
            else:
                print(f"Name: {movie["Name"]},Price: ${movie["Price"]},Recommendation: {movie["Recommendation"]},Category: {movie["Category"]},")
    elif type == "filter-movie":
        for movie in movies_or_refreshments:
            if movie["title"].replace(" ", "").lower() == movie_name.replace(" ", "").lower():
               return movie
        else:
            return False
        
    elif type == "filter-refreshment":
        for refreshment in movies_or_refreshments:
            if refreshment["Name"].replace(" ", "").lower() == selected_refreshment.replace(" ", "").lower():
                return refreshment
        else:
            return False

    
# refreshment function

def book_a_movie():
    name = input("What is your name?: ")

    # Listing of movies
    print(f"{"--" * 24}\nWhat movie do you want to see?\n{"--" * 24}")
    list_movies_and_refreshments(movies)

    # Searching a specific movie to book
    options = input(f"{"--" * 24}\nWrite the name of the movie you want to see: ")
    searched_movie = list_movies_and_refreshments(movies, movie_name=options,type= "filter-movie")

    if searched_movie == False:
        print(f"{"--" * 24}\nWrong choice of movie. Try again\n{"--" * 24}")
        return True

    # Purchase movie
    choice = input("Do you want to purchase this movie? (Yes | No): ")
    
    if choice.lower() == "Yes".lower():
        print(f"{"--" * 24}\nThe movie {searched_movie["title"]} cost {searched_movie["price"]} at {searched_movie["time"]}.\n{"--" * 24}")
        
    refresh = input(f"{"--" * 24}\n Do you want to order refreshment: ")

    if refresh == "No":
        booked_movies_and_refreshments.append({"name": name,"movie": searched_movie})
        print(f"{"--" * 24}\nYou bought {searched_movie["title"]} for {searched_movie["price"]}. Thank you.\n{"--" * 24}")
    elif refresh == "Yes":
        # Collecting refreshment details
        print(f"{"--" * 24}\nWhat refreshments do you want to have?\n{"--" * 24}")
        list_movies_and_refreshments(refreshments)
        refreshoptions = input(f"{"--" * 24}\nWhat refreshment do you want to order: ")
        selected_refreshmemt = list_movies_and_refreshments(refreshments, selected_refreshment=refreshoptions, type="filter-refreshment")

        if selected_refreshmemt == False:
            print(f"{"--" * 24}\nUnavailable.Please Try again\n{"--" * 24}")
            return True
                
        refreshmentchoice = input(f"You are about to buy {selected_refreshmemt['Name']} at {selected_refreshmemt['Price']},would you like to add it to your cart: ")

        if refreshmentchoice == "Yes":
            booked_movies_and_refreshments.append({"name": name,"extra": [selected_refreshmemt],"movie": searched_movie})
            print(f"{"--" * 24}\n {name} bought {searched_movie["title"]} for {searched_movie["price"]} and also {selected_refreshmemt['Name']} at {selected_refreshmemt["Price"]}. Thank you.\n{"--" * 24}")
                    
        else:
            booked_movies_and_refreshments.append({"name": name,"movie": searched_movie})
            return True
    else:
        print("Try Again")
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
