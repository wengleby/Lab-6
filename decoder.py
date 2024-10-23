
def decode(password):
    decoded = ''
    for item in password:
        decoded_value = int(item)-3
        if decoded_value < 0:
            decoded_value += 10
        decoded += str(decoded_value)
    return decoded

