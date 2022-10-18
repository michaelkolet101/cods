from time import sleep
import os
def picture_1():
	
	return "x-------x \n\n\n\n\n"
def picture_2 ():
	return r"""
	x-------x
	|
	|
	|
	|
	|
	
	"""
def picture_3():
	
	return r"""
	x-------x
	|       |
	|       0
	|
	|
	|
	
	"""
def picture_4() :
	
	return r"""
    x-------x
    |       |
    |       0
    |       |
    |
    |
	
	"""
def picture_5() :
	return r"""
    x-------x
    |       |
    |       0
    |      /|\
    |
    |
	"""
def picture_6() :
	return r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
	"""
def picture_7() :
	return r"""	
	x-------x
        |       |
        |       0
        |      /|\
        |      / \
        |
	
	"""
	
def check_valid_input(letter_guessed,old_letters_guessed):
	"""Checks if the input is correct
    :param letter_guessed: letter_guessed value
    :param old_letters_guessed: letters list value
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True or False
    :rtype: bool
    """
	"""z is The value of the first string"""
	z = ord(letter_guessed[0])
	if len(letter_guessed) > 1 :
		return False
	elif letter_guessed in old_letters_guessed:
		return False
	if ((z > 96) and (z < 123)) or ((z > 64) and (z < 91)):
		return True 
		old_letters_guessed += letter_guessed
	else:
		return False
		
	
		
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	"""Checks whether the character is invalid or has already guessed the character in the past.
    :param letter_guessed: letter_guessed value
    :param old_letters_guessed: letters list value
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True or print X
    :rtype: bool
    """
	
	if check_valid_input(letter_guessed,old_letters_guessed) == True:
		old_letters_guessed += letter_guessed
		return True 
	elif check_valid_input(letter_guessed,old_letters_guessed) == False:
		new_list = sorted(old_letters_guessed, key=str.lower)
		string_list_to_print = '-> '.join(new_list)
		print("X \n", string_list_to_print.lower(),"Pleas enter anuther char ")
	
	
	
def HANGMAN_ASCII_ART():
	"""Prints a photo of the opening of the game.
    
    """
	print("""

	    ________________________________________________________
	... |                                                      |
	... |    _    _                                            |
	... |   | |  | |                                           |
	... |   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     |
	... |   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \    |
	... |   | |  | | (_| | | | | (_| | | | | | | (_| | | | |   |
	... |   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|   |
	... |                        __/ |                         |
	... |                       |___/                          |
	... |______________________________________________________|
	...
	... """)
	
	

def show_hidden_word(secret_word, old_letters_guessed):
	"""Print and shows what the player has guessed so far.
    :param secret_word: secret_word value
    :param old_letters_guessed: letters list value
    :type secret_word: str
    :type old_letters_guessed: list
    
    """
	"""מחרוזת שנקראת secret_word. המחרוזת מייצגת את המילה הסודית שהשחקן צריך לנחש."""
	"""רשימה שנקראת old_letters_guessed. הרשימה מכילה את האותיות שהשחקן ניחש עד כה."""
	
	new_list = []
	for index_of_secret_word in secret_word:
		if index_of_secret_word in old_letters_guessed:
			new_list += index_of_secret_word
		else:
			new_list += "_"
	new_string =" ".join(new_list)
	print(new_string)
	

def check_win(secret_word, old_letters_guessed):
	"""Checks whether the user has won or lost.
    :param secret_word: secret_word value
    :param old_letters_guessed: letters list value
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True or False
    :rtype: bool
    """
	
	mone = 0
	for index_of_secret_word in secret_word:
		if index_of_secret_word in old_letters_guessed:
			mone += 1
	
	if mone == len(secret_word):
		return True
	else:
		return False
	
def print_hangman(num_of_tries ,HANGMAN_PHOTOS):
	"""Prints the welcome screen and the number of attemptsץ
    :param num_of_tries: number value
    :param HANGMAN_PHOTOS: photo value
    :type num_of_tries: int
    :type HANGMAN_PHOTOSt: dict
    """
	print(HANGMAN_PHOTOS[num_of_tries])
	
	
def choose_word(file_path, index):
	
	"""Selects a word from the file.
    :param file_path: file value
    :param index: index value
    :type file: str
    :type index: int
    :return: A word from the file
    :rtype: str
    """
	word_count = 0
	index = index - 1
	input_file = open(file_path,"r")
	LIST_OF_WORDS = input_file.read().split()
	input_file.close()
	for word in LIST_OF_WORDS:
		for chek_word in LIST_OF_WORDS:
			if word == chek_word:
				word_count += 1
	the_argumnent = LIST_OF_WORDS[index]
	return the_argumnent
	
def colors():
	for i in range(1,5):
		os.system("color 01")
		sleep(0.5)
		os.system("color 02")
		sleep(0.5)
		os.system("color 06")
		sleep(0.5)
		os.system("color 05")
		sleep(0.5)
	sleep(3)
	
def return_to_suors_color():
	os.system('cls')
	os.system("color 07")
	
	

	
def main():
	
	


	MAX_TRIES = 6
	old_letters_guessed = []
	num_of_tries = 0
	
	
	HANGMAN_ASCII_ART()
	
	
	
	HANGMAN_PHOTOS = {0 :  picture_1() ,1 : picture_2(), 2 :  picture_3(), 3 :  picture_4() , 4 :  picture_5() , 5 :  picture_6() , 6 :  picture_7() }
	
	print( " \n", "\n Trials are allowed in the game: ", MAX_TRIES)
	colors()
	os.system('cls')
	return_to_suors_color()
	
	string_file = input("Please enter a file path for words: ")
	file = string_file.strip('"')
	
	num_of_tries == 0
	game = "yes"
	
	while game == "yes":
		return_to_suors_color()
		index = int(input("enter index of the word: "))
		input_file = open(file,"r")
		LIST_OF_WORDS = input_file.read().split()
		input_file.close()
	
		if index > len(LIST_OF_WORDS):
			index = index % len(LIST_OF_WORDS)				
		os.system('cls')
		
		os.system("color 03")
		print_hangman(num_of_tries ,HANGMAN_PHOTOS)
		the_game_bord = choose_word(file, index)
		if (the_game_bord.find(" ") == -1): 
			print("__ "*len(the_game_bord))
		   
		while num_of_tries < 6:
			
			gassing_of_char = input("Please enter one letter: ")
			
			if not try_update_letter_guessed(gassing_of_char,old_letters_guessed) == True:
				continue
			os.system('cls')
			show_hidden_word(the_game_bord, old_letters_guessed)
			
				
			if not gassing_of_char in the_game_bord:
				
				num_of_tries += 1
			print_hangman(num_of_tries ,HANGMAN_PHOTOS)
			
			
			
			if check_win(the_game_bord, old_letters_guessed) == True:
				print("***   WIN   ***")
				for i in range(1,6):
					os.system("color 01")
					sleep(0.5)
					os.system("color 02")
					sleep(0.5)
				
				game = input("\n\n\n Rematch? yes / no ")
				if game == "no":
					os.system('cls')
					os.system("color 07")
					print("***  GOODBY  ***")
					sleep(3)
				else:
					os.system('cls')
					os.system("color 03")
					num_of_tries = 0
					old_letters_guessed = []
				break
			if num_of_tries == 6:
				print("LOSE")
				for i in range(1,6):
					os.system("color 01")
					sleep(0.5)
					os.system("color 04")
					sleep(0.5)
				game = input("\n\n\n remac? yes / no ")
				if game == "no":
					os.system('cls')
					os.system("color 07")
					print("***  GOODBY  ***")
					sleep(3)
				else:
					os.system('cls')
					os.system("color 03")
					num_of_tries = 0
					old_letters_guessed = []
				break
	
		
		
	
	
	
	
	
	 
if __name__=="__main__":
	main()

	
	
	
	
	
	
	