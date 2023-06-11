import tkinter
import customtkinter
from PIL import Image, ImageTk
from webscraper import WebScraper


def login(username, password):
    if username and password:
        scraper = WebScraper(username, password)
        scraper.cc_login()


class LoginWindow:

    def __init__(self):

        self.root = customtkinter.CTk()
        self.width, self.height = 600, 400

        self.background_path = "loginimage.jpg"
        self.cc_icon_path = "cc_icon.png"

        self.background_image = None
        self.cc_icon_image = None

        self.setup_root()
        self.setup_background()
        self.setup_login_form()

    def setup_root(self):
        self.root.title("Login")
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False, False)

    def setup_background(self):
        background_img = Image.open(self.background_path)
        background_img = background_img.resize((self.width + 1400, self.height + 200), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(background_img)

        background_label = tkinter.Label(master=self.root, image=self.background_image)
        background_label.pack()

        cc_icon_img = Image.open(self.cc_icon_path)
        cc_icon_img = cc_icon_img.resize((50, 50), Image.ANTIALIAS)
        self.cc_icon_image = ImageTk.PhotoImage(cc_icon_img)

        cc_icon_label = tkinter.Label(master=self.root, image=self.cc_icon_image, bg="#2C2827")
        cc_icon_label.place(x=10, y=10)


    def setup_login_form(self):
        login_frame = customtkinter.CTkFrame(master=self.root, width=350, height=300, corner_radius=15)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

        label = customtkinter.CTkLabel(master=login_frame, text="Clubcooee Login:", font=('Century Gothic', 20))
        label.place(x=85, y=20)

        username_entry = customtkinter.CTkEntry(master=login_frame, width=200, font=('Century Gothic', 15), placeholder_text="Username")
        username_entry.place(x=75, y=100)

        password_entry = customtkinter.CTkEntry(master=login_frame, width=200, font=('Century Gothic', 15), placeholder_text="Password", show="*")
        password_entry.place(x=75, y=150)

        login_button = customtkinter.CTkButton(master=login_frame, text="Login", font=('Century Gothic', 15), width=150, corner_radius=6, command=lambda: login(username_entry.get(),password_entry.get()))
        login_button.place(x=100, y=240)
