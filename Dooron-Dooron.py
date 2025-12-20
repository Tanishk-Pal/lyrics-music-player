import tkinter as tk
import time
import pygame
import threading

# --- Lyrics ---
lyrics = [
    "Sochu ke milni te bolaanga ki",
    "Teri taan gallaach... shaayari",
    "Vekhegi mainu te sochegi kya tu",
    "Mitti da banda main, tu taan pari...",
    "Ishqe di galitach, khoya e dil ve",
    "Aas Lagaaye Ki",
    "Jaaye Tu Mil Ve",
    "Kol tere mainu",
    "aan de soni",
    "Karaan main kitne jatan O soni",
    "Dooron dooron main..."
]

delays = [1.0, 1.8, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.8, 5.35, 3.0]

# --- Music Setup ---
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\win\Downloads\Dooron.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_pos(171)  # skip intro humming

# --- GUI Setup ---
root = tk.Tk()
root.title("✨ Dooron Dooron Lyrics ✨")

window_width = 700
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_offset = (screen_width // 2) - (window_width // 2) + 170  
y_offset = (screen_height // 2) - (window_height // 2) - 100 

root.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")
root.configure(bg="#0f0f0f")  # dark aesthetic background

label = tk.Label(root, text="", font=("Courier New", 20, "bold"), fg="#00ffcc", bg="#0f0f0f")
label.pack(expand=True)

# --- Typing Effect ---
def show_lyrics():
    time.sleep(1.4)
    for i, line in enumerate(lyrics):
        text = ""
        for char in line:
            text += char
            label.config(text=text)
            root.update()
            time.sleep(0.06)
        time.sleep(delays[i])
    pygame.mixer.music.fadeout(2000)  # smooth fade out after lyrics

    # Show developer credit with animation
    show_developer()

# --- Developer Animation ---
def show_developer():
    dev_text = "Developer = Tanx"
    label.config(text="", font=("Helvetica", 26, "bold"), fg="#FFD700", bg="#0f0f0f")  # gold color

    # Typing fade-in effect
    text = ""
    for char in dev_text:
        text += char
        label.config(text=text)
        root.update()
        time.sleep(0.12)

    # Subtle pulse animation (size grows/shrinks)
    def pulse():
        sizes = [26, 28, 26, 24]
        i = 0
        while True:
            label.config(font=("Helvetica", sizes[i % len(sizes)], "bold"))
            root.update()
            time.sleep(0.4)
            i += 1
    threading.Thread(target=pulse, daemon=True).start()

# Run lyrics in a separate thread so GUI stays responsive
threading.Thread(target=show_lyrics).start()

root.mainloop()

# --- Stop music after lyrics duration ---
total_duration = 1.2 + sum(len(line) * 0.06 + delays[i] for i, line in enumerate(lyrics))
time.sleep(total_duration)
pygame.mixer.music.stop()
