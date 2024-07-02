import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json

class TextRPG:
    def __init__(self, root):
        self.root = root
        self.root.title("Escape From Ruin")
        self.load_game_data()
        self.load_images()
        self.create_widgets()
        self.display_scenario('home')

    def load_game_data(self):
        with open('game_data.json', 'r') as file:
            self.game_data = json.load(file)

    def load_images(self):
        try:
            image = Image.open("game-image.png")
            resized_image = image.resize((300, 300), Image.ANTIALIAS)
            self.game_image = ImageTk.PhotoImage(resized_image)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")
            self.game_image = None

    def create_widgets(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        self.image_frame = tk.Frame(self.main_frame)
        self.image_frame.pack(side="left", padx=10)
        if self.game_image:
            self.image_label = tk.Label(self.image_frame, image=self.game_image)
            self.image_label.pack()

        self.text_button_frame = tk.Frame(self.main_frame, bd=1, relief="groove")
        self.text_button_frame.pack(side="left", fill="both", expand=True)

        self.text = tk.Label(self.text_button_frame, wraplength=250)
        self.text.pack()

        self.button_frame = tk.Frame(self.text_button_frame)
        self.button_frame.pack(fill="x")

    def display_scenario(self, scenario_key):
        scenario = self.game_data[scenario_key]
        self.text.config(text=scenario['text'])
        # Clear existing buttons
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        for option_key, option_text in scenario.get('options', {}).items():
            button = tk.Button(self.button_frame, text=option_text,
                               command=lambda key=option_key: self.process_choice(scenario_key, key))
            button.pack(fill='x')

    def process_choice(self, current_scenario, choice):
        next_scenario = self.game_data[current_scenario]['next'][choice]
        if next_scenario == 'exit':
            self.end_game()
        else:
            self.display_scenario(next_scenario)

    def end_game(self):
        self.text.config(text="Thank you for playing!")
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        exit_button = tk.Button(self.button_frame, text="Exit", command=self.root.quit)
        exit_button.pack(fill='x')

def main():
    root = tk.Tk()
    app = TextRPG(root)
    root.mainloop()

if __name__ == "__main__":
    main()
