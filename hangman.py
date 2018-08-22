from hangmangraphic import*

for i in range(0, len(word_guess)):
    word_to_guess.append(word_guess[i])

for i in word_to_guess:  
    currently.append("_")

guesses=0
def guess_input():
    global guesses
    global currently
    global word_to_guess

    while True:
        user_input= input("Please input your guess (a single letter): ")

        if user_input in accepted_input:
            if user_input in guess_letters:
                print("You have already inputted this letter before, be more attentive!")
            else:
                guess_letters.append(user_input)
                if user_input in word_to_guess:
                    print("Well done, you guessed the right letter")
                    for i in range(0, len(word_to_guess)):
                        if word_to_guess[i] == user_input:
                            currently[i] = user_input
                else:
                    print("Opps, there is no such letter in our word")

                    guesses = guesses + 1

        else:
            print("INPUT ERROR! Please input single letter in range a-z")

        if guesses > 5: 
            ob.hangman_graphic(guesses)
            break
        elif "_" in currently: 
            ob.hangman_graphic(guesses)
        else: 
            ob.hangman_graphic(-1)
            break
def hangman():
    ob.hangman_graphic(guesses)
    guess_input()

hangman()
print("END!")
