from random import choice
import sys
class Namegenerator:
    def __init__(self):
        self.prefixes=[]
        self.sufixes=[]
    def getting_prefixes_sufixes_values(self):
        print(f"Name generator...!")
        for value in range(1,6):
            getting_prefixes=input(f"Enter prefix_value{value}: ")
            while not getting_prefixes.isalpha():
                print(f"Enter a valid input..")
                getting_prefixes=input(f"Enter prefix_value{value}: ")
                self.prefixes.append(getting_prefixes)
            self.prefixes.append(getting_prefixes)
          
            getting_sufixes=input(f"Enter sufixes_value{value}: ")
            while not getting_sufixes.isalpha():
                print(f"Enter a valid input..")
                getting_sufixes=input(f"Enter sufixes_value{value}: ")
                self.sufixes.append(getting_sufixes)
            self.sufixes.append(getting_sufixes)
                    
    def name_generating(self):
        prefixes=choice(self.prefixes)
        sufixes=choice(self.sufixes)
        generated_name=prefixes+sufixes
        return f"{val}. {generated_name}"
obj=Namegenerator()
obj.getting_prefixes_sufixes_values()
print(f"Generated name..")
for val in range(1,6):
    print(obj.name_generating())
getting_choice=input("Do you want to  continue this funny  name generator..[yes\no]")
if getting_choice.casefold()=="yes":
    obj=Namegenerator()
    obj.getting_prefixes_sufixes_values()
    for val in range(1,6):
        print(obj.name_generating())
elif getting_choice.casefold()=="no":
    print("name generator is going to exit....")
    sys.exit()
else:
    print("Enter a  valid input")
    sys.exit()
    
            
            
            
        
