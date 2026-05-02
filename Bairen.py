import sys
sys.stdout.reconfigure(encoding='utf-8')

import time
import pygame

# ---------------- LYRICS ----------------
lyrics = [
    "Haa manne sambh-sambh rakhe tere jhanjhara ke jode ✨",
    "Meri gall ro-ro ye bhi chhori bawle se hore 💔",
    "Manne aaye jaave khyaal tere khayal jaave khyaal tere 🌙",
    "Jeene koni deti naye bairi tanhayi manne 🥀",
    "Geeta mein gayi kade chhaati ke lagayi manne 🎶",
    "Jad bhi gaya re teri yaad khadi payi manne ⏳",
    "Sambh sambh rakhi bahut chhaati ke lagayi manne 💔",
    "💔 Jad bhi gaya re teri yaad khadi payi manne ❤️"
]

# EXACT timing (seconds after lyrics start)
timestamps = [1, 3, 7, 11, 15, 18, 20, 24]

# ---------------- SMART TYPE FUNCTION ----------------
def type_line(line, duration):
    # avoid division error
    if len(line) == 0:
        return

    # dynamic speed based on available time
    speed = duration / len(line)

    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

    print()

# ---------------- MUSIC SETUP ----------------
pygame.mixer.init()

song_path = r"C:\Users\win\Downloads\Bairan.mp3"
pygame.mixer.music.load(song_path)

# Start music
pygame.mixer.music.play()
pygame.mixer.music.set_pos(0)

# small buffer for stability
time.sleep(1)

# ---------------- SYNCED LYRICS ----------------
start_time = time.time()

print("\n--- Starting Lyrics ---\n")

for i, line in enumerate(lyrics):

    # wait until correct timestamp
    while time.time() - start_time < timestamps[i]:
        time.sleep(0.005)

    # calculate duration until next line
    if i < len(timestamps) - 1:
        line_duration = timestamps[i+1] - timestamps[i]
    else:
        line_duration = 4  # last line fallback

    # type with smart speed
    type_line(line, line_duration)

# ---------------- CLEAN EXIT ----------------
while pygame.mixer.music.get_busy():
    time.sleep(1)

pygame.mixer.music.stop()
pygame.quit()