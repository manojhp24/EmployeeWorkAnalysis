import customtkinter as ctk

class HomeView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(self, text="🏠 Home Page", font=("Arial", 24, "bold")).pack(pady=30)

        ctk.CTkLabel(self, text="Welcome to the Dashboard", font=("Arial", 16)).pack(pady=10)

        stats_frame = ctk.CTkFrame(self)
        stats_frame.pack(pady=20, padx=20)

        ctk.CTkLabel(stats_frame, text="Total Employees: 100", font=("Arial", 14)).grid(row=0, column=0, padx=20, pady=10)
        ctk.CTkLabel(stats_frame, text="Pending Reports: 5", font=("Arial", 14)).grid(row=0, column=1, padx=20, pady=10)
