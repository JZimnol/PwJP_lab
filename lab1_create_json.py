import json


def print_options():
    to_print = "" \
        "----------------------------------------\n" \
        "OPTIONS:\n" \
        "\t1. Show data\n" \
        "\t2. Edit data\n" \
        "\t3. Add data\n" \
        "\t4. Delete data\n" \
        "\t5. Quit\n" \
        "----------------------------------------"
    print(to_print)


def show_data(data: dict):
    print(json.dumps(data, sort_keys=True, indent=4))


def edit_data(data: dict):
    movie_name = input("Enter movie name: ")
    if movie_name in data:
        edit_option = input("What do you want to change? ")
        if edit_option in data[movie_name]:
            data[movie_name][edit_option] = input(f"Enter {edit_option}: ")
        else:
            print(f"No {edit_option} in database")
    else:
        print(f"No \"{movie_name}\" found.")


def add_data(data: dict):
    movie_name = input("Enter movie name: ")
    if movie_name in data:
        print(f"Movie \"{movie_name}\" already exist in the databse")
    else:
        data[movie_name] = {}
        data[movie_name]["description"] = input("Add description: ")
        data[movie_name]["rating"] = input("Add rating: ")


def delete_data(data: dict):
    movie_name = input("Enter movie name: ")
    data.pop(movie_name, None)


if __name__ == '__main__':
    try:
        with open("user_file.json", 'r') as f:
            movie_data = json.load(f)
    except Exception as e:
        print(e)
        movie_data = {}

    while True:
        print_options()
        user_input = int(input("User input: "))

        if user_input == 1:
            show_data(movie_data)
        elif user_input == 2:
            edit_data(movie_data)
        elif user_input == 3:
            add_data(movie_data)
        elif user_input == 4:
            delete_data(movie_data)
        elif user_input == 5:
            break
        else:
            pass

    with open("user_file.json", 'w') as f:
        json.dump(movie_data, f)
