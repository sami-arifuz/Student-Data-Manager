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


  
        
    
  
  
    
