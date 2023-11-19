"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """Main Function for Score Categorising Function"""
    score = float(input("Enter score: "))
    score_category = get_score_category(score)
    print(score_category)
    random_score = random.randint(0, 100)
    random_score_category = get_score_category(random_score)
    print(f"Random Score Category is: {random_score_category}")


def get_score_category(score):
    """Categories the Score"""
    if score < 0 or score > 100:
        score_category = "Invalid Score"
    elif score >= 90:
        score_category = "Excellent"
    elif score >= 50:
        score_category = "Passable"
    else:
        score_category = "Bad"
    return score_category


if __name__ == "__main__":
    main()
