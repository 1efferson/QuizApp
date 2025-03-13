import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox
from dict_for_quiz_questions import questions_q



# IMPORTS THE DICTIONARY QUESTIONS FROM dict_for_quiz_questions
questions=questions_q()


# MAIN TKINTER WINDOW
root = tk.Tk()
root.title("Python Quiz")
root.geometry("1100x700+220+70")
root.resizable(False, False)
root.configure(background="#FFF")




# INITIALIZING GLOBAL VARIABLES
score = 0
current_question = 0
selected_answers = []
time_left = 300

# A FUNCTION TO SHOW THE QUESTION
def show_question():
    global current_question

    if current_question < len(questions):
        
        question = list(questions.keys())[current_question]
        choices = questions[question]["choices"]


        selected_answer_var.set(value=-1)

        
        question_label.config(text=question)

        
        radio_button_a.config(text=f"A: {choices[0]}", value="A")
        radio_button_b.config(text=f"B: {choices[1]}", value="B")
        radio_button_c.config(text=f"C: {choices[2]}", value="C")
        radio_button_d.config(text=f"D: {choices[3]}", value="D")

    else:
        show_result()


# THIS FUNCTION HANDLES THE SUBMISSION OF THE ANSWER

def submit_answer():
    global score, current_question

    answer = selected_answer_var.get()

    if answer != "":
        
        correct_answer_index = questions[list(questions.keys())[current_question]]["answer"]
        correct_answer = ["A", "B", "C", "D"][correct_answer_index]

    
        if answer == correct_answer:
            score += 1 
        current_question += 1
        show_question()

    else:
        messagebox.showwarning("Selection Error", "Please select an answer.")




# THIS FUNCTION DISPLAYS THE RESULT AFTER THE QUIZ IS OVER

def show_result():
    global score

    if score < 5:
        response = f"{score}???? Look at you! Better luck next time!"
    else:
        response = f"Great job! Your score is {score} out of {len(questions)}."


    messagebox.showinfo("Quiz Over", response)

   
    root.quit()

# FUNCTION TO ADD A TIMER TO THE QUIZ

def update_timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time Left: {time_left} seconds") 
        root.after(1000, update_timer)
    else:
        end_quiz()


# THE FUNCTION THAT ENDS THE QUIZ

def end_quiz():
    messagebox.showinfo("Time's Up!", f"Quiz Over! Your score is {score}/{len(questions)}")
    root.quit()

# ICON OF THE APPLICATION
app_icon = Image.open("images/applogo.png")
app_icon = ImageTk.PhotoImage(app_icon)
root.iconphoto(False, app_icon)


# TITLE IMAGE (Python Quiz)
header_image = Image.open("images/titleimage.png")
header_image = ImageTk.PhotoImage(header_image)
title_image = tk.Label(root, image=header_image, background="#f0f1f5")
title_image.place(x=310, y=-10)


# CELLUSYS PICTURE AS A STILLIMAGE
# codecamp = Image.open("images/codeCampLogo_.png")
# codecamp = ImageTk.PhotoImage(codecamp)
# cellusys_picture = tk.Label(root,image=codecamp, background="#fff"  )
# cellusys_picture.place(x=750, y=570)

# CELLUSYS PICTURE AS A GIF
gif_path = "images/advert.gif"
gif = Image.open(gif_path)

frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]

def update_frame(index):
    cellusys_picture.config(image=frames[index])
    next_index = (index + 1) % len(frames)
    root.after(100, update_frame, next_index)

cellusys_picture = tk.Label(root, background="#fff")
cellusys_picture.place(x=750, y=630)

update_frame(0)



# THIS IS TO CREATE A LABEL FOR THE QUESTION
question_label = tk.Label(root, text="", font=("Times New Roman", 16), bg="#fff")
question_label.pack(padx=100, pady=100)


# THIS VARIABLE STORES THE ANSWER SELECTED BY THE USER
selected_answer_var = tk.StringVar()



# THIS CREATES THE RADIO BUTTONS FOR THE MULTIPLE CHOICES
radio_button_a = tk.Radiobutton(root,bg="#fff",variable=selected_answer_var, value=0, font=("Times New Roman", 14))
radio_button_a.pack(anchor="w", padx=80, pady=6)

radio_button_b = tk.Radiobutton(root,bg="#fff", variable=selected_answer_var, value=1, font=("Times New Roman", 14))
radio_button_b.pack(anchor="w", padx=80, pady=6)

radio_button_c = tk.Radiobutton(root,bg="#fff", variable=selected_answer_var, value=2, font=("Times New Roman", 14))
radio_button_c.pack(anchor="w", padx=80, pady=6)

radio_button_d = tk.Radiobutton(root,bg="#fff",variable=selected_answer_var, value=3, font=("Times New Roman", 14))
radio_button_d.pack(anchor="w", padx=80, pady=6)


# THIS CREATES A LABEL FOR THE TIMER
timer_label = tk.Label(root,bg="#fff", text=f"Time Left: {time_left} seconds", justify = "left", font=("Times New Roman", 12))
timer_label.pack(anchor="s", side="bottom", padx=10, pady=10)



#THIS CREATES THE SUBMIT ANSWER BUTTON
submit_button  = tk.Button(root, 
                   text="submit answer", 
                   command=submit_answer,
                   activebackground="light blue", 
                   activeforeground="#fff",
                   anchor="center",
                   bg="lightgray",
                   disabledforeground="gray",
                   fg="black",
                   font=("Times New Roman", 13),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   padx=10,
                   width=10,
                   wraplength=100)

submit_button.pack(padx=110, pady=80)


# def on_right_click(event):
#     print(f"Right click at ({event.x}, {event.y})")

# root.bind("<Button-3>", on_right_click)


show_question()

update_timer()

root.mainloop()
