# #FileNotFound
# with open("a_file.txt") as file:
#     file.read())

# #KeyError
# a_dictionay = {"key": "value"}
# value = a_dictionay["non_existent_key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

# File not found

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sfdsfd"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("algo")
# except KeyError as error_message:
#     print(f"The Key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that i made up")

#BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
