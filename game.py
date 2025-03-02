import tkinter as tk
from PIL import Image, ImageTk
import random

class TheForgottenForest:
    def __init__(self, root):
        self.root = root
        self.root.title("The Forgotten Forest")
        self.root.attributes('-fullscreen', True)  # Enable fullscreen
        self.root.configure(bg="black")

        self.text = tk.StringVar()
        self.text.set(
            "You awaken in the Forgotten Forest, your past a shattered dream.\n"
            "A whisper calls to you: 'Heir of Eldoria… The time has come.'\n"
            "Memories flicker—the Celestial Stone, a lost kingdom, a looming darkness.\n"
            "You must find the truth before the forest claims you."
        )

        # Load the background image using PIL
        image = Image.open("forest.png")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        image = image.resize((screen_width, screen_height))
        self.bg_image = ImageTk.PhotoImage(image)

        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        self.label = tk.Label(root, textvariable=self.text, wraplength=screen_width * 0.7, justify="center",
                              font=("Georgia", 16), fg="white", bg="black")
        self.label.pack(pady=50)

        self.button1 = tk.Button(root, text="Follow the whispers", command=self.follow_whispers,
                                 font=("Georgia", 14), width=25, bg="darkgreen", fg="white")
        self.button2 = tk.Button(root, text="Search the ruins", command=self.search_ruins,
                                 font=("Georgia", 14), width=25, bg="darkblue", fg="white")

        self.button1.pack(side="left", padx=100, pady=20)
        self.button2.pack(side="right", padx=100, pady=20)

        # Exit fullscreen with ESC key
        self.root.bind("<Escape>", self.exit_fullscreen)

    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)

    def follow_whispers(self):
        self.text.set("The whispers guide you to an ancient tree marked with glowing runes. "
                      "A silver wolf with golden eyes blocks your path.")
        self.update_buttons("Speak to the wolf", self.speak_to_wolf, "Try to sneak past", self.sneak_past_wolf)

    def search_ruins(self):
        self.text.set("You stumble upon crumbling ruins. An eerie light glows from an altar at the center. "
                      "A shadow moves behind you.")
        self.update_buttons("Investigate the altar", self.touch_crystal, "Turn and face the shadow", self.face_shadow)

    def speak_to_wolf(self):
        self.text.set("The wolf's voice echoes in your mind: 'Only the worthy may pass.'\n"
                      "'Who are you, child of Eldoria?'")
        self.update_buttons("I am the lost heir", self.claim_heir, "I do not know", self.admit_lost)

    def sneak_past_wolf(self):
        if random.choice([True, False]):
            self.text.set("You slip past, but the forest twists around you. A shadowy figure emerges.")
            self.update_buttons("Run", self.run_away, "Confront the figure", self.confront_shadow)
        else:
            self.text.set("The wolf growls, and the trees close in. You are lost forever. Game Over.")
            self.end_game()

    def claim_heir(self):
        self.text.set("The wolf bows. 'Then prove it. The Celestial Stone awaits.'\n"
                      "A path opens before you.")
        self.update_buttons("Follow the path", self.follow_path, "Ask about the stone", self.ask_about_stone)

    def admit_lost(self):
        self.text.set("The wolf sighs. 'Then you must remember. The forest will test you.'\n"
                      "The path splits into darkness and light.")
        self.update_buttons("Take the dark path", self.dark_path, "Take the light path", self.light_path)

    def touch_crystal(self):
        if random.choice([True, False]):
            self.text.set("A surge of memories returns. You see your family, the fall of Eldoria…\n"
                          "The prophecy is real. The kingdom needs you.")
            self.update_buttons("Embrace your destiny", self.embrace_destiny, "Seek more answers", self.seek_knowledge)
        else:
            self.text.set("The crystal cracks, releasing a dark force. The ruins crumble. Game Over.")
            self.end_game()

    def face_shadow(self):
        self.text.set("A cloaked figure steps forward. 'You seek the Celestial Stone, yet you do not know its power.'\n"
                      "Do you trust them?")
        self.update_buttons("Trust them", self.trust_shadow, "Doubt them", self.doubt_shadow)

    def follow_path(self):
        self.text.set("The path leads to an ancient chamber. The Celestial Stone glows, waiting for you.")
        self.update_buttons("Touch the stone", self.touch_stone, "Kneel before it", self.kneel_stone)

    def ask_about_stone(self):
        self.text.set("The wolf whispers: 'The stone grants power, but power has a price.'\n"
                      "'Will you wield it wisely?'")
        self.update_buttons("I will", self.follow_path, "I am uncertain", self.doubt_path)

    def dark_path(self):
        self.text.set("The path is cold and twisted. You hear voices whispering forbidden secrets.")
        self.update_buttons("Embrace the darkness", self.embrace_darkness, "Turn back", self.follow_path)

    def light_path(self):
        self.text.set("A golden light surrounds you. A vision of Eldoria appears, calling you home.")
        self.update_buttons("Step forward", self.follow_path, "Resist the vision", self.doubt_path)

    def embrace_destiny(self):
        self.text.set("You place your hand on the Celestial Stone. Light floods your mind. Eldoria is reborn.")
        self.end_game()

    def seek_knowledge(self):
        self.text.set("A hidden library appears. Within, you learn the truth: The stone does not restore—it chooses.")
        self.end_game()

    def trust_shadow(self):
        self.text.set("The figure removes their hood. It is the last Guardian of Eldoria. 'You are the kingdom’s last hope.'")
        self.update_buttons("Accept your role", self.embrace_destiny, "Refuse", self.doubt_path)

    def doubt_shadow(self):
        self.text.set("The figure vanishes. The ruins collapse. You hesitated… and the chance is lost. Game Over.")
        self.end_game()

    def touch_stone(self):
        self.text.set("A powerful force fills you. You are the rightful ruler of Eldoria.")
        self.end_game()

    def kneel_stone(self):
        self.text.set("The stone shimmers. 'A ruler who bows is one who understands power.' You are ready.")
        self.end_game()

    def update_buttons(self, text1, command1, text2, command2):
        self.button1.config(text=text1, command=command1)
        self.button2.config(text=text2, command=command2)

    def end_game(self):
        self.button1.pack_forget()
        self.button2.pack_forget()
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Georgia", 14), bg="red", fg="white")
        self.exit_button.pack(pady=20)

root = tk.Tk()
game = TheForgottenForest(root)
root.mainloop()