import customtkinter as ctk
from tkinter import ttk

from controller.file_controller import FileController
from view.home.home_view import HomeView
from view.upload_data.upload_view import UploadView

class Dashboard(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.file_controller = FileController(lambda: getattr(self,'tree',None))
        self.pack(fill="both", expand=True)
        self.view_cache = {}

        # Configure layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#1E1E2E")
        self.sidebar.grid(row=0, column=0, sticky="ns")

        ctk.CTkLabel(self.sidebar, text="Dashboard", font=("Arial", 18, "bold")).pack(pady=20)

        # Sidebar buttons
        self.nav_buttons = {}

        nav_items = {
            "Home": HomeView,
            "Upload Data": UploadView,
            # "Analysis" : self.show_analysis,
            # "Show Report": self.show_salary_report,
        }

        for name, command in nav_items.items():
            btn = ctk.CTkButton(
                self.sidebar,
                text=name,
                command=lambda c=command, n=name: self.navigate(n, c),
                fg_color="transparent",
                hover_color="#2E2E3E",
                anchor="w",
                width=180
            )
            btn.pack(pady=5, padx=10)
            self.nav_buttons[name] = btn

        # Main content area
        self.main_content = ctk.CTkFrame(self, corner_radius=10, fg_color="#262626")
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.active_tab = None
        self.navigate("Home", HomeView)

    def navigate(self, name, ViewClass):
        for btn in self.nav_buttons.values():
            btn.configure(fg_color="transparent")
        self.nav_buttons[name].configure(fg_color="#3E3E4E")

        self.clear_main_content()

        if name in self.view_cache:
            view = self.view_cache[name]
        else:
            if ViewClass == UploadView:
                view = ViewClass(self.main_content, controller=self.file_controller)
            else:
                view = ViewClass(self.main_content)
            self.view_cache[name] = view

        view.pack(fill="both", expand=True)

        if hasattr(view, 'tree'):
            self.tree = view.tree

    def clear_main_content(self):
        for view in self.view_cache.values():
            view.pack_forget()

    def show_salary_report(self):
        ctk.CTkLabel(self.main_content, text="Salary Report", font=("Arial", 20)).pack(pady=30)

    def show_analysis(self):
        ctk.CTkLabel(self.main_content,text="Analysis", font=("Arial",20)).pack(pady=30)



