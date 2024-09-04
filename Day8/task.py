"""
* I was reading this article by Tim Urban - Your Life in Weeks and realised just 
how little time we actually have.
* Create a function called life_in_weeks() using maths and f-Strings that 
tells us how many weeks we have left, if we live until 90 years old.
* It will take your current age as the input and output a message with our time left in this format:
* You have x weeks left.
* Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
* **Warning** The function must be called life_in_weeks for the tests to pass. Also the output must have the same punctuation and spelling as the example. Including the full stop!

* Example Input: 56
* Example Output: You have 1768 weeks left.
"""

def life_in_weeks(current_age):
    
    current_age= int(current_age)
    years_remaining= 90 - current_age
    weeks_left = years_remaining * 52

    print(f"You have {weeks_left} weeks left.")

# Example usage
print(life_in_weeks(20))
print(life_in_weeks(40))
print(life_in_weeks(56))
print(life_in_weeks(70))

"""_summary_
Love Calculator
💪 This is a difficult challenge! 💪 
You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.

name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times 
R occurs 1 time 
U occurs 2 times 
E occurs 2 times 

Total = 5 

L occurs 1 time 
O occurs 0 times 
V occurs 0 times 
E occurs 2 times 

Total = 3 

Love Score = 53

Example Input : calculate_love_score("Kanye West", "Kim Kardashian")
Example Output: 42
"""

def calculate_love_score(name1, name2):
    # Combine both names into one string
    combined_names = name1 + name2
    # Convert the combined string to lowercase
    combined_names = combined_names.lower()
    
    # Calculate the number of times each letter in "TRUE" occurs
    t_count = combined_names.count('t')
    r_count = combined_names.count('r')
    u_count = combined_names.count('u')
    e_count = combined_names.count('e')
    true_total = t_count + r_count + u_count + e_count
    
    # Calculate the number of times each letter in "LOVE" occurs
    l_count = combined_names.count('l')
    o_count = combined_names.count('o')
    v_count = combined_names.count('v')
    e_count = combined_names.count('e')
    love_total = l_count + o_count + v_count + e_count
    
    # Combine the totals to form a two-digit number
    print(f"{true_total}{love_total}")
    

# Example usage
print(calculate_love_score("Kanye West", "Kim Kardashian"))

