import string

#Ayy you got it! labCTF{caesar_loved_numbers_2}
flag = "065 121 121 032 121 111 117 032 103 111 116 032 105 116 033 032 108 097 098 067 084 070 123 099 097 101 115 097 114 095 108 111 118 101 100 095 110 117 109 098 101 114 115 095 050 125"


def caesar_nums(plaintext, shift):
	nums = '0123456789'
	shifted_nums = nums[shift:] + nums[:shift]
	table = string.maketrans(nums, shifted_nums)

	return plaintext.translate(table)



print(caesar_nums(flag, 3))