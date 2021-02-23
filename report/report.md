# Report for assignment 3

## Project

Name: Pythonic Data Structures and Algorithms

URL: https://github.com/keon/algorithms

Minimal and clean example implementations of data structures and algorithms in Python 3.

## Onboarding experience
    
Worked out of the box without any dependencies except the need for installing the library "pytest" for testing.


## Complexity

### search() @ tree/trie/add_and_search.py
Counting the cyclomatic complexity (CC) manually gave the result 10 which was the same that the tool "Lizard" measured.
The reason the search function, which checks if a word is in a Trie, has such a high CC is because it allows for "wild-card" searches. Meaning that the function should return true for the given example:
```
add_word("man")
search("m.n") # returns true
```
Without the wild-card functionality, the CC could be brought down to 4 which is good.
The function is short (20 LOC) and does not contain exceptions.
The documentation shows good examples for the search function.

### valid_solution_set() @ matrix/sudoku_validator.py
When we calculated the CCN manually we got 11 which is the same as the automated lizard tool gets. Since most of the code consist of for-loops and if-statements the function is short in terms of LOC even though it has fairly high CCN. There are no exceptions used in this function.

The function is a sudoku validator so it goes through a sudoku board (9x9 matrix) and checks that every rule is fulfilled, which requires a lot of checks that increase the CCN. The rules it checks is that every row, column and square has only the numbers 1-9 and exactly one of each. 
 
There is a comment at the start explaning that the input is a 2D array and that it will return 0/1 depending of if it is valid or not but the function itself and what is being tested in the branches is not commented at all. 

### prime_check() @ maths/prime_check.py
The function was measured with Lizard which gave the result of 9.
The reason the prime_check function, which checks if a number is a prime, has such a high CC is because it uses cleaver modulo operations which lowers the running time at the cost of higher CC with the extra if-statements. 
There is another variation the loops through each number up to the square root of the number that is being checked. It brings down the CC to 6 but does not seem suitable since the function is based on mathematical lemmas and easy to test.
The function is short (16 LOC) and does not contain exceptions.
There is no documentation that provides examples.

## Refactoring

### Plan for refactoring complex code:

In the function valid_solution_set I was working with there is three nestled for-loops with the purpose of getting the columns 
from the matrix, which adds to the CCN. A simple way to refactor this funtion could be to simply import numpy and use a numpy 
matrix instead which is much efficient since with numpy you can get the columns out with a single for-loop. 

### Estimated impact of refactoring (lower CC, but other drawbacks?).

While I think this would lower the CC and especially make the function easier to read the drawback is that you would be dependant
on numpy and it seems the people who control the project prefers to be entirely independant on other libraries. 



Carried out refactoring (optional, P+):

git diff ...

## Coverage

### Tools

Document your experience in using a "new"/different coverage tool.

How well was the tool documented? Was it possible/easy/difficult to
integrate it with your build environment?

### Your own coverage tool

Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is
its output?

### Evaluation

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

## Coverage improvement

### valid_solution_set

Apart from loops to iterate there are three if-statements required to test if a board is valid or not which means that there are 6 paths to take (true/false for the 3 if-statements). The function has 1 testcase for a valid board and 1 testcase for a invalid board. To see that a board is valid all 3 if-statements must be true, which means that the valid testcase takes 3 out of the 6 paths. However the invalid testcase fails on the first if-statement and ends the test since it already know it is not a valid board, meaning the other two false if-statements are never tested. 

I added two more test cases, one which passes the first validation check, but then fails on the second, and one test
that passes the first two validation checks but then fails on the third. With these two additional test cases all 6 
possible paths has been tested. 


Show the comments that describe the requirements for the coverage.

Report of old coverage: [link]

Report of new coverage: [link]

Test cases added:

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).

## Self-assessment: Way of working

Current state according to the Essence standard: ...

Was the self-assessment unanimous? Any doubts about certain items?

How have you improved so far?

Where is potential for improvement?

## Overall experience

What are your main take-aways from this project? What did you learn?

Is there something special you want to mention here?
