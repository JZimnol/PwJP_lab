import json


class MyJsonClass():
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        try:
            with open(self.file_path, 'r') as f:
                self.data = json.load(f)
        except Exception as e:
            print(e)
            self.data = {}

    def print_options(self):
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

    def show(self):
        print(json.dumps(self.data, sort_keys=True, indent=4))

    def edit(self):
        movie_name = input("Enter movie name: ")
        if movie_name in self.data:
            edit_option = input("What do you want to change? ")
            if edit_option in self.data[movie_name]:
                self.data[movie_name][edit_option] = input(f"Enter {edit_option}: ")
            else:
                print(f"No {edit_option} in database")
        else:
            print(f"No \"{movie_name}\" found.")
        self.save()

    def add(self):
        movie_name = input("Enter movie name: ")
        if movie_name in self.data:
            print(f"Movie \"{movie_name}\" already exist in the databse")
        else:
            self.data[movie_name] = {}
            self.data[movie_name]["description"] = input("Add description: ")
            self.data[movie_name]["rating"] = input("Add rating: ")
        self.save()

    def delete(self):
        movie_name = input("Enter movie name: ")
        self.data.pop(movie_name, None)
        self.save()

    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f)


if __name__ == '__main__':
    movies = MyJsonClass("user_file.json")

    while True:
        movies.print_options()
        user_input = int(input("User input: "))

        if user_input == 1:
            movies.show()
        elif user_input == 2:
            movies.edit()
        elif user_input == 3:
            movies.add()
        elif user_input == 4:
            movies.delete()
        elif user_input == 5:
            break
        else:
            pass
