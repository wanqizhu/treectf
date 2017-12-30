def grade(arg, key):
	if key in ["labCTF{what'a'heavenly'view}", "what'a'heavenly'view", "what_a_heavenly_view", "labCTF{what_a_heavenly_view}"]:
		return True, "Correct"
	else:
		return False, "Incorrect"
