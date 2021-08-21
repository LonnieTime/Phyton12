print("Loading.")
print("Loading..")
print("Loading...")
print("Welcome to your Robot Assistant")


class Profile:
    def __init__(self, robot_name, age, job):
        self.robot_name = robot_name
        self.age = age
        self.job = job

    def profile_display(self):
        print("My name is: " + self.robot_name)
        print("My age is: " + self.age)
        print("My job is: " + self.job)


'''
user1 = Profile()
user1.name = "Serina"
user1.age = "100 years old"
user1.job = "Assist Humans With Daily Tasks"
user1.profile_display()
'''

print("Let Me Get To Know You More")
name = input("Enter your name here: ")
print("Thats\n A \n Very \n Cool\n Name!")
print("Its nice to meet you...")
print(name)
print("I have 3 different settings for different ages")
print("This Includes")
list = ["Kid", "Adult", "Senior"]
print(list)
print("Are You A Kid?")
true_or_false = input("True Or False (UpperCase First Letter) ")
if true_or_false == "True":
    print("Ok kid mode will be activated")
elif true_or_false == "False":
    print("Settings Will Remain The Same")
print("One Last Question")
last_question = input("Do you want to be my friend? (UpperCase First Letter)")
if last_question == "no":
    print(":(")
elif last_question == "yes":
    print(":)")
else:
    print("I was looking for no or yes answer")
print("Anyways Now That everything is done we can now commence!")
print(name)
file.open("Phyton2")
