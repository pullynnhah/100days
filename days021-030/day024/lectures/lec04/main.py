path = '/home/paula/Desktop/100days/days021-030/day024/lectures/lec02'

with open(f'{path}/my_file.txt') as file:
    contents = file.read()
    print(contents)

with open('../lec02/my_file.txt') as file:
    contents = file.read()
    print(contents)
