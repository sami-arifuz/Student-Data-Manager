
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

# List to store student data
student = []

def add_student(name, mark):
  if not name or not isinstance(name, str):
    raise ValueError("Invalid name.")
  if not isinstance(mark, (int, float)) or mark < 0 or mark > 100:
    raise ValueError("Mark should be between 0 and 100.")
  students.append({'name': name.strip(), 'mark': mark})

def search_student(name):
  return [s for s in students if name.lower() in s['name'].lower()]

def sort_students_by_marks():
  students.sort(key=lambda x: x['mark'], reverse=True)

def visualize_marks():
  if not students:
    messagebox.showinfo("Info", "No data to visualize.")
    return
  names = [s['name'] for s in students]
  marks = [s['mark'] for s in students]
  
  plt.figure(figsize=(10, 6))
  plt.bar(names, marks, color='skyblue')
  plt.xlabel('Students')
  plt.ylabel('Marks')
  plt.title('Student Marks Visualization')
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()

# GUI CODE

root = tk.tk()
root.title("Student Data Manager")
root.geometry("450x500")
root.config(bg="#f5f5f5")

font_style = ("Helvetica", 12)
button_style = {'width': 20, 'height': 2, 'bg': '#4CAF50', 'fg': 'white', 'font': font_style, 'bd': 0, 'relief': 'solid'}
label_style = {'font': ("Arial", 14), 'bg': '#f5f5f5'}

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

def handle_search():
  name = simpledialog.askstring("Search", "Enter name to search:")
  if name:
    results = search_student(name)
        if results:
            msg = "\n".join(f"{s['name']} - {s['mark']}" for s in results)
            messagebox.showinfo("Results", msg)
        else:
            messagebox.showinfo("Results", "No matching students found.")

def handle_sort():
  sort_students_by_marks()
  if students:
    msg = "\n".join(f"{s['name']} - {s['mark']}" for s in students)
    messagebox.showinfo("Sorted", msg)
  else:
    messagebox.showinfo("Sorted", "No students to sort.")

#Inputs 

tk.Label(root, text="Student Name:", **label_style).pack(pady=10)
name_entry = tk.Entry(root, font=font_style)
name_entry.pack()

tk.Label(root, text="Mark (0-100):", **label_style).pack(pady=10)
mark_entry = tk.Entry(root, font=font_style)
mark_entry.pack()

# Buttons
tk.Button(root, text="Add Student", command=handle_add, **button_style).pack(pady=10)
tk.Button(root, text="Search Student", command=handle_search, **button_style).pack(pady=5)
tk.Button(root, text="Sort Students", command=handle_sort, **button_style).pack(pady=5)
tk.Button(root, text="Show Chart", command=visualize_marks, **button_style).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, **button_style).pack(pady=20)

# Start the GUI loop
root.mainloop()






    
    
  
  

    
  
  
    
 
  





  
        
    
  
  
    
