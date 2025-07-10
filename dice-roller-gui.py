# 🎲 Dice Roller using Tkinter with Images by Prince 💛
import tkinter as tk
import random
import time

# 🎲 Emoji Faces for Dice 1 to 6
dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

# 🌈 Function to roll dice with animation
def roll_dice():
    roll_button.config(state='disabled')
    result_label.config(text="Rolling... 🎲")
    window.update()

    for _ in range(10):  # Spin 10 times
        face = random.randint(1, 6)
        dice_label.config(text=dice_faces[face])
        window.update()
        time.sleep(0.1)

    final = random.randint(1, 6)
    dice_label.config(text=dice_faces[final])
    result_label.config(text=f"✅ You rolled a {final}!")
    roll_button.config(state='normal')

# 🪟 GUI Setup
window = tk.Tk()
window.title("🎲 Prince's Dice Roller")
window.geometry("300x300")
window.config(bg="#1e1e1e")

# 🎲 Dice Label
dice_label = tk.Label(window, text="⚀", font=("Segoe UI Emoji", 100), bg="#1e1e1e", fg="white")
dice_label.pack(pady=20)

# 📢 Result Label
result_label = tk.Label(window, text="Tap below to roll!", font=("Segoe UI", 14), fg="white", bg="#1e1e1e")
result_label.pack()

# 🎯 Roll Button
roll_button = tk.Button(window, text="🎲 Roll Dice", font=("Segoe UI", 14, "bold"),
                        bg="#33cc33", fg="white", padx=20, pady=10, command=roll_dice)
roll_button.pack(pady=30)

window.mainloop()

# 🎉 Enjoy rolling the dice! 🎉