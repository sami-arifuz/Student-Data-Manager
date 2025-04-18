
#This part of the code is responsible for importing the needed libraries that make the app work. 
#First, the line import tkinter as tk brings in the Tkinter library, which is the standard GUI (Graphical User Interface) toolkit in Python. 
#The second line, from tkinter import messagebox, imports a specific module from Tkinter that allows the program to display pop-up messages to the user.
#This is used for showing alerts, confirmations, or information messages.
#The next line, from tkinter import simpledialog, is used to create input dialogs that ask the user for information, like a name or number, through a simple pop-up window.
#Lastly, import matplotlib.pyplot as plt brings in the matplotlib.pyplot module, which is a powerful plotting library used to create visualizations such as bar charts and line graphs.

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import matplotlib.pyplot as plt 

#This part of the code is where the app starts keeping track of all the students and their marks. 
#It first creates an empty list called students, which will store each student's information as a small dictionary (with their name and mark). 
#Then there's a function called add_student(name, mark) that is used to add a student to the list. 
#But before doing that, the function checks if the inputs are okay. It checks if the name is not empty and is actually a string (not a number or something else). 
#If the name is invalid, it raises a ValueError with a message saying "Invalid name."
#After that, it checks the mark to make sure it's a number (either an integer or float), and that it's between 0 and 100. 
#If the mark doesn't follow these rules, it raises another ValueError that says "Mark should be between 0 and 100."
#Once the name and mark are confirmed to be okay, it adds them to the list. 
#It also uses .strip() on the name, which removes any extra spaces at the beginning or end.

student = []

def add_student(name, mark):
  if not name or not isinstance(name, str):
    raise ValueError("Invalid name.")
  if not isinstance(mark, (int, float)) or mark < 0 or mark > 100:
    raise ValueError("Mark should be between 0 and 100.")
  students.append({'name': name.strip(), 'mark': mark})

#This function is used to search for a student by name from the list of students. 
#It's called search_student(name), and it takes one input: the name you're looking for. 
#Inside the function, it goes through the students list and looks for any student whose name contains the same input, 
#ignoring whether it's upper or lowercase  using .lower().

def search_student(name):
  return [s for s in students if name.lower() in s['name'].lower()]

#This function is used to sort all the students based on their marks, from highest to lowest. 
#It's called sort_students_by_marks(), and it doesn’t require any input because it works directly with the students list that’s already in the code. 
#Inside the function, it uses the .sort() method, which arranges the items in the list. 
#The part key=lambda x: x['mark'] tells Python to look at the 'mark' value inside each student’s data when sorting. 
#The reverse=True part means it will sort in descending order, so the student with the highest mark will appear first in the list. 

def sort_students_by_marks():
  students.sort(key=lambda x: x['mark'], reverse=True)

#This function is called visualize_marks(), and it’s used to show a bar graph of all the students and their marks. 
#First, it checks if the students list is empty by using if not students: 
#If there are no students added yet, it pops up a message box that says “No data to visualize” and then stops the function using return. 
#If there is data, it creates two separate lists: names and marks. 
#The names list collects all the student names, and the marks list collects their corresponding marks. 
#These two lists are later used to plot the bar graph, with names on the x-axis and marks on the y-axis.

def visualize_marks():
  if not students:
    messagebox.showinfo("Info", "No data to visualize.")
    return
  names = [s['name'] for s in students]
  marks = [s['mark'] for s in students]

#This code creates and shows a bar graph of student marks. 
#It sets the graph size, draws the bars using student names and marks, and colors them light blue. 
#Labels are added to the x and y axes, and the title is set as "Student Marks Visualization." 
#The student names on the x-axis are rotated for better readability. Finally, the graph is displayed using plt.show().
  
  plt.figure(figsize=(10, 6))
  plt.bar(names, marks, color='skyblue')
  plt.xlabel('Students')
  plt.ylabel('Marks')
  plt.title('Student Marks Visualization')
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()

#This part of the code sets up the main GUI window using Tkinter. 
#It starts by creating a window (root = tk.Tk()) and gives it a title and size. 
#The background color is set to light gray. Then, it defines a custom font style and creates styles for buttons and labels.

root = tk.tk()
root.title("Student Data Manager")
root.geometry("450x500")
root.config(bg="#f5f5f5")

font_style = ("Helvetica", 12)
button_style = {'width': 20, 'height': 2, 'bg': '#4CAF50', 'fg': 'white', 'font': font_style, 'bd': 0, 'relief': 'solid'}
label_style = {'font': ("Arial", 14), 'bg': '#f5f5f5'}

#This function is works when the user clicks the “Add Student” button in the app. 
#It first gets the name and mark from the user in the  input fields. 
#Then it converts the mark into a number and uses the add_student() function to save the data. 
#If everything is fine, it shows a success message and clears the input fields. 
#If something is wrong, like the name is empty or the mark is not a valid number from 1- 100, it shows an error message using messagebox. 

def handle_add():
  try:
    name = name_entry.get()
    mark = float(mark_entry.get())
    add_student(name, mark)
    messagebox.showinfo("Success", f"Added {name} with {mark} marks.")
    name_entry.delete(0, tk.END)
    mark_entry.delete(0, tk.END)
  except ValueError as ve:
    messagebox.showerror("Input Error", str(ve))
  except Exception as e:
    messagebox.showerror("Error", str(e))

#This function runs when the user clicks the “Search Student” button. 
#It opens a small input box asking the user to type a name. 
#When the user types a name, the function looks for students whose names match. 
#When match found, it shows their names and marks in a pop-up message. 
#If no matches are found, it shows a message saying "No matching students found." 

def handle_search():
  name = simpledialog.askstring("Search", "Enter name to search:")
  if name:
    results = search_student(name)
        if results:
            msg = "\n".join(f"{s['name']} - {s['mark']}" for s in results)
            messagebox.showinfo("Results", msg)
        else:
            messagebox.showinfo("Results", "No matching students found.")

#This function is called when the user clicks the “Sort by Marks” button. 
#It sorts all the students in the list from highest to lowest marks using the sort_students_by_marks() function. 
#If there are students in the list, it shows their names and marks in sorted order in a pop-up window. 
#If the list is empty, it shows a message saying there's nothing to sort.

def handle_sort():
  sort_students_by_marks()
  if students:
    msg = "\n".join(f"{s['name']} - {s['mark']}" for s in students)
    messagebox.showinfo("Sorted", msg)
  else:
    messagebox.showinfo("Sorted", "No students to sort.")

#This part of the code creates the input section of the app. 
#It first adds a label that says “Student Name:” and an entry box for typing the name. 
#Then creates another label  called “Mark (0-100):” with an entry box for the user to type the student’s mark. 
#This allows users to enter the students data, and the labels help make everything  easy to understand which box is for what entry. 

tk.Label(root, text="Student Name:", **label_style).pack(pady=10)
name_entry = tk.Entry(root, font=font_style)
name_entry.pack()

tk.Label(root, text="Mark (0-100):", **label_style).pack(pady=10)
mark_entry = tk.Entry(root, font=font_style)
mark_entry.pack()

#This section of the code creates all the buttons in the app, each one made for a specific action. 
#The “Add Student” button allows users to add a new student to the list. 
#The “Search Student” button opens a dialog box where users can type a name to find matching students. 
#The “Sort Students” button arranges the student list from highest to lowest marks. 
#The “Show Chart” button displays a bar graph of all the students and their marks. 
#The “Exit” button safely closes the app. 

tk.Button(root, text="Add Student", command=handle_add, **button_style).pack(pady=10)
tk.Button(root, text="Search Student", command=handle_search, **button_style).pack(pady=5)
tk.Button(root, text="Sort Students", command=handle_sort, **button_style).pack(pady=5)
tk.Button(root, text="Show Chart", command=visualize_marks, **button_style).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, **button_style).pack(pady=20)

# Start the GUI loop
root.mainloop()






    
    
  
  

    
  
  
    
 
  





  
        
    
  
  
    
