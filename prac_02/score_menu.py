"""CP1404 Practical 2, Score Menu"""
import score


def main():
    print("(G)et Score (0-100)\r\n(P)rint Results\r\n(S)how Stars\r\n(Q)uit")
    user_input = input(">>> ").upper()
    user_score = -1
    while user_input != "Q":
        if user_input == "G":
            user_score = get_valid_score()
        elif user_input == "P":
            if user_score < 0:
                print("No Score has been entered!")
            else:
                score_category = score.get_score_category(user_score)
                print(f"Your score category is: {score_category}")
        elif user_input == "S":
            print_stars(user_score)
        else:
            print("Invalid Input")
        user_input = input(">>> ").upper()
    print("Farewell!")


def get_valid_score():
    user_score = int(input("Enter your Score: "))
    while user_score < 0 or user_score > 100:
        print("Invalid Score!")
        user_score = int(input("Enter your Score: "))
    return user_score


def print_stars(number_of_stars):
    if number_of_stars < 0:
        print("No Score has been entered!")
    else:
        print("*" * number_of_stars)


if __name__ == "__main__":
    main()
