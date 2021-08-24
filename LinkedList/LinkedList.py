class NotFoundValue(Exception):
    pass

class LinkedList:
    class _Node:
        __slots__ = '_element', '_prev', '_next'
        def __init__(self, elem = None, prev = None, next = None) -> None:
            self._element = elem
            self._prev = prev
            self._next = next

    __slots__ = '_node', '_size'
    def __init__(self) -> None:
        self._node = None
        self._size = 0

    def __len__(self):
        return self._size

    def push_back(self, value):
        """
        Return None
        The given value is stored at the last node additionally.

        (For Example)
        a <-> b <-> c
        A result of push_back(d) is
        a <-> b <-> c <-> d
        """
        if self._node == None:
            self._node = self._Node(value)
        else:
            self._push_back(self._node, value)
        self._size +=1
    
    def _push_back(self, node, value):
        if node._next == None:
            node._next = self._Node(value, prev=node)
        else:
            self._push_back(node._next, value)

    def insert(self, p, v):
        """
        insert the given value in pos-th index
        
        (For example)
        [Structure] a <--> b <--> c
        A result of insert(1, d) is
        [Structure] a <--> d <--> b <--> c

        The values after pos-th index value are pushed by one index
        """
        if p > self._size-1 or p < 0:
            raise IndexError
        self._size += 1
        self._insert(self._node, p, v)

    def _insert(self, node, p, v):
        if p == 0:
            node = self._Node(v, node._prev, node)
            if node._prev is not None:
                node._prev._next = node
                node._next._prev = node
            else:
                self._node = node
        else:
            self._insert(node._next, p-1, v)

    def pop(self):
        if self._size-1 < 0:
            raise IndexError

        self._size -= 1
        return self._pop(self._node)

    def _pop(self, node):
        if node._next != None:
            return self._pop(node._next)
        else:
            val = node._element
            node._prev._next = None
            return val
            
    def remove(self, p):
        """
        Return None
        Remove a value of the p-th index
        
        (For example)
        [Structure] a <--> b <--> c
        A result of remove(1) is
        [Structure] a <--> c

        The values after pos-th index value are pulled by one index
        """
        if p > self._size -1 or p < 0:
            raise IndexError
        self._size -= 1
        self._remove(self._node, p)

    def _remove(self, node, p):
        if p == 0:
            if node._prev is None:
                self._node = node._next
            elif node._next is None:
                self.pop()
                self._size += 1
            else:
                node._prev._next = node._next
                node._next._prev = node._prev
        else:
            self._remove(node._next, p-1)

    def search(self, val, err = True):
        """
        Return an index of the value (If successful)
        Search the index of the given value
        If it fails to search the value, it will raise NotFoundValue error
        when the argument err is True.
        
        (For example)
        a <--> b <--> c
        A result of search('a') is
        [return] 0
        A result of search('d', err = False) is
        [return] None

        I won't raise NotFoundValue error when the argument err is False.
        """
        if err:
            result = self._search(val)
            if result is not None:
                return result
            else:
                raise NotFoundValue
        return self._search(val)
                    
    def _search(self, val):
        for p, e in enumerate(self):
            if e == val:
                return p
        return None
            
    def __getitem__(self, p):
        for i, v in enumerate(self):
            if p == i:
                return v
    
    def __setitem__(self, p, val):
        if p > self._size - 1 or p < 0:
            raise IndexError
        else:
            self._setitem(self._node, p, val)
    
    def _setitem(self, node, p, val):
        if p == 0:
            node._element = val
        else:
            self._setitem(node._next, p-1, val)

    def __iter__(self):
        for e in LinkedList._iterate(self._node):
            yield e._element
    
    def _iterate(node):
        if node != None:
            yield node
        if node._next != None:
            for e in LinkedList._iterate(node._next):
                yield e

    def __repr__(self):
        string = '[ '
        try:
            for p, n in enumerate(self):
                if p == len(self) - 1:
                    string += f'{n} ]'
                    break
                else:
                    string += f'{n}, '
        except AttributeError:
            string += ']'
        return string

    def clear(self):
        self._node = None

    def update(self, lst):
        if type(lst) != LinkedList:
            raise TypeError
        l_node = self._last_node(self._node)
        l_node._next = lst._node
        lst._node._prev = l_node
        self._size += len(lst)
        
    def _last_node(self, node):
        if node._next != None:
            return self._last_node(node._next)
        else:
            return node