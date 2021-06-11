import json

def write_json(name, fav_color, fav_number):
    data = {
        name: {
            "favorite color": fav_color,
            "favorite number": fav_number
        }
    }

    with open('favorites.json', 'w') as file:
        json.dump(data, file, indent=4)


def read_json():
    with open('favorites.json') as file:
        data = json.load(file)
        print(type(data))
    return data


write_json("Paula", "Violet", 7)
print(read_json())
