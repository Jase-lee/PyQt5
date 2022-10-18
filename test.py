import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit(111)
print('You typed ' + response + '.')