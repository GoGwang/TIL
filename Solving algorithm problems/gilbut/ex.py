import random
def guessing_game():
    word = random.randint(ord('a'),ord('z')+1)

    while True:
        alphabet = input("알파벳을 입력하세요:")
        if ord(alphabet) > word:
            print("DOWN!")
        elif ord(alphabet) == word:
            print("RIGHT!!!")
            break
        else:
            print("UP!") 

guessing_game()