import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2
import os
from PIL import Image, ImageTk
import webbrowser

def play_video(video_path):
    if video_path.startswith("http"):
        webbrowser.open(video_path)
    else:
        cap = cv2.VideoCapture(video_path)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Video', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

def open_file():
    file_path = filedialog.askopenfilename()
    video_entry.delete(0, tk.END)
    video_entry.insert(0, file_path)

def play_video_click():
    video_path = video_entry.get()
    if video_path:
        play_video(video_path)
    else:
        messagebox.showwarning("Input Error", "Please enter or select a video link.")

def run_volume_control():
    os.system('python volume_control_python.py')

# Set up the main window
root = tk.Tk()
root.title("Volume Controller Using Hand Gesture")
root.geometry("800x600")

# Load and set the background image
bg_image = Image.open("background.png")
bg_image = bg_image.resize((1500, 1000), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

# Welcome text
welcome_text = tk.Label(root, text="Welcome to the Volume Controller", font=("Helvetica", 24), bg="#000000", fg="white")
welcome_text.pack(pady=20)

# Video link entry bar
video_entry = tk.Entry(root, width=50, font=("Helvetica", 14))
video_entry.pack(pady=10)
file_button = tk.Button(root, text="Browse...", command=open_file, bg="sky blue", fg="black", font=("Helvetica", 14))
file_button.pack(pady=5)

# Play button
play_button = tk.Button(root, text="Play Video", command=play_video_click, bg="sky blue", fg="black", font=("Helvetica", 14))
play_button.pack(pady=10)

# Volume control button
volume_control_button = tk.Button(root, text="Control Volume Using Hand Gesture", command=run_volume_control, bg="sky blue", fg="black", font=("Helvetica", 14))
volume_control_button.pack(pady=20)

# Note
note_label = tk.Label(root, text="Use your hand to control your system volume. \nIncreasing the distance between your index finger and thumb will increase the system volume.\nMinimizing the distance between your fingers will decrease the volume.",
                      font=("Helvetica", 12), bg="#000000", fg="white", justify="center")
note_label.pack(pady=20)

root.mainloop()
