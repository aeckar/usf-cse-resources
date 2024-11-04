# COP 3514 - Project 4, Task 1 Guide

*Original by Jing Wang of the University of South Florida*

**Disclaimer:** This is a guide *not* a solution.
Different approaches to problems you may face in this project are outlined below,
but not concrete solutions are not. 
This is not the *only* way to look at this project, and you are encouraged to explore alternatives.

### Plain-English Directions

The purpose of this program is to determine who wins each round of a game. The players are Marjorie and John,
with Marjorie always playing on the first round of the game.

The game consists of a board of integers, which can be represented as an array of size **N**.
For each round, one of the players picks the largest number at either end of the board.
Once the board is empty, whoever's numbers produce the greatest sum wins.

Because the player at each round, and what number they will pick can be known ahead of time,
the program should print the result of the round as soon as it knows what numbers are on the board.

The program should assume the following:

- Every number in the board is unique
- A board can contain no more than 1000 numbers
- If both ends are the same number, choose the tail (last) element

The program should roughly follow these procedures:

1. **Ask user for the number of rounds, T**
    - Validate whether the input is between 1 and 100
2. **For each round, perform the following:**
    1. Ask user for the size of the board
        - Validate whether the input is between 1 and 1000
    2. Populate the board with input from the user
    3. Determine the only possible winner of the round using an algorithm
    4. Print the winner, or `Draw` if the players have equal sums

Additionally, the program must include the function header below, as well as its definition:

```c
// Prints the result of the round ("Marjorie", "John", or "Draw")
void round_result(int *board, int n);
```

A caveat to this exercise is that you cannot use iteration variables such as `i` to traverse the board,
you must use pointer arithmetic instead. However, you can still use loops with iteration variables to
keep track of the current round.

### Example

```c
5                       // Input # of rounds
7                       // Input board size
1 2 3 4 5 6 7           // Input board contents
// Output: "Marjorie"
3                       // Board size
1 3 2                   // Board contents
// Output: "Draw"
1                       // Board size
1                       // Board contents
// Output: "Marjorie"
1                       // Board size
1                       // Board contents
// Output: "John"
11                      // Board size
5 8 3 10 1 11 2 9 4 7 6 // Board contents
// Output: "John"
```
