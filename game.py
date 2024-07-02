import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  

class TextRPG:
    def __init__(self, root):
        self.root = root
        self.root.title("Escape From Ruin")
        self.load_images()
        self.create_widgets()

    def load_images(self):
        try:
            # Load the image
            image = Image.open("game-image.png")
            # Resize the image
            resized_image = image.resize((300, 300), Image.ANTIALIAS)  # Example size: 300x300
            self.game_image = ImageTk.PhotoImage(resized_image)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")
            self.game_image = None

    def create_widgets(self):
        # Main layout frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        # Frame for the image
        self.image_frame = tk.Frame(self.main_frame)
        self.image_frame.pack(side="left", padx=10)

        if self.game_image:
            self.image_label = tk.Label(self.image_frame, image=self.game_image)
            self.image_label.pack()

        # Frame for the text and buttons
        self.text_button_frame = tk.Frame(self.main_frame)
        self.text_button_frame.pack(side="left", fill="both", expand=True)

        # Text above the buttons
        self.text = tk.Label(self.text_button_frame, text="Your plane has crashed and you are the only survivor. "
                                                         "You are in a dense jungle. Choose your path wisely to survive.",
                             wraplength=250)  # Adjust wraplength to fit the width you want for the text
        self.text.pack()

        # Buttons
        self.button_frame = tk.Frame(self.text_button_frame)
        self.button_frame.pack(fill="x")

        self.button_a = tk.Button(self.button_frame, text="A: Look for supplies",
                                  command=lambda: self.process_choice('A'))
        self.button_a.pack(fill='x')

        self.button_b = tk.Button(self.button_frame, text="B: Get out of seat and go towards the back exit",
                                  command=lambda: self.process_choice('B'))
        self.button_b.pack(fill='x')

        self.button_c = tk.Button(self.button_frame, text="C: Go to the closer exit in front of me",
                                  command=lambda: self.process_choice('C'))
        self.button_c.pack(fill='x')

    def process_choice(self, choice):
        if choice == 'A':
            self.update_scenario("You look for supplies and find a survival kit.")
        elif choice == 'B':
            self.update_scenario("Moving towards the back, you find an emergency exit.")
        elif choice == 'C':
            self.update_scenario("You head to the front exit and see a path leading into the jungle.")

    def update_scenario(self, scenario):
        self.text.config(text=scenario)
        self.button_a.pack_forget()
        self.button_b.pack_forget()
        self.button_c.pack_forget()

        self.continue_button = tk.Button(self.button_frame, text="Continue", command=self.end_game)
        self.continue_button.pack(fill='x')

    def end_game(self):
        messagebox.showinfo("End", "Thank you for playing!")
        self.root.quit()

def main():
    root = tk.Tk()
    app = TextRPG(root)
    root.mainloop()

if __name__ == "__main__":
    main()
