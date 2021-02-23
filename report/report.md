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

### prime_check() @ maths/prime_check.py
The function was measured with Lizard which gave the result of 9.
The reason the prime_check function, which checks if a number is a prime, has such a high CC is because it uses cleaver modulo operations which lowers the running time at the cost of higher CC with the extra if-statements. 
There is another variation the loops through each number up to the square root of the number that is being checked. It brings down the CC to 6 but does not seem suitable since the function is based on mathematical lemmas and easy to test.
The function is short (16 LOC) and does not contain exceptions.
There is no documentation that provides examples.

## Refactoring

Plan for refactoring complex code:

Estimated impact of refactoring (lower CC, but other drawbacks?).

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
