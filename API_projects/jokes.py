import requests

categories = {
    1: "Programming",
    2: "Miscellaneous",
    3: "Dark",
    4: "Pun",
    5: "Any"
}

def main():
    ask_again = True
    while ask_again:
        print()
        chosen_category_number = int(input(f"Choose joke type. Enter corresponding number: {categories}"))
        if chosen_category_number <= 5 and chosen_category_number > 0:
            ask_again = False
    url = get_url(chosen_category_number)
    final_joke = get_joke(url)
    print(f"\nHere's your Joke:\n\n{final_joke}\n")

def get_url(number):
    category = categories[number]
    return f"https://v2.jokeapi.dev/joke/{category}?type=single"

def get_joke(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data["joke"]

if __name__ == "__main__":
    main()
