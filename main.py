import pandas

# student_data_frame = pandas.DataFrame(student_dict)
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # pass

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    # print(row)
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# students = {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
pairs = {row.letter:row.code for (index, row) in data.iterrows()}
# print(pairs)


def create_pairs():
    user_input = input("Write your name: ").upper()
    try:
        output_list = [pairs[letter] for letter in user_input]
    except KeyError:
        print("Please enter ONLY alphabetical characters")
        create_pairs()
    else:
        print(output_list)
        create_pairs()


create_pairs()
