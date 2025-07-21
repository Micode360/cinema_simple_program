import tkinter as tk
from tkinter import ttk, messagebox

movies = [
    {"title": "Avatar", "price": 2500, "genre": "Sci-Fi", "time": "12:00 PM"},
    {"title": "Barbie", "price": 2000, "genre": "Fantasy/Comedy", "time": "1:30 PM"},
    {"title": "Fast X", "price": 3000, "genre": "Action", "time": "3:00 PM"},
    # ... add more if you want
]

class CinemaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Genesis Cinema Booking")
        self.geometry("500x400")
        self.configure(padx=20, pady=20)

        self.style = ttk.Style(self)
        self.style.theme_use('clam')  # better looking theme than default

        self.create_widgets()

    def create_widgets(self):
        header = ttk.Label(self, text="Select a movie to book:", font=("Helvetica", 16, "bold"))
        header.pack(pady=(0,10))

        # Frame for listbox and scrollbar
        list_frame = ttk.Frame(self)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.movie_listbox = tk.Listbox(list_frame, height=10, font=("Helvetica", 12))
        self.movie_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.movie_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.movie_listbox.config(yscrollcommand=scrollbar.set)

        for movie in movies:
            text = f"{movie['title']} - {movie['genre']} - {movie['time']} - ₦{movie['price']}"
            self.movie_listbox.insert(tk.END, text)

        self.book_button = ttk.Button(self, text="Book Movie", command=self.book_movie)
        self.book_button.pack(pady=15)

        self.status_label = ttk.Label(self, text="", font=("Helvetica", 12), foreground="green")
        self.status_label.pack()

    def book_movie(self):
        selected_indices = self.movie_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("No Selection", "Please select a movie to book.")
            return

        index = selected_indices[0]
        movie = movies[index]
        msg = f"You booked {movie['title']} costing ₦{movie['price']} at {movie['time']}."
        self.status_label.config(text=msg)
        messagebox.showinfo("Booking Confirmed", msg)

if __name__ == "__main__":
    app = CinemaApp()
    app.mainloop()
