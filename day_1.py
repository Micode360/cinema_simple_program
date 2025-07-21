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
# Admin login details
admin_login_details = {
    "username": "admin",
    "password": "admin123"
}
# Function to handle admin login
def admin_login():
    print(f"{"--" * 24}\nWelcome to the Admin Dashboard.\n{"--" * 24}")
    username = input("Enter your username: ").lower()
    password = input("Enter your password: ").lower()
 # Check if the username and password match the admin login details
    if username == admin_login_details["username"] and password == admin_login_details["password"]:
        print(f"{"--" * 24}\nLogin successful!\n{"--" * 24}")
        return True
    # If the credentials are incorrect, prompt the user to try again
    else:
        print(f"{"--" * 24}\nInvalid credentials. Please try again.\n{"--" * 24}")
        return admin_login()
    

booked_movies_and_refreshments = []
booking_slot = 14

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
    if len(booked_movies_and_refreshments) >= booking_slot:
        print(f"{"--" * 24}\nBooking slot is full. Please try again later.\n{"--" * 24}")
        return True
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
    

        # Function to view all bookings and also calculate total revenue
def view_all_bookings():
    if not booked_movies_and_refreshments:
        print(f"{"--" * 24}\nNo bookings available.\n{"--" * 24}")
    else:
        print(f"{"--" * 24}\nBooked Movies and Refreshments:\n{"--" * 24}")
        total_revenue = 0
        for booking in booked_movies_and_refreshments:
            name = booking["name"]
            movie_title = booking["movie"]["title"]
            movie_price = booking["movie"]["price"]
            total = booking["total"]
            total_revenue += total

            if refreshments:
                refresh_name = refreshments["Name"]
                refresh_price = refreshments["Price"]
            print(f"{name} booked {movie_title} for {movie_price} and also {refresh_name} at {refresh_price} and the Total is {total} .")
        else:
            print(f"{name} booked {movie_title} for {movie_price} and the Total is {total}.")

            print(f"/nTotal bookings: {len(booked_movies_and_refreshments)} / {booking_slot}")
            print(f"Total Revenue: {total_revenue}")

# Function to view revenue summary and calculate total revenue
def view_revenue_summary():
    print(f"{"--" * 24}\nNo bookings available.\n{"--" * 24}")
    movie_total = 0
    refreshment_total = 0
    for booking in booked_movies_and_refreshments:
        movie_total += booking["movie"]["price"]
        if "refreshment" in booking:
            refreshment_total += booking["refreshment"]["Price"]
    total_revenue = movie_total + refreshment_total
    print(f"Total Revenue from Movies: {movie_total}")
    print(f"Total Revenue from Refreshments: {refreshment_total}")
    print(f"Overall Total Revenue: {total_revenue}")
    print(f"Total Bookings: {len(booked_movies_and_refreshments)} / {booking_slot}")

# Function to cancel an order by inputting the name of the booking
def cancel_order():
    if not booked_movies_and_refreshments:
        print(f"{"--" * 24}\nNo bookings available to cancel.\n{"--" * 24}")
        return
    name_to_cancel = input("Enter the name of the booking to cancel: ").replace(" ", "").lower()
    for booking in booked_movies_and_refreshments:
        if booking["name"].lower() == name_to_cancel.lower():
            booked_movies_and_refreshments.remove(booking)
            print(f"Order for {booking["name"]} has been cancelled.")
            return
# If no matching booking is found, print a message
        print(f"{"--" * 24}\nNo matching booking found for {name_to_cancel}.\n{"--" * 24}")

    # Admin Dashboard with menu to view bookings, revenue and cancel orders
def admin_dashboard_menu():
    while True:
        print(f"{"--" * 24}\nAdmin Dashboard menu\n{"--" * 24}")
        print("1. View all bookings.")
        print("2. View revenue summary.")
        print("3. Cancel an order.")
        print("4. Back to main menu.")
        admin_option = input("Choose an option (1 | 2 | 3 | 4): ").strip()
        if admin_option not in ["1", "2", "3", "4"]:
            print(f"{"--" * 24}\nInvalid option. Please try again.\n{"--" * 24}")
            return True
        if admin_option == "1":
            view_all_bookings()
        elif admin_option == "2":
            view_revenue_summary()
        elif admin_option == "3":
            cancel_order()
        elif admin_option == "4":
            return False
        else:
            print(f"{"--" * 24}\ninvalid option. Please try again.\n{"--" * 24}")
            return True
                
# Main function to run the program
def main():
    print(f"{"--" * 24}\nWelcome to Genesis Cinema.\n{"--" * 24}")

    while True:
        options = input("1. Book a movie.\n2. View all movies.\n3. Admin Dashboard.\n4 Exit\nChoose any options (1 | 2 | 3 | 4 |): ")
    
        if options == "1":
            book_a_movie()
        if options == "2":
            print("Option 2")
        if options == "3":
           if admin_login():
            admin_dashboard_menu()
        if options == "4":
            print("Option 4")
        if options == "5":
            break
           

                    



main() # Running the program.
