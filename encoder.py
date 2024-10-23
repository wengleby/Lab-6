def encoder(message):
	result = ''
	for digit in message:
		new_digit = str((int(digit)+3) % 10)
		result += new_digit
	return result
