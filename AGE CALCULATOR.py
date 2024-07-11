# AGE CALCULATOR
import builtins
import statistics
# creators:
# سالم الرحيمان 2230001023
# علي عبدالله الزهراني 2230007267
# عبدالرحمن الزهراني 2230003733
# سعود الدليجان 2230003025
# ناصر سالم الخالدي 2230002041
# فيصل احمد العمهوج 2230001991

# Discription:
# This app calculates user's age by selecting the birth_date.
# The user must enter a date that older than current date.

# App features:
# This app calculates user's age in years, months, and days.

# How to use:
#    -Select your birth_date in the Comboboxes, and then, press Calculate button.
#    -The result will be printed in the result box above the Comboboxes.
#    -You can erase the result by pressing Erase button.
#    -If you select the current date or a future date,
#     then the calculator will return ERROR messege.
#    -This calculator calculates ages in years, months, and days.

# ©2023-2024, AGE CALCULATOR™. Made in KSA.

# importing the modules tkinter, datetime, tkcalendar and their functions.
import tkinter as tk
from tkinter import ttk
from tkinter import *
from calendar import month_name
from datetime import *

# printing the cataloge of the app.
print("AGE CALCULATOR\n")
print("Creators:"
      "\nسالم الرحيمان 2230001023"
      "\nعلي عبدالله الزهراني 2230007267"
      "\nعبدالرحمن الزهراني 2230003733"
      "\nسعود الدليجان 2230003025"
      "\nناصر سالم الخالدي 2230002041"
      "\n2230001991 فيصل احمد العمهوج")
print("\nDiscription:\n"
      "This app calculates user's age by selecting the birth_date.\n"
      "The user must enter a date that older than current date.")
print("\nApp features:\n"
      "This app calculates user's age in years, months, and days.\n")
print("How to use:\n"
      "   -Select your birth date in the Comboboxes, and then, press Calculate button.\n"
      "   -The result will be printed in the result box above the Comboboxes.\n"
      "   -You can erase the result by pressing Erase button.\n"
      "   -If you select the current date or a future date,\n"
      "    then the calculator will return ERROR messege.\n"
      "   -This calculator calculates ages in years, months, and days.\n")
print("©2023-2024, AGE CALCULATOR™. Made in KSA.")

def ageCalculator(birthDate):  # The data type of the periemeter is string.
    months_with_30_days = ('Apr', 'Jun', 'Sep', 'Nov') # The list of all months that only have 30 days.
    # This is calculator's function
    today = date.today()  # Stores current Date.
    birthDate = datetime.strptime(birthDate, '%b/%d/%Y').date()  # To change the data type of birthDate to data.
    age_in_years = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))  # To calculate age in years.
    age_in_months = today.month - birthDate.month + ((birthDate.month, birthDate.day) > (today.month, today.day)) * 12 - (birthDate.day > today.day) # To calculate age in months.
    # Note: we use (months_with_30_days) list and 'Feb' to calculate the exact day of the birth of the user.
    if birthDate.strftime('%h') in months_with_30_days:
        age_in_days = today.day - birthDate.day + (birthDate.day > today.day) * 30
    elif birthDate.strftime('%h') == 'Feb':
        age_in_days = today.day - birthDate.day + (birthDate.day > today.day) * 28
    else:
        age_in_days = today.day - birthDate.day + (birthDate.day > today.day) * 31
    # Note: if the age of the user is less than one year, then the calculator will return user's age in months.
    # else if the age of the user is less than one month, then the calculator will return user's age in days.
    if birthDate < today:
        return f'Years: {age_in_years}, Months: {age_in_months}, Days: {age_in_days}'
    else:
        # if the user has not entered an older date.
        return 'ERROR! older dates only'
class AgeCalculator:
    # defining the variables.
    def __init__(self):
        # All variables are secured and cannot be changed.
        self.__today = date.today() # This variable stores current date.
        self.__bg = 'light gray' # background color.
        self.__fg = 'blue' # font color.
        self.__catalogue = (
            # The catalogue of the app.
    'Creators:',
    '   -سالم الرحيمان 2230001023.',
    '   -علي عبدالله الزهراني 2230007267.',
    '   -عبدالرحمن الزهراني 2230003733.',
    '   -سعود الدليجان 2230003025.',
    '   -ناصر سالم الخالدي 2230002041.',
    '   -فيصل احمد العمهوج 2230001991.',
    '',
    'Discription:',
    "This app calculates user's age by selecting the birth_date.",
    "The user must enter a date that older than current date.",
    '',
    'App features:',
    "This app calculates user's age in years, months, and days.",
    '',
    'How to use:',
    '   -Select your birth date in the Comboboxes, and then, press Calculate button.',
    '   -The result will be printed in the result box above the Comboboxes.',
    '   -You can erase the result by pressing Erase button.',
    '   -If you select the current date or a future date, ',
    '    then the calculator will return ERROR messege.',
    '   -This calculator calculates ages in years, months, and days.',
    '',
    '©2023-2024, AGE CALCULATOR™. Made in KSA.'
            )
    def run(self):
        # This method is to run the app.
        def erase():
            # To Erase the result box content.
            result_box.config(state='normal') # Change the result box state to normal.
            result_box.delete(0, END) # Erase old data.
            result_box.config(state='readonly') # reChange the result box state to readonly.

        def calculate():
            # To calculate user's age.
            birthDate = f'{month_cb.get()}/{day_cb.get()}/{year_cb.get()}' # Storing the birth_date
            age = ageCalculator(birthDate).strip() # Storing the result and deleting the spaces around the result.
            # The result box state will be changed to normal for inserting the result, and then, the result box state will be changed to readonly.
            result_box.config(state='normal') # Make the result box writable.
            result_box.delete(0, END) # Erase old content.
            result_box.insert(0, age) # Insert the result into the result box.
            result_box.config(state='readonly') # Make the result box unwritable again.

        def new_window():
            # To open the creators names window.
            catalogue = Tk()  # The start of the window.
            catalogue['bg'] = self.__bg  # Changing window background color.
            catalogue.title('Catalogue (Age Calculator)')  # The title of the app.
            catalogue.resizable(False, False)  # The window cannot be resized.
            catalogue.geometry('440x240')  # The size of the window.
            scrollbar = Scrollbar(catalogue)  # The scrollbar of the listbox.
            scrollbar.grid(row=1, column=1, sticky=NS)  # The location of the scrollbar, and the scrollbar is in the right of the listbox.
            creators_label = Label(catalogue, text='Catalogue', font=('Arial', 20), bg=self.__bg, fg=self.__fg)  # Displayed in the top of the listbox.
            creators_label.grid(row=0, column=0)  # The location of the creators_label.
            creators_list = Listbox(catalogue, yscrollcommand=scrollbar.set, width=70)  # The listbox of the creators.
            for name in self.__catalogue[::-1]:
                # This loop is for inserting the names into the creators_list.
                creators_list.insert(0, name)
            creators_list.grid(row=1, column=0)  # The location of the creators_list.
            scrollbar.config(command=creators_list.yview)  # To make the creators_list scrollable vertically.
            button_exit2 = Button(catalogue, text='Close', fg='white', bg='gray', font=('Arial', 10), command=catalogue.destroy)  # This button is to close the window.
            button_exit2.grid(row=2, column=0, sticky=E+W)  # The location of this button.
            catalogue.mainloop()  # The end of the window.

        def update_days_cb(event): # One positional argument is required to run the function.
            # This function is to update (days_cb) Combobox days to be in the range of the (month_cb) Combobox months.
            months_with_30_days = ('Apr', 'Jun', 'Sep', 'Nov') # The list of all months that only have 30 days.
            if month_cb.get() == 'Feb':
                # Only February has 28 days.
                day_cb.config(values=[d for d in range(1, 29)]) # The range of day_cb will be from 1 to 28 days.
                if int(day_cb.get()) > 28: # if the user has selected number more than 28.
                    day_cb.set(28) # day_cb set value.
            elif month_cb.get() in months_with_30_days: # if the user has selected month that in months_with_30_days list.
                day_cb.config(values=[d for d in range(1, 31)]) # The range of day_cb will be from 1 to 30 days.
                if int(day_cb.get()) > 30: # if the user has selected number more than 30.
                    day_cb.set(30) # day_cb set value.
            else:
                # if the month has 31 days
                day_cb.config(values=[d for d in range(1, 32)]) # The range of day_cb will be in its default.

        app = Tk()  # The start of the program.
        app.title(f'Age Calculator')  # The title of the app.
        app['bg'] = self.__bg  # The background color of the app.
        app.resizable(False, False)  # The app cannot be resized.

        app.geometry('253x170')  # The size of the app.
        title_label = Label(app, text=f'AGE CALCULATOR\nDate: {self.__today.strftime("%d %h %Y")}', fg=self.__fg, bg=self.__bg, font=('Arial', 20))  # The title of the app.
        title_label.grid(row=0, column=1)  # This title is in the top of the app.

        result_box = Entry(app, font=('Arial', 13), fg=self.__fg, state='readonly', width=27) # To display the result.
        result_box.grid(row=1, column=1)  # The location of the box.

        # years Combobox.
        selected_year = tk.StringVar()
        year_cb = ttk.Combobox(app, textvariable=selected_year, width=10, values=[y for y in range(date.today().year, 1828, -1)])
        year_cb['state'] = 'readonly'
        year_cb.set(date.today().year) # Setting current year number.
        year_cb.grid(row=2, column=1, sticky=W)

        # months Combobox.
        selected_month = tk.StringVar()
        month_cb = ttk.Combobox(app, textvariable=selected_month, width=11, values=[month_name[m][0:3] for m in range(1, 13)])
        month_cb['state'] = 'readonly'
        month_cb.set(date.today().strftime('%h')) # Setting current month name.
        month_cb.grid(row=2, column=1)

        # days Combobox.
        selected_day = tk.StringVar()
        day_cb = ttk.Combobox(app, textvariable=selected_day, width=10, values=[d for d in range(1, 32)])
        day_cb['state'] = 'readonly'
        day_cb.set(date.today().day) # Setting current day number.
        day_cb.grid(row=2, column=1, sticky=E)

        # To make an action happen by selecting value in (month_cb) Combobox.
        month_cb.bind('<<ComboboxSelected>>', update_days_cb)

        button_calculate = Button(app, text='Calculate', fg='black', bg='orange', font=('Arial', 10), width=9, command=calculate)  # This button calculates the age of the user.
        button_calculate.grid(row=8, column=1, sticky=N+E)  # The location of the button.

        button_erase = Button(app, text='Erase', fg='white', bg='gray', font=('Arial', 10), width=10, command=erase)  # This button erases the content of the result box.
        button_erase.grid(row=8, column=1, sticky=N)  # The location of the button.

        button_creators = Button(app, text='Catalogue', fg='white', bg='gray', font=('Arial', 10), width=9, command=new_window)  # This button opens a new window that displays the creators of this app.
        button_creators.grid(row=8, column=1, sticky=N+W)  # The location of the button.

        button_exit = Button(app, text='Exit', fg='white', bg='gray', font=('Arial', 10), command=exit)  # This button closes the program and it's windows.
        button_exit.grid(row=9, column=1, sticky=E+W)  # The location of the button.

        app.mainloop()  # The end of the application.

# running the application..
my_age = AgeCalculator()
my_age.run()