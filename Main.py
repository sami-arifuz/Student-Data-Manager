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


  
        
    
  
  
    
