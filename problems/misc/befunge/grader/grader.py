def grade(arg, key):
	if "labCTF{ice_meme}" == key:
		return True, "Correct"
	elif "labCTF{this_is_not_the_flag}" == key:
		return False, "heh, you didn't seriously think that was the flag, right?!"
	else:
		return False, "Incorrect"
