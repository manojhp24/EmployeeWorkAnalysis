import customtkinter as ctk
from view.dashboard import Dashboard

def run_app():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Employee Analysis Dashboard")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    width = int(screen_width * 0.85)
    height = int(screen_height * 0.8)

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")

    Dashboard(root)
    root.mainloop()
