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
    return data


def update_json(name, fav_color, fav_number):
    new_data = {
        name: {
            "favorite color": fav_color,
            "favorite number": fav_number
        }
    }

    data = read_json()
    data.update(new_data)
    with open('favorites.json', 'w') as file:
        json.dump(data, file, indent=4)

write_json("Paula", "Violet", 7)
info = read_json()
print(type(info))
print(info)
update_json("Jon", "Orange", 10)
