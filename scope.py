spam = 42

def eggs():
    spam = 99
    print('In eggs():', spam)

def ham():
    print('In ham():', spam)

def bacon():
    global spam
    print('In bacon():', spam)
    spam = 0

def CRASH():
    print(spam)
    spam = 0

print(spam)
eggs()
print(spam)
ham()
print(spam)
bacon()
print(spam)
CRASH()
