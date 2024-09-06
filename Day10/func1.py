# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())

# def format_name(f_name, l_name):
#     formated_f_name= f_name.title()
#     formated_l_name= l_name.title()
#     print(f"{formated_f_name} {formated_l_name}")


# def format_name(f_name, l_name):
#     formated_f_name= f_name.title()
#     formated_l_name= l_name.title()
    
#     return f"Result: {formated_f_name} {formated_l_name}"

def format_name(f_name:str="Wasiq", l_name:str="Zainul") -> str:
    """"
    Take a first and last name and format it to 
    return the title case version of name
    """
    
    formated_f_name= f_name.title()
    formated_l_name= l_name.title()
    
    return f"Result: {formated_f_name} {formated_l_name}"

# print(format_name(f_name= "mohammad", l_name= "wasiq"))
print(format_name())
# print(format_name(input("What is your first name? "), input("What is your last name? ")))