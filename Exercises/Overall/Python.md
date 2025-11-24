# Python

## Python KeyWords

```python
False, None, True,
and, or, not,
as, assert,
async, await,
break, continue,
class, def, return,
del, pass,
elif, else, if,
except, finally, try, raise,
for, while,
from, import,
global, nonlocal,
in, is,
lambda, yield
```

## Python Built-in Functions

```python
abs(), aiter(), all(), any(), anext(), ascii(),
bin(), bool(), breakpoint(), bytearray(), bytes(),
callable(), chr(), classmethod(), compile(), complex(),
delattr(), dict(), dir(), divmod(),
enumerate(), eval(), exec(),
filter(), float(), format(), frozenset(),
getattr(), globals(),
hasattr(), hash(), help(), hex(),
id(), input(), int(), isinstance(), issubclass(), iter(),
len(), list(), locals(),
map(), max(), memoryview(), min(),
next(),
object(), oct(), open(), ord(),
pow(), print(), property(),
range(), repr(), reversed(), round(),
set(), setattr(), slice(), sorted(), staticmethod(), str(), sum(), super(),
tuple(), type(),
vars(),
zip(),
__import__()
```

## Built-in Types and Important Methods

### String Methods

```python
capitalize, casefold, center, count, encode, endswith,
expandtabs, find, format, index, isalnum, isalpha, isdigit,
islower, isnumeric, isspace, istitle, isupper, join, ljust,
lower, lstrip, partition, replace, rfind, rindex, rjust,
rpartition, rsplit, rstrip, split, splitlines, startswith,
strip, swapcase, title, translate, upper, zfill
```

### List Methods

```python
append, clear, copy, count, extend,
index, insert, pop, remove, reverse, sort
```

### Dictionary Methods

```python
clear, copy, fromkeys, get,
items, keys, values,
pop, popitem, setdefault, update
```

### Set Methods

```python
add, clear, copy, difference, difference_update, discard,
intersection, intersection_update, isdisjoint, issubset,
issuperset, pop, remove, symmetric_difference,
symmetric_difference_update, union, update
```

### Tuple Methods

```python
count, index
```

### File Object Methods

```python
close, read, readline, readlines,
write, writelines, seek, tell, flush
```

## OOP Concepts in Python

1.Class & Object

- Creating classes
- Creating objects
- __init__ constructor

2.Encapsulation

- Private attributes → _attribute, __attribute
- Getters & Setters using @property

3.Inheritance

- Single inheritance
- Multiple inheritance
- Multilevel inheritance
- super() function

4.Polymorphism

- Method overriding
- Method overloading (achieved using default args, not real overloading)

5.Abstraction

- Using abc module
- @abstractmethod

## Operator Overloading

### Arithmetic Operators

```python
__add__(self, other)
__sub__(self, other)
__mul__(self, other)
__truediv__(self, other)
__floordiv__(self, other)
__mod__(self, other)
__pow__(self, other)
```

### Comparison Operators

```python
__eq__(self, other)
__ne__(self, other)
__lt__(self, other)
__le__(self, other)
__gt__(self, other)
__ge__(self, other)
```

### Unary Operators

```python
__neg__(self)  
__pos__(self)  
__abs__(self)   
```

### Memory

```python
__new__(cls, ...)
__init__(self, ...)
__del__(self)
```

### Object Information

```python
type(obj)
id(obj)
dir(obj)
globals()
locals()
vars(obj)
```

### Inheritance Helpers

```python
super()
isinstance(obj, Class)
issubclass(A, B)
```

---
