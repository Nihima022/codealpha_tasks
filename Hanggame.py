import random

#Step-1:Random word Selection
def choose_word():
    word_list=["python","programming","game","machine","learning",
               "developer","artificial","intelligence","keyboard",
               "function","variable","waterpot","decision","choice"]
    selected_word=random.choice(word_list)
    return selected_word

#Step-2:display words
def display_word(word,guessed_letters):
    result=[]
    for letter in word:
        if letter in guessed_letters:
            result.append(letter)
        else:
            result.append("_")
    return " ".join(result)

#Step-3:Start game
def game():
    word=choose_word()
    guessed_letters=[]
    attempts=6
    word_guess=0
    print("Welcome to Hanggame")
    print("Guess the word")
    print(display_word(word,guessed_letters))

    while word_guess<attempts and set(word) !=set(letter for letter in guessed_letters if letter in word):
        guess=input("Enter a letter:").lower()

        if len(guess)!=1:
            print("Please enter a valid letter")
            continue
        if not guess.isalpha():
            print("Please enter a alphabetic letter")
            continue
        if guess in guessed_letters:
            print("You have already guessed the letter")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Your guess is correct.")
        else:
            word_guess +=1
            print("You are wrong")
            attempts_left=attempts-word_guess
            print("Attempts left:",attempts_left)

        display=display_word(word,guessed_letters)
        print(display)

        wrong_guess=[]

        for letter in guessed_letters:
            if letter not in word:
                wrong_guess.append(letter)
        print("Wong letters are :",wrong_guess)

    if set(word).issubset(set(guessed_letters)):
        print("Congratulations")
    else:
        print("Better luck next time")


if __name__ == "__main__":
    while True:
        game()
        print("Start a new game")






