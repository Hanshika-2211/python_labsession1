# Write a code to generate a roll no randamly and add it to a dictionary hvaing those roll no as the key values 
import random
a=str(input("Enter the name:"))
age=int(input("Enter your age:"))
email=str(input("Enter your email:"))
def myname(a,age,email):
    return a,age,email
def generate_rollnumber():
    return random.randint(1, 46) 
def add_to_dictionary(dictionary, roll_number):
    dictionary[roll_number] = myname(a,age,email)
student_dict = {}
roll_no = generate_rollnumber()
add_to_dictionary(student_dict, roll_no)
print("Generated Roll Number:", roll_no)
print("Student Dictionary:", student_dict)