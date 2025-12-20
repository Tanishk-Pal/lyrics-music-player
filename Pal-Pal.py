import sys
import time
import pygame

def print_lyrics():
    lyrics = [

        "Mein ab kyun hosh may aata nahi?",
        "Sukoon yeh dil kyun paata nahi?",
        "Kyun toruun khud se jo thay waaday",
        "Ke ab yeh ishq nibhaana nahi?",
        "Mein morrun tum se jo yeh chehra",
        "Dobara nazar milana nahi",
        "Yeh duniya jaanay mera dard",
        "Tujhe yeh nazar kyun aata nahi?"
    ]

    delays = [0.3, 0.3, 0.4, 0.3, 0.3, 0.3, 0.8, 0.8]
    
    print("Tanishk Presents: ")
    print("Pal Pal : \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(delays[i])

# --- MUSIC SETUP ---
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\win\Downloads\Pal Pal.mp3")

# Skip intro humming (adjust seconds)
pygame.mixer.music.play()
pygame.mixer.music.set_pos(35)  # jump to where lyrics start

# --- Calculate total lyric duration ---
lyrics = [
    "Mein ab kyun hosh may aata nahi?",
    "Sukoon yeh dil kyun paata nahi?",
    "Kyun toruun khud se jo thay waaday",
    "Ke ab yeh ishq nibhaana nahi?",
    "Mein morrun tum se jo yeh chehra",
    "Dobara nazar milana nahi",
    "Yeh duniya jaanay mera dard",
    "Tujhe yeh nazar kyun aata nahi?"
]
delays = [0.3, 0.3, 0.4, 0.3, 0.3, 0.3, 0.8, 0.8]

typing_speed = 0.06  # seconds per character
total_duration = 1.2 + sum(len(line) * typing_speed + delays[i] for i, line in enumerate(lyrics))

# --- Run lyrics printing ---
print_lyrics()

# --- Stop music after lyrics duration ---
time.sleep(total_duration)
pygame.mixer.music.stop()
pygame.quit()
