# Project Name
Python - Everything is an Object

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is 
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

### `.txt` Answer Files
- Only one line
- No Shebang on the first line (i.e. “#!/usr/bin/python3”)
- All your files should end with a new line

## Tasks
0. Who am I? What function would you use to print the type of an object? Write the name of the function in the file, without ().

1. Where are you? How do you get the variable identifier (which is the memory address in the CPython implementation)? Write the name of the function in the file, without ().

2. Right count. In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = 100
```

3. Right count. In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = 89
```

4. Right count. In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = a
```

5. Right count =+.
In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = a + 1
```

6. Is equal.
What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

7. Is the same.
What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

8. Is really equal. What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

9. Is really the same.
What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

10. And with a list, is it equal.
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

11. And with a list, is it the same.
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

12. And with a list, is it really equal.
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

13. And with a list, is it really the same.
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

14. List append.
What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

15. List add.
What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

16. Integer incrementation.
What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

17. List incrementation.
What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```


18. List assignation.
What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

19. Copy a list object.
Write a function def copy_list(a_list): that returns a copy of a list.

- The input list can contain any type of objects
- Your file should be maximum 3-line long (no documentation needed)
- You are not allowed to import any module

20. Tuple or not?

`a = ()`
Is a a tuple? Answer with Yes or No.

21. Tuple or not?

`a = (1, 2)`
Is a a tuple? Answer with Yes or No.

22. Tuple or not?

`a = (1)`
Is a a tuple? Answer with Yes or No.

23. Tuple or not?

`a = (1, )`
Is a a tuple? Answer with Yes or No.

24. Who I am?
What does this script print?
```
a = (1)
b = (1)
a is b
```

25. Tuple or not.
What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```

26. Empty is not empty.
What does this script print?
```
a = ()
b = ()
a is b
```

27. Still the same?
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
Will the last line of this script print 139926795932424? Answer with Yes or No.

28. Same or not?
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
Will the last line of this script print 139926795932424? Answer with Yes or No.

