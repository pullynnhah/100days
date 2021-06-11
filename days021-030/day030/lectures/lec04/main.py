try:
    file = open('file.txt')
    dictionary = {"key": "value"}
    print(dictionary['non_existent_key'])
except FileNotFoundError:
    file = open('file.txt', 'w')
    file.write('Something')
except KeyError as error:
    print(f"The key {error} does not exist.")
