from anime_list import animes
import random
import art
print(art.logo)
score = 0
lives = 1
game = False
A = random.choice(animes)
B = random.choice(animes)
while not game:
    print(f"Compare A: {A['name']} was released in {A['release_year']} and has {A['number_of_episodes']} episodes")
    print(art.vs)
    print(f"Compare B: {B['name']} was released in {B['release_year']} and has {B['number_of_episodes']} episodes")

    answer = input('Which anime has more rating? A or B: ').lower()
    if A['rating'] > B['rating'] and answer == 'a':
        score += 1
        print(f'The rating of {A['name']} is {A['rating']}')
        print(f'The rating of {B['name']} is {B['rating']}')
        print(f'your current score is {score}')
        B = random.choice(animes)
    elif A['rating'] > B['rating'] and answer == 'b':
        lives -= 1
        print("Sorry that's wrong answer")
        print(f"Your final score is {score}")
        print(f'The rating of {A['name']} is {A['rating']}')
        print(f'The rating of {B['name']} is {B['rating']}')
        break
    elif A['rating'] < B['rating'] and answer == 'a':
        lives -= 1
        print("Sorry that's wrong answer")
        print(f'Your final score is {score}')
        print(f'The rating of {A['name']} is {A['rating']}')
        print(f'The rating of {B['name']} is {B['rating']}')
        break
    elif A['rating'] < B['rating'] and answer == 'b':
        score += 1
        print(f'your current score is {score}')
        print(f'The rating of {A['name']} is {A['rating']}')
        print(f'The rating of {B['name']} is {B['rating']}')
        A = B
        B = random.choice(animes)
    else:
        print("Wrong input! Try again!")
