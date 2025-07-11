

import pandas as pd
from tkinter import filedialog

from utils.helper_functions.data_preprocessor import DataPreprocessor
from utils.poups.custom_toast import show_toast


class FileController:
    def __init__(self,tree_getter):
        self.get_tree = tree_getter
        self.in_df = None
        self.out_df = None
        self.result_df = None
        self.columns = []



    def upload_in_file(self):
        file_pth = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])

        if file_pth:
            print(f"In file Path:{file_pth}")

        self.in_df = pd.read_excel(file_pth)
        tree = self.get_tree()
        if not tree:
            return file_pth

        return file_pth

    def upload_out_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files","*.xlsx *.xls")])

        if file_path:
            print(f"Out file path: {file_path}")

        self.out_df = pd.read_excel(file_path)
        tree = self.get_tree()
        if not tree:
            return file_path

        return file_path

    def on_submit(self):
        if self.in_df is not None and self.out_df is not None:
            column_name = 'check_in'
            self.result_df = DataPreprocessor.merge_df(self.in_df, self.out_df, column_name)
            self.result_df = DataPreprocessor.calculate_total_hours(self.result_df)
            self.columns =  self.result_df.columns
            print([x for x in self.result_df['total_hours']])


            if self.result_df is not None:
                tree = self.get_tree()
                if tree:
                    self.populate_tree(tree,  self.result_df)
                else:
                    print("Tree is not available.")
            else:
                print("Merged DataFrame is None.")
        else:
            self.columns = []
            print("No In Report uploaded.")
            show_toast(self.get_tree().winfo_toplevel(), "Upload both In & Out files!")

    def populate_tree(self, tree, df):
        tree.delete(*tree.get_children())  # clear rows
        for row in df.itertuples(index=False):
            tree.insert("", "end", values=row)




