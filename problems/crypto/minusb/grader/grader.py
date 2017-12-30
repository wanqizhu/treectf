def grade(arg, key):
	if key in ["labCTF{bee_there_or_bee_square}", "laCTF{ee_there_or_ee_square}", "labCTF{ee_there_or_ee_square}"]:
		return True, "I know it was a bad idea to let the bees escape..."
	else:
		return False, "Incorrect. Make sure your flag is in the default format."

