import os
from gtts import gTTS
import tkinter as tk
from tkinter import messagebox

def convert_to_speech():
    text = text_entry.get("1.0", "end-1c").strip()
    if not text:
        messagebox.showerror("Error", "Please enter some text.")
        return
    
    try:
        sound = gTTS(text, lang='en-US')
        sound.save("output.mp3")
        os.system("afplay output.mp3 &")  # On Mac
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create main window
window = tk.Tk()
window.title("Text-to-Speech Converter")

# Create text entry
text_entry = tk.Text(window, height=10, width=50)
text_entry.pack(pady=10)

# Create button to convert text to speech
convert_button = tk.Button(window, text="Convert to Speech", command=convert_to_speech)
convert_button.pack()

# Run the GUI
window.mainloop()
