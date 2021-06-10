class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('colour')
        self.seats = kw.get('seats')


car1 = Car(make='Nissan', model='GT-R')
print(f'Make: {car1.make}, Model: {car1.model}, Colour: {car1.colour}, Seats: {car1.seats}')

car2 = Car(make='Nissan', model='Skyline _')
print(f'Make: {car2.make}, Model: {car2.model}, Colour: {car2.colour}, Seats: {car2.seats}')
