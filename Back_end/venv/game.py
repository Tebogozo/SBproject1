import random
import time
from app import db
from models import User,Score


def get_level_by_age(age):
    """Assigns an age range category"""
    if age < 8:
        return 1  # Age 5-7
    elif age < 11:
        return 2  # Age 8-10
    else:
        return 3  # Age 11+

def generate_problem(age_level, sub_level):
    """Generates a problem based on age range and sub-level"""
    
    operations = ['+', '-']
    num_range = (1, 10)

    if age_level == 1:  # Ages 5-7
        if sub_level == 2:
            num_range = (1, 20)
        elif sub_level == 3:
            num_range = (1, 10)
            operations.append('*')

    elif age_level == 2:  # Ages 8-10
        num_range = (10, 50)
        operations.append('*')
        if sub_level == 2:
            operations.append('/')
        elif sub_level == 3:
            num_range = (10, 100)

    else:  # Ages 11+
        num_range = (50, 100)
        operations.extend(['*', '/'])
        if sub_level == 2:
            num_range = (50, 200)
        elif sub_level == 3:
            num_range = (50, 500)

    num1 = random.randint(*num_range)
    num2 = random.randint(*num_range)
    operation = random.choice(operations)

    if operation == '/':
        num1 = num1 - (num1 % num2)
        if num2 == 0:
            num2 = 1

    question = f"{num1} {operation} {num2} = ?"
    answer = eval(str(num1) + operation + str(num2))
    return question, answer

def assign_badge(score):
    """Assigns a badge based on the score"""
    if score == 5:
        return "🥇 Gold Badge!"
    elif score == 4:
        return "🥈 Silver Badge!"
    elif score == 3:
        return "🏅 Bronze Badge!"
    else:
        return None

def main():
    print("Welcome to the Arithmetic Drill!")

    # Get player's name
    player_name = input("Enter your name: ").strip()
    while not player_name:
        player_name = input("Please enter a valid name: ").strip()
    
    print(f"Hello, {player_name}! Let's get started.")

    while True:
        try:
            age = int(input(f"{player_name}, enter your age: "))
            if age < 5:
                print("This game is for ages 5 and above.")
                continue
            break
        except ValueError:
            print("Please enter a valid age.")

    age_level = get_level_by_age(age)
    print(f"{player_name}, you are in Age Level {age_level}!")

    sub_level = 1

    while True:
        print(f"\nStarting Age Level {age_level}, Sub-Level {sub_level}...")
        score = 0
        correct_streak = 0
        start_time = time.time()

        for _ in range(5):  # Ask 5 questions
            question, answer = generate_problem(age_level, sub_level)
            print(question)
            question_start = time.time()
            user_answer = input("Your answer: ")

            try:
                if float(user_answer) == answer:
                    elapsed_time = time.time() - question_start
                    print(f"Correct, {player_name}!")
                    score += 1
                    correct_streak += 1
                    if elapsed_time < 5:
                        print("🚀 Fast Thinker Bonus!")
                else:
                    print(f"Oops! The correct answer is {answer}.")
                    correct_streak = 0
            except ValueError:
                print("Please enter a valid number.")
                correct_streak = 0

        total_time = time.time() - start_time

        print(f"\n{player_name}, your final score is {score}/5!")
        badge = assign_badge(score)
        if badge:
            print(f"🏆 Congratulations, {player_name}! You earned a {badge}")

        if correct_streak == 5:
            print("🎯 Amazing! You got 5 correct in a row! Accuracy Master!")

        print(f"⏳ Total time taken: {total_time:.2f} seconds.")

        # Progression logic
        if score >= 4 and sub_level < 3:
            sub_level += 1
            print(f"Great job, {player_name}! Moving to the next sub-level.")
        elif score <= 1 and sub_level > 1:
            sub_level -= 1
            print(f"Don't give up, {player_name}! Moving to an easier sub-level.")
        else:
            print(f"{player_name}, you're staying at the current sub-level.")

        # Ask if the player wants to continue
        cont = input(f"\n{player_name}, do you want to play again? (yes/no): ").lower()
        if cont != 'yes':
            print(f"Thanks for playing, {player_name}! See you next time. 👋")
            break

def save_score(player_name, player_age, score, badge, correct_streak, total_time):
    """Function to save player score to the database"""
    # Find or create the user in the database
    user = User.query.filter_by(name=player_name).first()
    if not user:
        # Create the user if not found
        user = User(name=player_name, age=player_age)
        db.session.add(user)
        db.session.commit()

    # Save the score
    user_score = Score(
        score=score,
        badge=badge,
        correct_streak=correct_streak,
        total_time=total_time,
        user_id=user.id
    )
    db.session.add(user_score)
    db.session.commit()

    print(f"Score saved for {player_name} with {score}/5!")

if __name__ == "__main__":
    main()


