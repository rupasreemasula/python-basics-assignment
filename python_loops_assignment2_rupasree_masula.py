'''Q: 1
Scenario: You are a junior data analyst automating simple number-based reports using Python. Your manager wants all outputs generated using for loops only.

Task 1 Write a for loop that prints all numbers from 1 to 5 using range().

Task 2 Write a for loop that prints only odd numbers between 1 and 10 using the step parameter in range().

Task 3 Write a nested for loop that prints the following pattern:

0 0
0 1
1 0
1 1
2 0
2 1
Task 4 Write a for loop that prints numbers from 1 to 7. If the number is 5, stop the loop immediately using break.'''

for i in range(1,6):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(3):
    for j in range(2):
        print(i, j)

for i in range(1,8):
    if i == 5:
        break
    print(i)