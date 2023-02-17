def y_n_inputValidation(userInput):
    while True:
        if userInput == 'y' or userInput == 'n' or userInput == 'Y' or userInput == 'N':
            break
        else:
            userInput = input('Please answer the question again using only \"y\" or \"n\": ')
            continue
    return userInput.lower

def calculateTime():
    
    # This first line is provided for you
    monkey_one = input("Is the first monkey smiling? (y/n): ")
    m1 = y_n_inputValidation(monkey_one)
    monkey_two = input("Is the second monkey smiling? (y/n): ")
    m2 = y_n_inputValidation(monkey_two)
    if m1 != m2: print('Yay! We\'re going to have a good day!')
    else: print('Uh Oh! We\'re in trouble!')
    # end assignment

## If you want to test locally run > python monkeyCalculator.py

if __name__ == "__main__":
    calculateTime()
    