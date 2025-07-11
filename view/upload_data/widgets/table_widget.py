from tkinter import ttk


def create_table(parent,columns):
    style = ttk.Style()
    style.theme_use('default')

    style.configure(
        "Treeview",
        background="#1e1e28",
        foreground="#f1f1f1",
        rowheight=40,
        fieldbackground="#1e1e28",
        font=('Lato', 12)
    )

    style.configure(
        "Treeview.Heading",
        background="#3b82f6",
        foreground="white",
        font=("Lato", 13, 'bold')
    )

    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])


    tree = ttk.Treeview(parent, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=120)


    tree.pack(side="left", fill="both", expand=True, pady=10, padx=10)

    scrollbar = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    return tree