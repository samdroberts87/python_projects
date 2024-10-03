import requests

categories = {1: "Programming", 2: "Miscellaneous", 3: "Dark", 4: "Pun", 5: "Any"}


def main():
    another_joke = True
    while another_joke:
        chosen_category_number = get_input()
        url = get_url(chosen_category_number)
        final_joke = get_joke(url)
        print(f"\nHere's your Joke:\n\n{final_joke}\n")
        another_joke = ask_for_another_joke()


def get_input():
    chosen_category_number = 0
    while chosen_category_number not in range(1, len(categories) + 1):
        try:
            chosen_category_number = int(
                input(
                    f"\nChoose joke type. Enter corresponding number from {categories}\n:"
                )
            )
        except ValueError:
            print(f"\nYou must enter a number between 1 and {len(categories)}\n")
    return chosen_category_number


def get_url(number):
    category = categories[number]
    return f"https://v2.jokeapi.dev/joke/{category}?type=single"


def get_joke(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data["joke"]


def ask_for_another_joke():
    answer = input("\nWant another joke? (yes/no): ").strip().lower()
    if answer in ["yes", "y"]:
        return True
    else:
        print("\nThanks for using the joke app! Goodbye!\n")
        return False


if __name__ == "__main__":
    main()
