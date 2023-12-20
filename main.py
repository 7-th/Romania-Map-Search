import tkinter as tk
from tkinter import ttk
from PIL import Image as im
from PIL import ImageTk
from tkinter import *
import Algorithms

# main window
root = tk.Tk()
root.title("Romanai Map GUI, Searching Algorithm")
root.geometry("900x900") 
root.config(bg='#E3CF57')

# styles
style_optionMenu = ttk.Style()
style_optionMenu.configure('my.TMenubutton', font=('Arial', 16))

btn_style = ttk.Style()
btn_style.configure('my.TButton', font=('Arial', 20, 'bold'))

# main label
# Main text
main_lbl = tk.Label(root,text = "Romania Map Search Problem", bg='#E3CF57', font= ("Arial", 25)) 
main_lbl.pack(pady=20)

# Map image
path = r'images/Romanai_map.png'
map_image = im.open(path)
width, height = map_image.size
map_image = map_image.resize((int(width//3), int(height//3)))

can_img = Canvas(root, width=600, height=400, highlightthickness=2, highlightbackground='black', bg = 'white')
can_img.pack()

tk_img = ImageTk.PhotoImage(map_image)

can_img.create_image(20, 20, anchor = NW, image = tk_img) # add tk_image

# inputs Frame
inputs_frame = Frame(root)
inputs_frame.pack(pady = 20)
inputs_frame.config(highlightbackground='black', highlightthickness=2, bg= 'white')


# initial state
init_lbl = tk.Label(inputs_frame, text="Initial State: ", font= ("Arial", 14), bg = 'white')
init_lbl.grid(column= 0, row= 0)

# initial list
init_menu = StringVar()

# try this keda
init_list = list(Algorithms.Map.keys())

init_drop = ttk.OptionMenu(inputs_frame, init_menu, "Arad",  *init_list)
init_drop.config(width=20, style="my.TMenubutton")
init_drop.grid(column=0, row=1)

# goal state
goal_lbl = tk.Label(inputs_frame, text="Goal State: ", font= ("Arial", 14), bg = 'white')
goal_lbl.grid(column= 1, row= 0)

# initial list
goal_menu = StringVar()
goal_list = list(Algorithms.Map.keys())


goal_drop = ttk.OptionMenu(inputs_frame, goal_menu, "Bucharest", *goal_list)
goal_drop.config(width=20, style="my.TMenubutton")
goal_drop.grid(column=1, row=1)

# goal state
alg_lbl = tk.Label(inputs_frame, text="Searching Algorithm: ", font= ("Arial", 14), bg = 'white')
alg_lbl.grid(column= 2, row= 0)

# algorithms list
alg_menu = StringVar()
alg_list = ['BFS', 'DFS']

alg_drop = ttk.OptionMenu(inputs_frame, alg_menu, "BFS", *alg_list)
alg_drop.config(width=20, style="my.TMenubutton")
alg_drop.grid(column=2, row=1)

result_lbl = tk.Label(root, text= "Result Will Appear Here", font= ("Arial", 14, "bold"), borderwidth=2, relief="groove", bg = 'white')
result_lbl.pack(pady=20)

# Calculate function
def cal(algorthim):
    if (algorthim == "BFS"):
        return Algorithms.breadth_first_search(str(init_menu.get()), str(goal_menu.get()))
        
    elif (algorthim == 'DFS'):
        return ("False", "False")
    
    # add if alogrithms here


# view result function
def view_result():
    # Later: edit result font here
    path_to_goal, cost = cal(alg_menu.get())
    res_text = f'Path: from {path_to_goal[0]} to {path_to_goal[-1]}\n\n {" -> ".join(path_to_goal)} \n\n Cost: {cost}'
    result_lbl.configure(text=res_text)
    
# Calculate button
btn = ttk.Button(inputs_frame, text="Calculate", command= view_result, style= 'my.TButton')
btn.grid(column=1, row= 2, ipadx=5, ipady=5, pady=10)


# mainLoop
root.mainloop()
