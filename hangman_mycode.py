import random

# #creating a list of words for hangman
word_list = ['book', 'cat', 'dog', 'apple', 'banana', 'class', 'python', 'java', 'rock', 'scissors', 'paper', 'run', 'walk', 'talk', 'try', 'evening', 'morning']

# #Word chosen by the program out of the word_list, using 'random' function
def pick_random_word(given_list):
	random_word = given_list[random.randrange(len(given_list))]
	return random_word


#below print statment for just checking if the pick_random_word function works
#print "The chosen word is ", pick_random_word(word_list)


# ********************+****
# #Function to ask the User for *****NEEEED HELP TO LINK THIS FUNCTION TO THE VALIDATION FUNCTIONS*****input
# # *************************
def get_user_input():
	user_guess = raw_input("Guess the letter: ")
	return user_guess



# #Function to validate if the User input is present in the secret word
def check_user_input(random_word, user_guess):
	# random_word = pick_random_word(word_list)
	print "The random word is ", random_word
	string_of_my_guesses = [len(guessed_word)]
	# hangmanword = []
	if user_guess in random_word:
		
		print "True"
	else:
		print "False"

# check_user_input(word_list,'a')

#check_user_input(word_list, user_guess)

def main():
	# @TODO: pick a word and store it
	guessed_word = pick_random_word(word_list)

	# @TODO: get user's guess
	user_guess = get_user_input()
	print user_guess
	# @TODO: check if guessed letter in word
	check_user_input(guessed_word, user_guess)
	# @TODO: if guessed letter in word update solution list

if __name__ == '__main__':
	main()
	


