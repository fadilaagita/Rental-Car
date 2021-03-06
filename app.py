import tkinter
from datetime import datetime, timedelta
from tkinter import BOTH, END
from tkinter import messagebox
from tkinter import ttk

from user import User
from car import Car
from rental import Rental

class App:
    def __init__(self, users: list, cars: list):
        self.list_user = users
        self.list_car = cars
        self.user = None

        # setting tkinter window
        self.window = tkinter.Tk()
        self.window.title('Car Rental App')
        self.window.iconbitmap('icon.ico')
        self.window.resizable(False, False)

        # setting tkinter frames
        self.frame = tkinter.Frame(self.window)
        self.frame.pack()

    def run (self):
        self.login_screen()
        self.window.mainloop()

    def login_screen(self):
        self.frame.destroy()
        self.frame = tkinter.Frame(self.window)

        # set padding for the frame 10px
        self.frame.pack_propagate(False)
        self.frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # display greeting
        greeting = ttk.Label(self.frame, text='Welcome!', font=('Open Sans', 13, 'bold'))
        greeting.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='w')

        # setting labels, entry boxes, with width automatically fill the space, for entry password box, set show='*'
        ttk.Label(self.frame, text='Username').grid(row=1, column=0, sticky='w')
        ttk.Label(self.frame, text='Password').grid(row=3, column=0, sticky='w')

        self.username_entry = ttk.Entry(self.frame, width=72)
        self.password_entry = ttk.Entry(self.frame, width=72, show='*')
        
        self.username_entry.grid(row=2, column=0, pady=5, ipadx=10, ipady=5)
        self.password_entry.grid(row=4, column=0, pady=5, ipadx=10, ipady=5)

        # checkbox to show password
        self.show_password = tkinter.IntVar()
        self.show_password_checkbox = ttk.Checkbutton(self.frame, text='Show Password', variable=self.show_password, command=self.password_checkbox)
        self.show_password_checkbox.grid(row=5, column=0, sticky='w')

        # setting buttons
        ttk.Button(self.frame, text='Login', command=self.login).grid(row=6, column=0, ipadx=20, ipady=5, pady=5, sticky='w')
        ttk.Button(self.frame, text='Register', command=self.register).grid(row=6, column=0, ipadx=20, ipady=5, pady=5, sticky='e')

    def menu_screen(self):
        self.frame.destroy()
        self.frame = tkinter.Frame(self.window)

        # set padding for the frame 10px
        self.frame.pack_propagate(False)
        self.frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # display user details
        if self.user is None:
            self.login_screen()
        else:
            # display greeting
            greeting = ttk.Label(self.frame, text='Hello, ' + self.user.get_username() + '!', font=('Open Sans', 13, 'bold'))
            greeting.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='w')

            # create 4 buttons for view rentals, add rentals, logout, and quit
            view_button = ttk.Button(self.frame, text='View Rentals', command=self.rental_screen, width=72)
            add_button = ttk.Button(self.frame, text='Add Rentals', command=self.form_screen, width=72)
            logout_button = ttk.Button(self.frame, text='Logout', command=self.logout, width=72)
            exit_button = ttk.Button(self.frame, text='Exit', command=self.window.destroy, width=72)
            
            view_button.grid(row=1, column=0, ipadx=20, ipady=5, pady=5, sticky='w')
            add_button.grid(row=2, column=0, ipadx=20, ipady=5, pady=5, sticky='w')
            logout_button.grid(row=3, column=0, ipadx=20, ipady=5, pady=5, sticky='w')
            exit_button.grid(row=4, column=0, ipadx=20, ipady=5, pady=5, sticky='w')

    def rental_screen(self):
        self.frame.destroy()
        self.frame = tkinter.Frame(self.window)

        # set padding for the frame 10px
        self.frame.pack_propagate(False)
        self.frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # display rentals detail
        if self.user is None:
            self.login_screen()
        else:
            # display greeting
            greeting = ttk.Label(self.frame, text='Hello, ' + self.user.get_username() + '!', font=('Open Sans', 13, 'bold'))
            greeting.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='w')

            # create scrollable list
            scrollbar = tkinter.Scrollbar(self.frame)
            scrollbar.grid(row=1, column=1, sticky='nsew')

            # create listbox
            listbox = tkinter.Listbox(self.frame, width=72, height=10, yscrollcommand=scrollbar.set, borderwidth=0, highlightthickness=0, background='#F0F0F0')
            listbox.grid(row=1, column=0, sticky='nsew')
            scrollbar.config(command=listbox.yview)

            # display rentals
            for index, rental in enumerate(self.user.get_rentals()):
                button = ttk.Button(listbox, text=rental.get_car().get_brand(), command=lambda rental=rental: self.detail_screen(rental), width=72)
                button.grid(row=index, column=0, ipadx=20, ipady=5, pady=5, sticky='w')
                
            # create buttons
            back_button = ttk.Button(self.frame, text='Back', command=self.menu_screen, width=72)
            back_button.grid(row=2, column=0, ipadx=20, ipady=5, pady=5, sticky='w')
        
    def detail_screen(self, rental):
        self.frame.destroy()
        self.frame = tkinter.Frame(self.window)

        # set padding for the frame 10px
        self.frame.pack_propagate(False)
        self.frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # display greeting
        greeting = ttk.Label(self.frame, text='Rental Details', font=('Open Sans', 13, 'bold'))
        greeting.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='w')

        ttk.Label(self.frame, text='Car').grid(row=1, column=0, sticky='w')
        ttk.Label(self.frame, text='Start Date').grid(row=3, column=0, sticky='w')
        ttk.Label(self.frame, text='End Date').grid(row=5, column=0, sticky='w')
        ttk.Label(self.frame, text='Total Price').grid(row=7, column=0, sticky='w')
        
        brand = ttk.Entry(self.frame, width=76)
        start_date = ttk.Entry(self.frame, width=76)
        end_date = ttk.Entry(self.frame, width=76)
        total_price = ttk.Entry(self.frame, width=76)

        brand.insert(0, rental.get_car().get_brand())
        start_date.insert(0, rental.get_start_date().strftime('%A, %d/%B/%Y'))
        end_date.insert(0, rental.get_end_date().strftime('%A, %d/%B/%Y'))
        total_price.insert(0, rental.get_total_price())

        brand.grid(row=2, column=0, pady=5, ipadx=10, ipady=5, sticky='w')
        start_date.grid(row=4, column=0, pady=5, ipadx=10, ipady=5, sticky='w')
        end_date.grid(row=6, column=0, pady=5, ipadx=10, ipady=5, sticky='w')
        total_price.grid(row=8, column=0, pady=5, ipadx=10, ipady=5, sticky='w')

        # create buttons
        back_button = ttk.Button(self.frame, text='Back', command=self.rental_screen, width=72)
        back_button.grid(row=9, column=0, ipadx=20, ipady=5, pady=5, sticky='w')

    def form_screen(self):
        self.frame.destroy()
        self.frame = tkinter.Frame(self.window)
        
        # set padding for the frame 10px
        self.frame.pack_propagate(False)
        self.frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # display user details
        if self.user is None:
            self.login_screen()
        else:
            # display greeting
            greeting = ttk.Label(self.frame, text='Add New Rental', font=('Open Sans', 13, 'bold'))
            greeting.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='w')

            # labels for Cars choice, duration, start date and end date, price, total
            ttk.Label(self.frame, text='Cars').grid(row=1, column=0, sticky='w')
            ttk.Label(self.frame, text='Duration').grid(row=3, column=0, sticky='w')
            ttk.Label(self.frame, text='Start Date').grid(row=5, column=0, sticky='w')
            ttk.Label(self.frame, text='End Date').grid(row=7, column=0, sticky='w')
            ttk.Label(self.frame, text='Price').grid(row=9, column=0, sticky='w')
            ttk.Label(self.frame, text='Total').grid(row=11, column=0, sticky='w')

            # set variables
            brand = tkinter.StringVar()
            duration = tkinter.StringVar()
            self.confirm_rental = tkinter.IntVar()

            # set entryboxes
            self.car_entry = ttk.Combobox(self.frame, textvariable=brand, width=70, values=self.list_car)
            self.duration_entry = ttk.Spinbox(self.frame, textvariable=duration, width=70, from_=1, to=30)
            self.start_date_entry = ttk.Entry(self.frame, width=72)
            self.end_date_entry = ttk.Entry(self.frame, width=72)
            self.price_entry = ttk.Entry(self.frame, width=72)
            self.total_entry = ttk.Entry(self.frame, width=72)
            self.confirm_rental_checkbox = ttk.Checkbutton(self.frame, text='Confirm Rental', variable=self.confirm_rental, command=self.confirm_checkbox)

            # set grid position
            self.car_entry.grid(row=2, column=0, pady=5, ipadx=10, ipady=5)
            self.duration_entry.grid(row=4, column=0, pady=5, ipadx=10, ipady=5)
            self.start_date_entry.grid(row=6, column=0, pady=5, ipadx=10, ipady=5)
            self.end_date_entry.grid(row=8, column=0, pady=5, ipadx=10, ipady=5)
            self.price_entry.grid(row=10, column=0, pady=5, ipadx=10, ipady=5)
            self.total_entry.grid(row=12, column=0, pady=5, ipadx=10, ipady=5)
            self.confirm_rental_checkbox.grid(row=13, column=0, pady=5, ipadx=10, ipady=5, sticky='w')

            # bind entry to update car
            self.car_entry.bind('<<ComboboxSelected>>', self.calculate_price)
            self.duration_entry.bind('<ButtonRelease-1>', self.calculate_price)

            # button to rent car
            self.rental_button = ttk.Button(self.frame, text='Rent Car', state='disabled', command=self.validate_rent)
            self.rental_button.grid(row=14, column=0, ipadx=20, ipady=5, pady=5, sticky='w')

            # button to go back to menu
            back_button = ttk.Button(self.frame, text='Back', command=self.menu_screen)
            back_button.grid(row=14, column=0, ipadx=20, ipady=5, pady=5, sticky='e')

    def validate_rent(self):
        duration = self.duration_entry.get()

        # get rentals data from entry boxes and append to rentals list of user
        if duration != '' and self.user is not None:
            rental = Rental(self.car, int(duration))
            self.user.add_rentals(rental)
            
            messagebox.showinfo('Rental', 'Rental added')
            self.menu_screen()

    def confirm_checkbox(self):
        brand = self.car_entry.get()
        duration = self.duration_entry.get()

        # enable rental button if checkbox is checked and the entry boxes are filled
        if brand != '' and duration != '':
            self.rental_button.config(state='normal' if self.confirm_rental.get() else 'disabled')

    def calculate_price(self, event):
        brand = self.car_entry.get()
        duration = self.duration_entry.get()

        # update the entry boxes values with the selected car price and duration
        if brand != '' and duration != '':
            for item in self.list_car:
                if item.get_brand() == brand:
                    self.car = item

            price = self.car.get_price()
            total = self.car.get_price() * int(duration)
            
            self.price_entry.delete(0, END)
            self.price_entry.insert(0, price)

            self.total_entry.delete(0, END)
            self.total_entry.insert(0, total)

            self.start_date_entry.delete(0, END)
            self.start_date_entry.insert(0, datetime.today().strftime('%A, %d/%B/%Y'))
            
            self.end_date_entry.delete(0, END)
            self.end_date_entry.insert(0, (datetime.today() + timedelta(days=int(duration))).strftime('%A, %d/%B/%Y'))


    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        
        for user in self.list_user:
            if user.validate(self.username, self.password):
                self.user = user
                break

        if self.user is None:
            messagebox.showinfo('Login Failed', 'Invalid username or password')
            self.password_entry.delete(0, 'end')
        else:
            self.menu_screen()

    def password_checkbox(self):
        # checkbox to display password
        self.password_entry.config(show='' if self.show_password.get() else '*')

    def register(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        user = User(self.username, self.password)
        
        self.list_user.append(user)
        self.login()

    def logout(self):
        self.user = None
        self.login_screen()

def main() -> None:
    users = [
        User('admin', 'password'),
        User('user', 'password')
    ]

    cars = [
        Car('Ferrari', 5000000),
        Car('Lamborghini', 6000000),
        Car('Alphard', 4000000),
        Car('Bugatti', 7000000),
        Car('Avanza', 200000)
    ]

    app = App(users, cars)
    app.run()

if __name__ == '__main__':
    main()