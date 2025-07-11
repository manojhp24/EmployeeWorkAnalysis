import customtkinter as ctk


from view.upload_data.widgets.upload_card import create_upload_card
from view.upload_data.widgets.table_widget import create_table


class UploadView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.tree = None

        ctk.CTkLabel(self, text="Upload Data", font=("Lato", 22, "bold")).pack(pady=(30, 10))

        file_grid_wrapper = ctk.CTkFrame(self, fg_color="transparent")
        file_grid_wrapper.pack(pady=10, padx=20, fill="x")

        file1_card = create_upload_card("In Report", file_grid_wrapper, browse_callback=self.controller.upload_in_file)
        file1_card.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        file2_card = create_upload_card("Out Report", file_grid_wrapper, browse_callback=self.controller.upload_out_file)
        file2_card.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        submit_button = ctk.CTkButton(
            self,
            text="Submit",
            command=self.on_submit  # Local method
        )
        submit_button.pack(pady=10)

        file_grid_wrapper.grid_columnconfigure(0, weight=1)
        file_grid_wrapper.grid_columnconfigure(1, weight=1)

        self.content_frame = ctk.CTkFrame(
            self,
            fg_color='#2C2F33',
            corner_radius=15,
            border_color='#7289DA',
            border_width=2,
            height=280
        )
        self.content_frame.pack(padx=20, pady=20, fill='both', expand=True)
        self.content_frame.pack_propagate(True)

    def on_submit(self):
        self.controller.on_submit()  # update columns

        if self.tree:
            self.tree.destroy()

        if list(self.controller.columns):  # checks if columns exist
            self.tree = create_table(self.content_frame, list(self.controller.columns))
            self.controller.tree = self.tree
            if self.controller.in_df is not None:
                self.controller.populate_tree(self.tree, self.controller.result_df)












