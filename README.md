[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5320626&assignment_repo_type=AssignmentRepo)
# extra01-summer-2021
Extra Practice 01

The goal of this exercise is to create a computer that can play the number guessing game. In this game, the user will pick a number in between two numbers. And the computer will give guesses until it can find the chosen number. The user will enter the two numbers and also give responses to the computer's guesses.

# Start of program
The program will first ask the user to enter two numbers. These numbers define the interval of numbers to choose from.

```shell
Min num? 1
Max num? 100
```

Once entered the computer will make a guess in between these two numbers (inclusive).

# After a guess
When the computer makes a guess, this needs to be printed to screen and then the computer asks higher or lower.
```shell
Guess: 25
high/low/correct? h
```
To simplify the code, please just use lowercase `h`, `l` and `c` for expected responses.
- `h`: actual answer is higher than the computer's guess
- `l`: actual answer is lower than the computer's guess
- `c`: the computer guessed the correct number.

# Repeat until correct
The computer will continue to repeat until the answer is guessed.

# Hints
- `while` loops should be used to repeat until answer is guessed.
- Use variables to store the guess.
- Use the `bisection method` to guess the number.
