#!/ usr / bin / env python3
# Created By : Fred
# Date : Feb 18 2008
# calculates square of numbers.

import math


def main():
    usernum_str = input("Enter an integer : ")

    try:
        user_num = int(usernum_str)
        if user_num < 0:
            print(
                "{} is not a positive integer. Please, enter a new one".format(user_num)
            )

        else:
            for counter in range(user_num + 1):
                square_ans = pow(counter, 2)
                print("{}^2 = {}".format(counter, square_ans))

    except ValueError:
        print("{} is not a valid integer. Please, enter a new one.".format(usernum_str))


print("Thanks for using the code")

if __name__ == "__main__":

    main()
