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
    
