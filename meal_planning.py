import random

choice = random.randint(1,4)
meal = input('breakfast, lunch, dinner, or quit: ')

print(f'we are having {meal}')

while True:

 if choice == 1:

    print('pancakes')
    break

 elif choice == 2:
    
    print('salad')
    break
 elif choice == 3:

    print('chicken')
    break

 elif choice == 4:
    print('quit')
    break 


    
        
