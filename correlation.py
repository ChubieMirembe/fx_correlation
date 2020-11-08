import pandas as pd     

df = pd.read_csv("correlation.csv")
pair_list = df.pair1.unique()
tf_list = list(df.columns[2::].values)

def correlation1(): 

    pair_1 = ''
    pair_2 = ''
    t_frame = ''
    
    while pair_1 not in pair_list:
            pair_1 = input("\nEnter the first pair: ").upper()
               
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
    while pair_1 not in pair_list:
            pair_1 = input("\nEnter the first pair: ").upper()
               
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

    df1 = (df[df.pair1 == (pair_1)])

    for row in df1.index:
        if df1[t_frame][row]> 80 or df1[t_frame][row]< -80:
            print(df1['pair1'][row], df1['pair2'][row], df1[t_frame][row])
        else:
            continue

number = int(input('How many pairs would you like to compare?: '))

if number <=2:
    correlation1() 
else:
    correlation2()
