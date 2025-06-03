# import tkinter as tk
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
# from PIL import ImageTk
# import sqlite3
#
# def clear_window(frame):
#     for widget in frame.winfo_children():
#         widget.destroy()
#
#
# def fetch_db():
#     c = sqlite3.connect("air_monitor/database/air.db")
#     cursor = c.cursor()
#     # cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
#     cursor.execute("SELECT name FROM stations")
#     all_tabels = cursor.fetchall()
#     names = []
#     for row in all_tabels:
#         names.append(row[0])
#         print(row[0])
#     c.close()
#     return names
#
#
# def load_frame1():
#     clear_window(frame2)
#     frame1.tkraise()
#     frame1.pack_propagate(False)
#
#     logo_img = ImageTk.PhotoImage(file="assets/logo.png")
#     logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
#     logo_widget.image = logo_img
#     logo_widget.pack()
#
#     tk.Label(
#         frame1,
#         text="Air Aware",
#         bg=bg_colour,
#         fg="black",
#         font=("Arial", 14),
#     ).pack()
#
#     tk.Button(
#         frame1,
#         text="Start",
#         font=("TkHeadingFont", 20),
#         bg="#ffffff",
#         fg="#4582EC",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda: load_frame2()
#     ).pack(pady=20)
#
# def load_frame2():
#     clear_window(frame1)
#     frame2.tkraise()
#     names = fetch_db()
#
#     logo_img = ImageTk.PhotoImage(file="assets/logo.png")
#     logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)
#     logo_widget.image = logo_img
#     logo_widget.pack(pady=20)
#
#     tk.Label(
#         frame2,
#         text="Lista stacji",
#         bg=bg_colour,
#         fg="black",
#         font=("TkHeadingFont", 14),
#     ).pack()
#
#     for i in names:
#         tk.Label(
#             frame2,
#             text=i,
#             bg="#28393a",
#             fg="black",
#             font=("TkHeadingFont", 12),
#         ).pack(fill="both")
#
#     tk.Button(
#         frame2,
#         text="Backt",
#         font=("TkHeadingFont", 18),
#         bg="#ffffff",
#         fg="#4582EC",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda: load_frame1()
#     ).pack(pady=20)
#
# # def launch_gui():
# bg_colour = "#ffffff"
# #initiallize app
# root = tk.Tk()
# root.title("Air Aware")
# # place app in the center
# root.eval("tk::PlaceWindow . center")
# # x = root.winfo_screenwidth() // 2
# # y = int(root.winfo_screenheight() * 0.1)
# # root.geometry('500x600+' + str(x) + '+' + str(y))
#
# frame1 = tk.Frame(root, width=500, height=500, bg=bg_colour)
# frame2 = tk.Frame(root, bg=bg_colour)
#
# for frame in (frame1, frame2):
#     frame.grid(row=0, column=0, sticky="nsew")
#
# load_frame1()
#
# root.mainloop()
