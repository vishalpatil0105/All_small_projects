import pandas


nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(nato_dict)
is_true = True

while is_true:
    user_input = input("Enter Your Name: ").upper()
    try:
        nato_name_list = [nato_dict[word] for word in user_input]
    except KeyError:
        print(f"Please enter valid string")
    else:
        is_true = False
        print(nato_name_list)


