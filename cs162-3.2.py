#At the REPL, typing `type(x)` will show what type of variable `x` is, while `dir(x)` will reveal all the methods that x has.
#Investigate the default behavior t.  Examine the behavior that python gives a using the following few lines of code:

class BlankClass(object):
    '''This is a Blank class for CS162.'''
    pass
t = BlankClass()

class ClassWithAttr(object):
    x1 = 1
    x2 = 2

my_attr = ClassWithAttr()
my_attr.x3 = 3

print('1.')
print(help(t))
print('\n2.')
print(type(t))
print('\n3.')
print(dir(t))
print('\n4.')
print(hash(t))
print('\n5.')
print(id(t))
print('\n6.')
print(hasattr(my_attr,'x3'))
print('\n7.')
print(getattr(my_attr,'x3'))
print('\n8.')
print(delattr(my_attr,'x3'))
print('\n9.')
print(vars(my_attr))
print('\n10.')
print(bool(t))

# Now find out about the following methods:
#  1. help(t)
#  2. type(t)
#  3. dir(t)
#  4. hash(t)
#  5. id(t)
#  6. hasattr(my_attr,'x3')
#  7. getattr(my_attr,'x3')
#  8. delattr(my_attr,'x3')
#  9. vars(my_attr)
# 10. bool(t)

# *Come to class able to give clear explanations of what is going on in each of
# the above methods, and when one might use them.*
