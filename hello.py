fruits=['apple','orange','banana']
#if fruits[0] == 'apple':
#    print('I love apple')

#for fruit in fruits:
#    print('Hello! I am a ' + fruit)

def fruitsNames(name):
    print("Hi!" + name)
    for fruit in fruits:
         if fruit == 'apple':
             print('I love apple')
         print('Hello! I am a ' + fruit)
fruitsNames('Sol')
