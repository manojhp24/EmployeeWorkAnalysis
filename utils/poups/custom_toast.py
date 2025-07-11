import customtkinter as ctk

def show_toast(parent, message, duration=2500):
    toast = ctk.CTkToplevel(parent)
    toast.overrideredirect(True)
    toast.attributes("-topmost", True)

    # Size of the toast
    width = 250
    height = 60

    # Get position of parent window
    parent.update_idletasks()
    x = parent.winfo_rootx() + parent.winfo_width() - width - 20
    y = parent.winfo_rooty() + parent.winfo_height() - height - 20

    # Place toast window
    toast.geometry(f"{width}x{height}+{x}+{y}")

    # Add label inside toast
    label = ctk.CTkLabel(
        toast,
        text=message,
        font=("Arial", 13),
        text_color="white",
        fg_color="#2ecc71",  # green toast
        corner_radius=12
    )
    label.pack(expand=True, fill="both", padx=10, pady=10)

    # Auto-close after duration (ms)
    toast.after(duration, toast.destroy)
