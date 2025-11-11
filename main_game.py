import random

print("Welcome to the Hangman game!")

list_of_words = [
    "banana",
    "monkey",
    "zoom",
    "cat",
    "dog",
    "avocado",
    "epic"
    "stone"
]

def choose_a_random_word(word_list: list):
    len_of_list = len(word_list)
    random_index = random.randint(a=0, b=len_of_list - 1)
    return word_list[random_index]


def print_hidden_word(word):
    ...

def get_input_from_user(letter_from_input: str):
    letter_from_input = str(input("please enter a letter"))
    if letter_from_input.isalpha():



if __name__ == '__main__':

    print(choose_a_random_word(list_of_words))
