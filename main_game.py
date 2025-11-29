from game_functions import (
    game_setup,
    display_and_feedback,
    input_and_validations,
    game_logic,
    game_state
)

word_list = [
    "banana",
    "monkey",
    "zoom",
    "cat",
    "dog",
    "avocado",
    "epic",
    "melon",
    "tomato"
]

all_letters = "abcdefghijklmnopqrstuvwxyz"
MAX_NUMBER_OF_GUESSES = 6

def main():
    print("\nWelcome to the Hangman game!\n")


    secret_word = game_setup.choose_random_word(word_list)
    print("The secret word is:", secret_word)

    secret_letters_to_be_guessed = game_setup.initialize_letters_to_be_guessed(secret_word)

    list_of_alphabet_letters = game_setup.initialize_alphabet_display(all_letters)

    incorrect_guesses_count = 0

    user_guessed_letters = set()

    display_and_feedback.display_game_status(
        letters_alphabet = list_of_alphabet_letters,
        guessed_letters = user_guessed_letters,
        hidden_word = secret_word,
        attempts_remain = (MAX_NUMBER_OF_GUESSES - incorrect_guesses_count)
        )

    letter_from_input = input_and_validations.get_valid_guess(guessed_letters=user_guessed_letters)
    game_logic.update_letters_to_be_guessed(user_guessed_letters, letter_from_input)

    if game_logic.check_letter_in_word(letter_from_input, secret_word):
        # correct guess
        # remove the correct letter from the secret_letters_to_be_guessed
        game_logic.update_letters_to_be_guessed(user_guessed_letters, letter_from_input)
    else:
        # wrong guess
        # add +1 to wrong guesses
        incorrect_guesses_count += 1

    display_and_feedback.display_game_status(
        letters_alphabet=list_of_alphabet_letters,
        guessed_letters=user_guessed_letters,
        hidden_word=secret_word,
        attempts_remain=MAX_NUMBER_OF_GUESSES - incorrect_guesses_count
    )


    while not game_state.is_game_over(
        hidden_letters=secret_letters_to_be_guessed,
        attempts_remaining=MAX_NUMBER_OF_GUESSES - incorrect_guesses_count
    ):

        letter_from_input = input_and_validations.get_valid_guess(guessed_letters=user_guessed_letters)
        game_logic.update_letters_to_be_guessed(user_guessed_letters, letter_from_input)

        if game_logic.check_letter_in_word(letter_from_input, secret_word):
            # correct guess
            # remove the correct letter from the secret_letters_to_be_guessed
            game_logic.update_letters_to_be_guessed(secret_letters_to_be_guessed, letter_from_input)
        else:
            # wrong guess
            # add +1 to wrong guesses
            incorrect_guesses_count += 1

        display_and_feedback.display_game_status(
            letters_alphabet=list_of_alphabet_letters,
            guessed_letters=user_guessed_letters,
            hidden_word=secret_word,
            attempts_remain=MAX_NUMBER_OF_GUESSES - incorrect_guesses_count
        )

if __name__ == "__main__":
    main()
