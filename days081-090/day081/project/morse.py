from morse3 import Morse
print('Welcome to the Morse Code Generator!')
message = Morse(input("Your message: "))

morse = message.stringToMorse()
print(f'Here is your message in morse code: {morse}')
