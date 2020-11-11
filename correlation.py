'''
This is a simple program that shows the correlation between different forex pairs
on different time frames.
'''

import pandas as pd

df = pd.read_csv("correlation.csv")
pair_list = df.pair1.unique()
tf_list = list(df.columns[2::].values)

def correlation1():
    '''
    Function to compare 2 specific pairs
    '''

    pair_1 = ''
    pair_2 = ''
    t_frame = ''

    while pair_1 not in pair_list:
        pair_1 = input("\nEnter the First pair: ").upper()

        if pair_1 not in pair_list:
            print("Input isn't valid! Try again")
        else:
            continue

    while pair_2 not in pair_list:
        pair_2 = input("\nEnter the Second pair: ").upper()

        if pair_2 not in pair_list:
            print("Input isn't valid! Try again")
        else:
            continue

    while t_frame not in tf_list:
        t_frame = input("\nEnter the Time frame: ").lower()

        if t_frame not in tf_list:
            print("Input isn't valid! Try again")
        else:
            continue

    df1 = (df[df.pair1 == (pair_1)])
    df2 = (df1[df1.pair2 == (pair_2)])

    for row in df2.index:
        corr = df2[t_frame][row]
        print(f"\nThe correlation betweeen {pair_1} and {pair_2} is {corr}")

def correlation2():
    '''
    Function to check all the correlations with one pair
    '''

    pair_1 = ''
    t_frame = ''

    while pair_1 not in pair_list:
        pair_1 = input("\nEnter the pair: ").upper()

        if pair_1 not in pair_list:
            print("Input isn't valid! Try again")
        else:
            continue

    while t_frame not in tf_list:
        t_frame = input("\nEnter the Time frame: ").lower()

        if t_frame not in tf_list:
            print("Input isn't valid! Try again")
        else:
            continue

    df1 = (df[df.pair1 == (pair_1)]).sort_values(by=t_frame, ascending=False)

    for row in df1.index:
        if df1[t_frame][row] > 80 or df1[t_frame][row] < -80:
            print(df1['pair1'][row], df1['pair2'][row], df1[t_frame][row])
        else:
            continue

while True:
    while True:
        try:
            number = int(input("What would you like to do?: \n(1) Compare 2 pairs \n (2) See all the correlations of one pair \n"))
        except ValueError:
            print("The input needs to be '1' or '2'")
            continue
        else:
            if number in (1, 2):
                break
            else:
                print("The input needs to be '1' or '2'")

    if number == 1:
        correlation1()
    elif number == 2:
        correlation2()

    while True:
        try:
            CHECKING = str(input("Would you like to check another pair? \n 'Yes' or 'No' \n"))
        except ValueError:
            print("You need to enter 'Yes' or 'No'")
            continue
        else:
            if CHECKING[0].lower() == 'y' or CHECKING[0].lower() == 'n':
                break
            else:
                print("You need to enter 'Yes' or 'No'")

    if CHECKING[0].lower() == 'y':
        CHECKING = True
        continue
    elif CHECKING[0].lower() == 'n':
        print("\nGoodbye!")
        break
    