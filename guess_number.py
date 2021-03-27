def guess_the_number():
    my_list = [69, 420, 46, 11, 1993]
    your_input = input('Guess my secret number: ')
    
    while your_input.lower() != 'q':
        try:
            if int(your_input) in my_list:
                print('You got it right! Thanks for playing!')
                break
            else:
                your_input = input('Wrong. Guess again, my friend. ')
        except ValueError:
            print('Please type an integer or q to quit.')
            your_input = input('Try again. ')
    if your_input.lower() == 'q':
        print('You pressed [q] to quit. Thanks for playing!') 
        
guess_the_number()