class Game:
    
    ##########################################################################"
    # The game contructer
    def __init__(self):
        print('Welcome To Ra-Games.')
        print('Type \'EO\' to play the Even-Odd number game.\nType \'SA\' to play the Sum-Average game.\nType \'MT\' to play the Multiplication Table Game.')
        self.choices()

    ##########################################################################"
    # The available choices
    def choices(self):
        select = input()

        if select == 'EO':
            self.Even_Odd_Game()
        elif select == 'SA':
            self.Sum_Average_Game()
        elif select == 'MT':
            self.Multiplacation_Table()
        else:
            print('Please type a valid keyword')
            self.choices()

    ##########################################################################"
    # The Even-Odd game code
    def Even_Odd_Game(self):
        print('Welcome To Even Odd number game')
        print('If you want to close the game type \'x\'')

        while True:
            number = input('Please enter a number')
            if number == 'X':
                print('Closing ...')
                break
            try:
                if int(number) % 2 == 0:
                    print('Its an even!')
                else:
                    print('Its an odd!')
            except ValueError:
                print('Please enter a Valid Number.')

    ##########################################################################"
    # The Sum-Average game code
    def Sum_Average_Game(self):
        print('Welcome to Sum-Average game! ')
        numbers = input('Please enter the numbers that you would\n')
        L_numbers = numbers.split(' ')
        sum = 0
        i = 0

        while i < len(L_numbers):
            sum += int(L_numbers[i])
            i += 1
        average = sum / len(L_numbers)
        print('The total of these numbers is : ' , sum)
        print('The average of these numbers is : ',average)

    # The Multiplication-Table game code
    def Multiplacation_Table(self):
        print('Welcome to the multiplication table')
        print('Please enter your first and last number')
        x = int(input('Enter your first number \n'))
        y = int(input('Enter your last number \n'))

        for x in range(x, y + 1):
            for y in range(1, 11):
                print(x, '×', y, '=', x * y)
            print('------------------')

##########################################################################
# Creating our first object
game1 = Game()
