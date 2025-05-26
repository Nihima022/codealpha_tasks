import random
import tkinter
import threading
from playsound import playsound
from PIL import Image, ImageTk

#GUI Setup-1:Window
window = tkinter.Tk()
window.title("Hang game")
window.geometry("600x800")
window.resizable(False, False)

#Game Variable
word = ""
guessed_letter = []
wrong_guess = 0
attempts = 6
win=0
losses=0


#GUI Step : Load Sound
def play_sound(file):
    threading.Thread(target=playsound, args=(file,), daemon=True).start()

def play_win():
    play_sound("win.mp3")

def play_lose():
    play_sound("loose.mp3")

def play_right():
    play_sound("correct.mp3")

def play_click():
    play_sound("click.mp3")

def play_error():
    play_sound("error.mp3")

def play_wrong():
    play_sound("wrong.mp3")


#GUI Setup:Load Background Image
try:
    background_image = Image.open("white.jpg").resize((800, 800), Image.Resampling.LANCZOS)
except AttributeError:
    background_image = Image.open("image.png").resize((800, 800), Image.ANTIALIAS)

background = ImageTk.PhotoImage(background_image)
background_label = tkinter.Label(window, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.lower()

#GUI Setup 3 :Display Setup

#GUI-1.Heading of the page
heading_label = tkinter.Label(window,
                              text="🎉 Welcome to Hanggame 🎉",
                              font=("Algerian", 28, "bold"),
                              fg="orange",
                              bg="light grey",
                              pady=10)
heading_label.pack(pady=5, padx=5,fill="x")

#GUI-2.Create frame for further usage
frame = tkinter.Frame(window, bg="light grey", bd=1,relief="ridge",height=300)
frame.pack(pady=20, padx=20,fill="x")

frame1 = tkinter.Frame(window, bg="lightgrey", bd=1,relief="ridge")
frame1.pack(pady=20, padx=20,fill="x")

#GUI-3.Display box
view_word = tkinter.Label(frame,text='',
                          font=("Courier", 20, "bold"),
                          bg="light yellow",fg="orange",
                          padx=15,pady=10,relief="ridge",bd=5)
view_word.pack(pady=10,padx=10,fill="x")

#GUI-4.Entry box
entry = tkinter.Entry(frame,justify="center",
                          font=("Helvetica", 25),
                          fg="black",bg="white",
                          cursor="hand2")
entry.insert(0,"Write Here")
entry.pack(pady=2,padx=10,fill="x")

#GUI-5.Indication of Entry
indicating_label = tkinter.Label(frame,
                              text="Write Your Text Here!!",
                              font=("Times New Roman", 15),
                              fg="grey",
                              bg="light grey")
indicating_label.pack(pady=5,fill="x")

#GUI-6.Result showing box
result_label = tkinter.Label(frame1, text="", font=("Helvetica bold", 18),bg="white",fg="brown",padx=10,pady=10)
result_label.pack(pady=15,padx=15,fill="x")

#GUI-7.Correct word showing
correct_word_label = tkinter.Label(frame1, text="", font=("Helvetica", 16), fg="hotpink", bg="light grey")
correct_word_label.pack(pady=5,fill="x")

#GUI-7.Wrong Guessed letter display
wrong_display = tkinter.Label(frame1, text="Wrong Guess", font=("Times New Roman", 18),bg="lightgrey",fg="purple",padx=10,pady=10)
wrong_display.pack(pady=15,padx=15,fill="x")

#GUI-8.Attempt left showing box
attempts_left_label=tkinter.Label(frame1,text="",font=("Helvetica",16),fg="orange",bg="lightgrey")
attempts_left_label.pack(pady=15,padx=15,fill="x")

#GUI-9.Scoreboard
scoreboard_label=tkinter.Label(frame1,text="",font=("Helvetica",18),fg="yellow",bg="grey")
scoreboard_label.pack(pady=15,padx=15,fill="x")


#Working Functions
#Step 1:Random Word Selection
def choose_word():
    word_list = ["python", "programming", "game", "machine", "learning",
                 "developer", "artificial", "intelligence", "keyboard",
                 "function", "variable", "waterpot", "decision", "choice"]
    selected_word = random.choice(word_list)
    return selected_word


#Step 2:Display word with Guesses
def display_word(word, guessed_letter):
    result = []
    for letter in word:
        if letter in guessed_letter:
            result.append(letter)
        else:
            result.append("_")
    return " ".join(result)


#Step 3:Update Display(this function update the game interface after each guess)
def update_display():
    word_display = display_word(word, guessed_letter)
    view_word.config(text=word_display)

    wrong_letters = []
    for letter in guessed_letter:
        if letter not in word:
            wrong_letters.append(letter)

    wrong_text = "Wrong Guesses: " + " ".join(wrong_letters)
    wrong_display.config(text=wrong_text)

    attempts_remain=attempts-wrong_guess
    attempts_left="Attempts Left: " + str(attempts_remain)
    attempts_left_label.config(text=attempts_left)


#Step 4:Start a new game function
def start_game():
    global word, guessed_letter, wrong_guess, attempts
    word = choose_word()
    guessed_letter.clear()
    wrong_guess = 0

    result_label.config(text="")

    correct_word_label.config(text="")

    entry.config(state="normal")

    guess_button.config(state="normal")

    entry.delete(0, tkinter.END)

    update_display()

    scoreboard_label.config(text=f"Wins: {win}  |  Losses: {losses}")


#Step :End game function
def end_game():
    entry.config(state="disabled")
    guess_button.config(state="disabled")


#Step 4:Handle a guess
def guessing_game():
    global wrong_guess,win,losses
    guess = entry.get().lower().strip()   #get the input guess from the user and make it to lower case
    play_click()
    entry.delete(0, tkinter.END)     #clear the entry box for further use


    if len(guess) != 1:
        result_label.config(text="Please enter a single letter")
        play_error()
        return

    if not guess.isalpha():
        result_label.config(text="Please enter a alphabetic letter")
        play_error()
        return

    if guess in guessed_letter:
        result_label.config(text="You have already guessed this letter")
        play_error()
        return

    guessed_letter.append(guess)

    if guess in word:
        result_label.config(text="Correct!")
        play_right()
    else:
        wrong_guess += 1
        result_label.config(text="Wrong!")
        play_wrong()

    update_display()

    #Check Win or Loose
    if set(word).issubset(guessed_letter):
        result_label.config(text="Congratulation! You Won")
        play_win()
        win +=1
        end_game()
        update_display()
        scoreboard_label.config(text=f"Wins: {win}  |  Losses: {losses}")
        window.after(10000, start_game)                                        #Restart game after every win or loose

    elif wrong_guess >= attempts:
        result_label.config(text="You Lost!, Better Luck Next Time")
        play_lose()
        correct_word_label.config(text=f"The correct word was: {word}")
        losses+=1
        end_game()
        update_display()
        scoreboard_label.config(text=f"Wins: {win}  |  Losses: {losses}")
        window.after(10000,start_game)                          #restart game after every win or loose


def reset_game():
    global win , losses
    win=0
    losses=0
    scoreboard_label.config(text=f"Wins:{win} | Losses{losses}")

guess_button = tkinter.Button(frame, text="Guess",
                              font=("Courier", 18),
                              bg="beige",fg="black",
                              cursor="hand2",
                              command=guessing_game)
guess_button.pack(pady=5)

reset_button = tkinter.Button(window, text="Reset", font=("Courier", 18),cursor="hand2",command=reset_game)
reset_button.pack()



start_game()
window.mainloop()
