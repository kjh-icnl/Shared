from LinkedList import *


print('\n------- Creation ------')
link = LinkedList()
print(link)

print('\n------- PushBack ------')
link.push_back(1)
link.push_back(5)
link.push_back('c')
link.push_back(True)
print(link)

print('\n------ Insertion ------')
link.insert(2, 'A')
link.insert(0, 'John')
link.insert(3, 3.3)
print(link)

print('\n------ Search ------')
print(link)
print(link.search(3.3))
print(link.search('John'))
print(link.search('abc', False))

print('\n------ Pop ------')
print(link.pop())
print(link)
print(link.pop())
print(link)

print('\n------ Remove ------')
link.remove(0)
print(link)
link.remove(3)
print(link)

print('\n------ Iteration ------')
for i in range(len(link)):
    print(link[i], end = '\t')
print()

print('\n------ Revision ------')
link[0] = 10
print(link)

print('\n------ Connection ------')
print(link)
link2 = LinkedList()
link2.push_back('b')
link2.push_back(False)
link2.push_back(3)
print(link2)
link.update(link2)
print(link)

print('\n------ Clear ------')
link.clear()
print(link)