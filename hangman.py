# imports
from random import choice

# hangerMan
stick_man = [
    """||------|   """,
    """||      |   """,
    """||     (O)  """,
    """||     /|V  """,
    """||     / L  """,
    """||          """]

# GAME INITIALIZATION
words_list = ['dentist', 'gaming', 'shovel', 'battle', 'storming']
print("Welcome to Hangman!")

#command
command = input(print("Play Game or exit ? y/n : "))

#single letter function
def IsSingleLetter(str):
    if len(str) == 1 and str.isalpha():
        return True
    else:
        return False

#condition if user proceeds to play by inputing 'y'
while command == "y":

    #variable initialization
    guess_word = choice(words_list)
    underscored_word = ["_"]*len(guess_word)
    number_of_guess = 0
    wrong_input = []
    correct_inputs = []

    #condition while the current number of guesses are not yet on limit and if the current progress word is not equal to Hidden Word
    while number_of_guess <= 5 and not ("".join(underscored_word) == guess_word):

        #printing  hint by transforming each character in Hidden word to undescore '_' 
        print("The word has", len(guess_word),"letters: " + '_'*len(guess_word))
        acquired_letter = input(print("Guess a Letter: ", '\n'))

        #calling IsSingleLetter function to validate if the user input is single letter and alphabet
        if IsSingleLetter(acquired_letter):

            #validation if the guess letter is already been guessed, presents prompt
            if acquired_letter in correct_inputs or acquired_letter in wrong_input:
                print("you've already guessed this letter")
                pass

            #validation if the guess letter is in the Hidden word
            if acquired_letter in guess_word:
                correct_inputs.append(acquired_letter)
                print("Great!!")

                #appending each correct guess letter in underscore word by appending to index
                for i, letter in enumerate(guess_word):
                    if letter != "_" and acquired_letter == letter:
                        underscored_word[i] = letter

                #displays the progress of the Hidden word
                print(f"Your Guessed Word", "".join(underscored_word).upper())

            #validation if the guess letter is not on the Hidden word and append to list for wrong inputs
            else:
                wrong_input.append(acquired_letter)
                number_of_guess += 1
                print(f"{acquired_letter} is not in the Hidden Word")
                print('\n', f"You have used {
                      number_of_guess} out of 6 guess", '\n')
                
                #displays the stickman array each wrong guess
                print(*stick_man[0:number_of_guess], sep='\n')

        #displays if the input is not letter or not sinlge character
        else:
            print(f"Please input only single letters", '\n')
            print(f"Hidden word has {'_'*len(guess_word)} letters")

    #validate if the guess reached the limit or if the underscored word is equally to hidden word
    else:

        #if he guess the hidden word 
        if "".join(underscored_word) == guess_word:
            print("CONGRATULATIONS YOU WON !!!!!!!!!!!!!!!")
            command = input(print("Would like to play again? y/n"))
        
        #if he reached the guess limit 
        else:
            print("Sorry you have used all the chances game over T_T")
            command = input(print("Would like to play again? y/n"))

else:
    quit()
