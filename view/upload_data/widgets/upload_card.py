import customtkinter as ctk


def create_upload_card(title, parent, browse_callback=None):
    card = ctk.CTkFrame(
        parent,
        fg_color="#1E1E2E",
        corner_radius=12,
        border_color="#3F3F46",
        border_width=1
    )

    ctk.CTkLabel(card, text=f"{title}:", font=("Lato", 14)).grid(row=0, column=0, padx=10, pady=10, sticky='w')
    path_label = ctk.CTkLabel(card, text="No file selected", font=("Lato", 12), text_color="#888")
    path_label.grid(row=0, column=1, padx=10, pady=10, sticky='w')

    ctk.CTkButton(card, text="Browse", width=100, command=browse_callback).grid(row=0, column=2, padx=10, pady=10)

    def on_browse():
        file_path = browse_callback()
        if file_path:
            path_label.configure(text=file_path)

    ctk.CTkButton(card, text="Browse", width=100, command=on_browse).grid(row=0, column=2, padx=10, pady=10)

    return card
