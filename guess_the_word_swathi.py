import random

# #creating a list of words for hangman
word_list = ['book', 'cat', 'dog', 'apple', 'banana', 'class', 'python', 'java', 'rock', 'scissors', 'paper', 'run', 'walk', 'talk', 'try', 'evening', 'morning']


# #Word chosen by the program out of the word_list, using 'random' function - **Code works from the main() function**
def pick_random_word(given_list):
	random_word = given_list[random.randrange(len(given_list))]
	return random_word


def add_letter(user_guessed_letter, random_word, string_of_my_guess):
	pos = []

	for i in range(len(random_word)):
		if random_word[i] == user_guessed_letter:
			pos.append(i)
	for i in pos:
		string_of_my_guess[i] = user_guessed_letter
	

def continue_game(continue_string):
	while True:
		if continue_string.lower() == "yes":
			break
		elif continue_string.lower() == "no":
			print "\nEnjoy!! See you later!! :)"
			quit()	

# ********************+****
# #Function to ask the User for input - **code Works from the main() function **
# Validates the user input
# # *************************
def get_user_input(string_of_my_guess):
	while True:
				user_guess = raw_input("\nGuess the letter: ")
				user_guess = user_guess.lower()
				if user_guess not in 'abcdefghijklmnopqrstuvwxyz':
					print "I don't understand!! Please enter a valid letter: "
				elif len(user_guess)!= 1:
					print "Please enter a single letter: "
				elif user_guess in string_of_my_guess:
					print "You have already entered the letter once, please enter again: "
				else:
					return user_guess



# #Function to validate if the User input is present in the secret word, 
#if yes - add it to a string of correct letters, else append it to string of incorrect_letters
def check_user_input(guessed_word):

	length_of_guessed_word = len(guessed_word)
	string_of_my_correct_guess = ["_" for i in range(length_of_guessed_word)]
	print "\nLength of copy of guessed_word is ",string_of_my_correct_guess

	incorrect_letters = []
	list_of_my_guesses = []
	while len(incorrect_letters) < 5:
		user_guessed_letter = get_user_input(list_of_my_guesses)
		list_of_my_guesses.append(user_guessed_letter)


		if user_guessed_letter in guessed_word:
			add_letter(user_guessed_letter, guessed_word, string_of_my_correct_guess)
			print string_of_my_correct_guess 
			
		else:
			
			incorrect_letters.append(user_guessed_letter)
			print "The incorrect guesses so far is: ",incorrect_letters

		if "".join(string_of_my_correct_guess) == guessed_word:
			continue_string = raw_input ("\nyayyy! you've won!!\n\nDo you want to continue? Enter yes or no: ")
			continue_game(continue_string)
			break
		elif len(incorrect_letters) == 5:
			continue_string = raw_input ("\nSorry! you have made 5 incorrect guesses - game over!\n\nDo you want to continue? Enter yes or no: ")
			continue_game(continue_string)


#To do: call function here asking user to continue or quit

	



def main():
	while True:
		guessed_word = pick_random_word(word_list)
		print "Random word is: ", guessed_word

		length_of_guessed_word = len(guessed_word)
		print "length of secret word is: ",length_of_guessed_word

		check_user_input(guessed_word)



if __name__ == '__main__':
	main()
	


