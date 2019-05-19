x = 1
if x == 1:
    print("x is 1.")

if x == 1 and 5 > 3:
    print("Print this.")

myfloat = float(7)
print(myfloat)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

x = 5 + 6 + 2 - 9 / 6 * 3
a, b = 3, 4
print(a,b)

mylist = []
mylist.append(1)

cubed = 2 ** 3
print(cubed)

x = object()
y = object()
x_list = [x]
y_list = [y]
big_list = []

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

astring = "Hello world!"
print(astring.index("o"))

x = 2
print(x == 2) # prints out True
print(x is y)
print((not False) == (False))

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed")

def list_benefits():
    pass

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))