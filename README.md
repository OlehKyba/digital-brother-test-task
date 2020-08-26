# Test assignments for the Junior Python Developer position at Digital Brother.
### Task #1:
If we are from a correctly written arithmetic expression containing numbers,
operation signs and opening and closing parentheses discard numbers and signs
operations, and then write the remaining parentheses in the expression without spaces between them,
then the result obtained will be called the correct bracket expression [bracket
the expression "(() (()))" is correct, but "() (" and "()) (" is not].

##### Result:
```bash
/home/olehkyba/Projects/digital_brother_test/venv/bin/python /home/olehkyba/Projects/digital_brother_test/test_1.py
Test: 
(): True
)(: False
)): False
((: False
()(: False
())(: False
()(): True
(()): True
(()()): True
(()(())): True

Test string: ()(())()()
Is correct string?  True
```
### Task #2:
You are given a list of cities. Each direct connection between two cities has its transportation
cost (an integer bigger than 0). The goal is to find the paths of minimum cost between pairs of
cities. Assume that the cost of each path (which is the sum of costs of all direct connections
belonging to this path) is at most 200000. The name of a city is a string containing characters
a,...,z and is at most 10 characters long.

##### Result:
```bash
/home/olehkyba/Projects/digital_brother_test/venv/bin/python /home/olehkyba/Projects/digital_brother_test/test_2.py
The number of tests <= 10: 1
the number of cities <= 10000: 4
City name: gdansk
The number of neighbors: 2
>> 2 1
>> 3 3
City name: bydgoszcz
The number of neighbors: 3
>> 1 1
>> 3 1
>> 4 4
City name: torun
The number of neighbors: 3
>> 1 3
>> 2 1
>> 4 1
City name: warszawa
The number of neighbors: 2
>> 2 4
>> 3 1
The number of paths to find <= 100: 2
Path #1: gdansk warszawa
Path #2: bydgoszcz warszawa

Result: 
gdansk warszawa: 3
bydgoszcz warszawa: 2
```
### Task #3:
Find the sum of the digits in the number 100! (i.e. 100 factorial)
{Correct answer: 648}

##### Result:
```bash
/home/olehkyba/Projects/digital_brother_test/venv/bin/python /home/olehkyba/Projects/digital_brother_test/test_3.py
Sum of the digits in the number 100!:  648
Count sum of the digits in the factorial of: 100
648
```
