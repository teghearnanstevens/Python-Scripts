def calculate_score():
  
    positive_scores = {'A': 3, 'a': 2, 'd': 1, 'D': 0}
    negative_scores = {'A': 0, 'a': 1, 'd': 2, 'D': 3}

    questions = [
        ("I feel that I am a person of worth, at least on an equal plane with others.", 'positive'),
        ("I feel that I have a number of good qualities.", 'positive'),
        ("All in all, I am inclined to feel that I am a failure.", 'negative'),
        ("I am able to do things as well as most other people.", 'positive'),
        ("I feel I do not have much to be proud of.", 'negative'),
        ("I take a positive attitude toward myself.", 'positive'),
        ("On the whole, I am satisfied with myself.", 'positive'),
        ("I wish I could have more respect for myself.", 'negative'),
        ("I certainly feel useless at times.", 'negative'),
        ("At times I think I am no good at all.", 'negative')
    ]

    score = 0 

    print("This program is an implementation of the Rosenberg Self-Esteem Scale.")
    print("Please rate how much you agree with each of the following statements by responding with:")
    print("A = Strongly Agree, a = Agree, d = Disagree, D = Strongly Disagree\n")

    for i, (question, q_type) in enumerate(questions, start = 1):
        response = input(f"{i}. {question}\n   Enter D, d, a, or A: ").strip()

        while response not in ['A', 'a', 'd', 'D']:
            response = input("Invalid input. Please enter D, d, a, or A: ").strip()

        if q_type == 'positive':
            score += positive_scores[response]
        else:
            score += negative_scores[response]

    print(f"\nYour score is {score}.")

    if score < 15:
        print("A score below 15 may indicate problematic low self-esteem.")
    elif score <= 25:
        print("Your self-esteem is within the normal range.")
    else:
        print("You have high self-esteem.")

calculate_score()