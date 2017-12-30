def grade(arg, key):
	if "labCTF{nice}" == key or "nice" == key:
		return True, "Correct"
	else:
		return False, "Incorrect"
