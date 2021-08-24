# Introduction
Thank you for searching my implementation about Linked-List. This implementation is written by Python. However, I am getting ready to provide it of **C++** version and did not publish this implementation on **PyPI**. I will release it on PyPI soon. Thank you for waiting for it.

***LinkedList.py*** has an ultimate implementation of the linked list. ***main.py*** has detailed examples of this implementation.

# Requirements
Python >= 3.7.x

# Usage
### import
```python
>>> from LinkedList import *
```
### Creation
```python
>>> link = LinkedList()
>>> print(link)
[ ]
```

### Push Back
```python
>>> link.push_back(1)
>>> link.push_back(5)
>>> link.push_back('c')
>>> link.push_back(True)
>>> print(link)
[ 1, 5, c, True ]
```

### Insertion
```python
>>> link.insert(2, 'A')
>>> link.insert(0, 'John')
>>> link.insert(3, 3.3)
>>> print(link)
[ John, 1, 5, 3.3, A, c, True ]
```

### Search
```python
>>> print(link)
[ John, 1, 5, 3.3, A, c, True ]
>>> print(link.search(3.3))
3
>>> print(link.search('John'))
0
>>> print(link.search('abc', False))
None
```

### Pop
```python
>>> print(link.pop())
True
>>> print(link)
[ John, 1, 5, 3.3, A, c ]
>>> print(link.pop())
c
>>> print(link)
[ John, 1, 5, 3.3, A ]
```

### Remove
```python
>>> link.remove(0)
>>> print(link)
[ 1, 5, 3.3, A ]
>>> link.remove(3)
>>> print(link)
[ 1, 5, 3.3 ]
```

### Iteration
```python
>>> for i in range(len(link)):
...     print(link[i], end = '\t')
1       5       3.3
```

### Revision
```python
>>> link[0] = 10
>>> print(link)
[ 10, 5, 3.3 ]
```

### Connection
```python
>>> print(link)
[ 10, 5, 3.3 ]
>>> link2 = LinkedList()
>>> link2.push_back('b')
>>> link2.push_back(False)
>>> link2.push_back(3)
>>> print(link2)
[ b, False, 3 ]
>>> link.update(link2)
>>> print(link)
[ 10, 5, 3.3, b, False, 3 ]
```

### Clear
```python
>>> link.clear()
>>> print(link)
[ ]
```

### Help
```python
>>> from LinkedList import *
>>> help(LinkedList)
Help on class LinkedList in module LinkedList:

class LinkedList(builtins.object)
 |  LinkedList() -> None
 |
 |  Methods defined here:
 |
 |  __getitem__(self, p)
 |
 |  __init__(self) -> None
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __iter__(self)
 |
 |  __len__(self)
 |
 |  __repr__(self)
 |      Return repr(self).
 |
 |  __setitem__(self, p, val)
 |
 |  clear(self)
 |
 |  insert(self, p, v)
 |      insert the given value in pos-th index
 |
 |      (For example)
 |      [Structure] a <--> b <--> c
 |      A result of insert(1, d) is
 |      [Structure] a <--> d <--> b <--> c
 |
 |      The values after pos-th index value are pushed by one index
-- More --
```


# Issues
If there is any issue, post your issue on the **Issues** section. I will try to find causes of the problems and resolve them.
