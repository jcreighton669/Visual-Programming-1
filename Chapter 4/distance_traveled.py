speed = int(input('What is the speed of the vehicle in MPH? '))
hours = int(input('How many hours has it traveled? '))

print('Hours\t\tDistance')

for i in range(1, hours+1):
    distance = i * speed
    print(i, '\t\t', distance, 'miles')
