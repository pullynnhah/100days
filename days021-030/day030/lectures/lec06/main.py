try:
    file = open('file.txt')
    dictionary = {"key": "value"}
    print(dictionary['key'])
except FileNotFoundError:
    file = open('file.txt', 'w')
    file.write('Something')
except KeyError as error:
    print(f"The key {error} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
    raise TypeError("This is a ERROR that I made up.")
