import os
import time
import random

# Function to clear the terminal screen
def clear():
    os.system('clear')

# Function to print with random colors
def print_random_color(text):
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m", "\033[97m"]
    print(random.choice(colors) + text + "\033[0m")

# Create an animated background with colorful text
def prank_animation():
    clear()
    background_colors = ["\033[41m", "\033[42m", "\033[43m", "\033[44m", "\033[45m", "\033[46m", "\033[47m"]
    texts = [
        "Error! Something went wrong.",
        "Access Denied!",
        "Please Wait...",
        "System Overload!",
        "Your files are being processed...",
        "Warning: High CPU usage detected.",
        "Virus detected: Quarantine initiated!"
    ]
    
    while True:
        for color in background_colors:
            clear()
            os.system(f"echo -e {color} ")
            for text in texts:
                print_random_color(text)
            time.sleep(0.3)

# Run the prank animation
prank_animation()
