# Work in progress :)
import tkinter as tk
import chatbot as cb

def process_request():
    query = E1.get()
    LB1.config(text = cb.respond_to(query, cb.chat_data))

window = tk.Tk()
window.title("CB-1")
window.configure(width=500, height=300)
window.configure(bg="lightgray")

LB1 = tk.Label(window, text="      ")
LB1.pack()

E1 = tk.Entry(window, bd = 5)
E1.pack(side=tk.RIGHT)

B1 = tk.Button(window, text ="Send", command=process_request)
B1.pack(side=tk.LEFT)
window.mainloop()
