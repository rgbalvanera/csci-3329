from pandastable import Table, TableModel
import tkinter as tk
import pandas as pd

root = tk.Tk()

root.geometry("800x800")

frame = tk.Frame(root)

frame.pack(fill='x')

pt = Table(frame)

df = pd.DataFrame([1,2,3], ['what','is','this'],[123,123,123],column=['VIN', 'Make', 'Model'])

pt.updateModel(TableModel(df))

root.mainloop()