enemies= 1

#  1 usage
def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies inside function {enemies}")
    
increase_enemies()
print(f"Enemies outside function {enemies}")