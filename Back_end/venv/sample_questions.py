import random
#import time
#from app import db
#from models import User,Score



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

   
    
def Get_questions(player_name, age, sub_level):
    questions_arr=[]
    
    # Get player's name
    if not player_name:
        player_name = input("Please enter a valid name: ").strip()

    if age < 5:
        print("This game is for ages 5 and above.")
        
    age_level = get_level_by_age(age)
    
    if sub_level<1:
        sub_level=1

    for _ in range(5):  # Ask 5 questions
        question, answer = generate_problem(age_level, sub_level)

        questions_arr.append(
            {
                "question":question,
                "answer": answer
            }
        )
    print(questions_arr)
    return questions_arr





    

