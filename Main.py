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

    
  
  
    
 
  





  
        
    
  
  
    
