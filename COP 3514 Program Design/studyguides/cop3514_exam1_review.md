# COP 3514 Program Design - Exam 1 Review

<p style="text-align:center">
    <a href="../cop3514_textbook.pdf">textbook</a> |
    <a href="https://www.onlinegdb.com/online_c_compiler">c compiler</a>
</p>

## Accessing the Student Cluster

### Windows Setup

1. Set up password-less 2FA with an authentication app
    - For Microsoft Authenticator, this involves setting up "Phone Sign-In"
2. Sign in [here](https://vpn.usf.edu/global-protect/login.esp) with your NetID and password
3. While the webpage is loading, confirm the sign-in with your authentication app
4. Download GlobalProtect from the same site once you have signed in
5. Once downloaded, open the program and sign in with your NetID and password
6. While it's loading, confirm the sign-in with your authentication app
7. Connect to USF's VPN portal by typing `sc.rc.usf.edu` into the GlobalProtect VPN sidebar 
8. Download [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
9. Open PuTTY from the start icon
10. Type `sc.rc.usf.edu` into the field *Host Name (or IP address)* and `22` into *Port*
11. In the terminal popup, type your NetID and password

### Sending Files to/from the Cluster on Windows

1. Sign-in to the Cluster using the above directions
2. Open a Windows command prompt (cmd.exe) with PuTTY installed
3. Type `pscp -r <from directory> <netid>@sclogin1:<to directory>`

### Using the Cluster

- The Student Cluster is a remote group of computers running a Unix-based operating systems
    - Enables access to a Unix-based OS at all times
    - Enables execution of pre-compiled scripts shared by the professor
- Students should be familiar with using the Linux command-line
    - The most common commands found below

```bash
pwd                  # print current directory
cd <to directory>    # Change directory
ls                   # Show files and folders in current directory--pass -l to show file perms
nano                 # Barebones text editor
vimtutor             # Learn to use the vim IDE
gcc                  # GNU Compiler Collection (C Compiler)
g++                  # GNU C++ Compiler
./<program>          # Run a program
chmod <perms> <file> # Change file permissions
rm                   # Delete a file--pass -rf to delete a folder
clear                # Clear the screen of all previous commands
mv <file>            # Rename a file--pass some directory afterward to move it there
```

## 1. Introduction to C

- *C* is a procedural, high-level programming language
    - Created 1972 by Dennis Ritchie to replace B
- Compiles directly to assembly
    - Thereafter compiled to binary
- `gcc` and `clang` are popular *compilers*
    - Converts code to optimized assembly code specific to a computer architecture

>**Example 1.** Compiling a program
>```bash
>gcc -Wall -std=c99 main.c   # outputs executable `a.out`
>```
>- `gcc` is commonly pre-installed on Unix-based operating systems, like many distributions of Linux. It is pre-installed on the Student Cluster
>- `-Wall` enables all warnings
>- `-std=c99` ensures use of the C99 language standard
>- `a.out` is the default name of the executable created by the compiler

- Code compiled for one architecture may not run on another
- C was created specifically for the Unix operating system at Bell Labs
    - Later became an ANSI and ISO standard
- For each revision of the ISO standard, C*xx*, improvements are added
- We are concerned with **only** the C99 standard
- *Undefined behavior* is behavior not specified by the standard
    - May produce unexpected results
- All statements must be followed by a semicolon (`;`)
    - No top-level statements, like in JavaScript and Python

## 2. Declaring & Initializing Variables

- Variable declarations follow the form `<type> <name> <initial value>?`
    - Follow `snake_case` by convention

```c
int my_int = 1;  // 'my_int' is a variable of type 'int', whose initial value is 1
```

- C is *strongly-typed*: every variable must be assigned a type that does not change
- **Important:** If an initial value is not specified, the value of the underlying bits is unknown
    - Colloquially known as a *garbage value*

```c
int k;  // Currently, the value of 'k' is unknown
```

- Access to garbage values is undefined behavior, though the value will usually start as `0`
    - Initialize all variables or be extra careful

```c
k = 0;  // 'k' is initialized after declaration
```

- Variables can be made `const` so their values do not change

```c
const int i = 5;    // Variables can be made `const` so their values do not change
// i = 7;           // Compilation error: variable cannot be reassigned
```

- All variables not within a function are considered *local*
    - As opposed to global variables
- As a shorthand, multiple variables can be initialized of the same type on the same line

```c
int n = 1, m = 2, o = 3;
```

- **Important:** Variable and function names in C are *case sensitive* and  must be typed exactly the way they are declared
- These names are called *identifiers*
    - Can be comprised of underscores, letters, or digits
    - Must not start with a digit
- In C99, identifiers cannot be any of the following keywords



- **Important:** If in a nested scope, declaring a variable of the same name as one outside of that scope will *shadow* it
    - High potential for bugs, as it makes it so there is no way of referring to the outer variable explicitly

```c

```

## 3. Types & Casting

#### **Figure 1.** Common Primitive Types
| Type          | Description       | Minimum Size (Bits)                   |
|:--------------|:------------------|:-------------------------------------:|
| `char`        | ASCII character   | 8                                     |
| `short`       | small integer     | 16                                    |
| `int`         | integer           | 16                                    |
| `long`        | large integer     | 32                                    |
| `long long`   | huge integer      | 64                                    |
| `float`       | small decimal     | n/a, typically 32                     |
| `double`      | decimal           | no smaller than `float`, typically 64 |
| `long double` | large decimal     | no smaller than `double`              |

- `char` values map to their [ASCII code](https://www.asciitable.com/)
- In addition to performing arithmetic, `int`s are useful as boolean *flags*
    - If `0`, represents `false`
    - **Important:** If any other number (typically `1`), represents `true`
    - Can be used in conditionals

```c
int my_condition = 0;   /* == false */
if (my_condition) {
    // do something     /* never executes */
}
```

- The header `<stdbool.h>` provides the macro `bool`, which can be used as a type to implement flags as well
    - Provides macros `true` and `false`, evaluating to `1` and `0`, respectively

```c
#include <stdbool.h>

// ...

bool my_condition = false;  /* == 0 */
```

- Integer types are `signed` by default, but can be made `unsigned` to restrict to non-negative numbers
    - Increases maximum value
    - Underlying bits do not change, just the representation

```c
unsigned int m = -1;        // 'm' is assigned maximum unsigned value (all 1 bits)
int n = m;                  // 'n' is assigned -1
```

- *Strings* are represented by the types `char *` or `char[]`
    - Contiguous array of characters
    - For displaying text

```c
char *greeting = "Hello, world!";

puts(greeting); // Output: Hello, world!
```

- Typecasting, or simply *casting*, is the conversion from one type to another
    - Done so using the `(<type>)` operator
- `char` variables, being integers, can be safely cast to `int`, and vice-versa

## 4. Logical & Arithmetic Operators

#### **Figure 2.** Basic Operators in C
| Operators                                                                                                                                                                                                                             | Precedence    | Associativity |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------:|:-------------:|
| `++` <small>*prefix*</small><br>`--` <small>*prefix*</small><br>`()`<br>`[]`<br>`.`<br>`->`                                                                                                                                           | 1             | Left-to-right |
| `++` <small>*postfix*</small><br>`--` <small>*postfix*</small><br>`+` <small>*unary*</small><br>`-` <small>*unary*</small><br>`*` <small>*dereference*</small><br>`&` <small>*address-of*</small><br>`!`<br>`(typecast)`<br>`sizeof`  | 2             | Right-to-left |
| `*` <small>*multiply*</small><br>`/` `%`                                                                                                                                                                                              | 3             | Left-to-right |
| `+` <small>*binary*</small><br>`-` <small>*binary*</small>                                                                                                                                                                            | 4             | Left-to-right |
| `<` `<=`<br>`>` `>=`                                                                                                                                                                                                                  | 5             | Left-to-right |
| `==` `!=`                                                                                                                                                                                                                             | 6             | Left-to-right |
| `&&`                                                                                                                                                                                                                                  | 7             | Left-to-right |
| `\|\|`                                                                                                                                                                                                                                | 8             | Left-to-right |
| `=`<br>`+=` `-=`<br>`*=` `/=` `%=`                                                                                                                                                                                                    | 9             | Right-to-left |
| `,`                                                                                                                                                                                                                                   | 10            | Left-to-right |

<small>\**There exist other operators, though we will not use them*</small>

- **Important:** Operators with higher *precedence* are evaluated first
- *Associativity* determines which way operator should be read when combined with others
- The `++` and `--` operators increment and decrement variables, respectively
    - If before the variable name, simply changes the value
    - **Important:** If after, changes the value, with the expression evaluating to the **old** value

## 5. Preprocessor Directives

- The *preprocessor* runs before the compilation starts
    - Evaluates preprocessor directives, each prefixed by `#`
- `include` directives insert an entire file with the given name at the location of the directive
    - Files surrounded in `<>` are standard, those surrounded in `""` are resolved relative to the project directory
- *Header files* end in `.h` are `include`d to declare
    - Functions
    - `typedef`s
    - `struct`s
- Functions declared in `.h` files are defined in other `.c` files

```c
#include <stdio.h>  // Provides standard input-output functions

// ...

puts("Hello, world!");  // 'puts' declared in standard header file 'stdio.h'
```

- `define` directives declare macros that, at every use, are substituted with their definition
    - **Important:** Substitution is exact, so it helps to enclose definitions in parentheses to prevent issues caused by precedence
- Use macros to define numeric and string constants across your program
    - Follow `SCREAMING_SNAKE_CASE` by convention

```c
#define N 3 + 4

// ...

printf("%d", N);    // Output: 7
printf("%d", N * 5);    // Output: 23 (evaluates to '3 + 4 * 5')
```

## 6. Functions & Nested Scopes

- **Important:** Assignment of a value to a variable is itself a statement

```c
int n;
n = (n = 6) + 2;
printf("%d", n);    // Output: 8
```

- *Compound statements* are groups of statements enclosed in brackets (`{}`)
    - Encapsulate program logic, particularly useful in conditionals and loops
    - The body of a function
- Local variables declared inside of a compound statement cannot be accessed once outside of the brackets
    - For this reason, they are also called *nested scopes*

```c
{
    int n = 1;  // Can only be used within these brackets
}
printf("%d", n);    // Compilation error: symbol 'n' not found
```

- Variables declared outside of functions are *global* and can be accessed from any part of the program
    - Generally discouraged, macros should be used for constants instead
- *Functions* are named, reusable blocks of code
    - Follow `snake_case` by convention
- Functions, generally, comprised of two parts
    1. Function declaration (also called *prototype*) 
    2. Function definition
- Function definition provides the procedure that is to be executed
    - Follow the form `<return type> <name> ( <parameters>? ) { <statements>? }`
- The *call site* is the location where a function is called
    - `return` value passed to this context
- The *scope* of a function is everything within its definition
    - Like compound literals, cannot have their local variables accessed by other functions

```c
void fun() {
    int m = 0;
}

int main() {
    // printf("%d", m); // Compilation error: Variable 'm' not found in this scope
    return 0;
}
```

- **Important:** If a function returns `void`, it returns nothing
    - `return;` can be used, although can be omitted entirely
- **Important:** All C programs begin execution at `main` function
    - Returns `0` on success, non-zero on failure
    - After return, program terminates

```c
#include <stdio.h>

int n;  // Declare integer 'n' to be global

int main() {
    n = 16; // Initial value of 16
    my_fun();
    printf("%d", n);    // Output: 17
    return 0;
}

void my_fun() { 
    n++;    // Increment by 1
}   // 'void' function returns nothing
```

- Function prototype describes the function
    - Name
    - Parameters, if any
    - Return type
- Because prototypes are statements, require a semicolon
    - Follow the form `<return type> <name> ( <parameters>? );`
- *Parameters* are the variables defined in the prototype, *arguments* are the values actually supplied
    - In prototype, do not require names

```c
int add(int, int);  // 'add' is a function that takes two integers and returns an integer

int main() {
    printf("%d", add(2, 2) /* call site */);    // Output: 4
    return 0;
}

int add(int x, int y) { // This is the procedure to be executed when 'add' is called
    return x + y;   // Return 'int' result to call site
}
```

- Prototype or definition **must** precede first call site, else function is defined implicitly
    - Should be avoided

```c
int main() {
    printf("%d", div(4, 2));    // 'div' function implicitly defined as prototype 'int div(int, int)' 
    return 0;
}

int div(double x, double y) {
    return x / y;
}

// Linker error: function 'div' cannot be found
```

## 7. Conditional Statements

- `if` statements execute the following statement if a condition is true
    - Follow the form `if ( <condition> ) <statement>`
- `else` can be appended to execute an alternative statement if the condition is false
- Compound statements can be used with either form of conditional

```c
int my_condition = /* 0 or non-zero */;
if (my_condition) fun_1(); else fun_2();  // 'fun_1' called if 'my_condition' is non-zero, else 'fun_2' is called
```

- `else` statements can contain other `if` statements

```c
if (condition_1) {
    // Run if 'condition_1' is true
} else if (condition_2) {
    // Run if 'condition_1' is false, but 'condition_2' is true
} else {
    // Run if neither are true
}
```

- Both `if` and `else` can be given empty statements

```c
if (condition); else;   // Legal
```

- `switch` statements are a more concise way of creating `if`-`else` chains
    - Compares integer types only (`int`, `char`, etc.)
- `switch` statements take an argument, and jump to the `case` label with the same value
    - `case`s are evaluated *in-order*
- **Important:** Unless otherwise specified, *all* code in the `switch` after the label will be executed after jump
    - Good practice to `break` after code in every `case`
    - Although not required, `break` is encouraged after final `case`

```c
char chr = 'a';
switch (chr) {
    case 'a':
        printf("a");    // All statements hereafter will be executed
    case 'z':   // Without 'break', this case is also run
        printf("z");
        break;
    case 'c':    // 'break' ensures this case is not also ran
        printf("c");
        break;
}   // Output: az
```

- `default` label is always ran when encountered
    - A single `switch` can have multiple

```c
switch (chr) {
    default:    // Always run
        printf("default");
    case 'a':   // Fall-through to this case
        printf("a");
        break;  // Break out of switch here
    default:
}   // Output: default
```

## 8. Loops

- `while` executes statement once for every time condition is true
    - Can be passed compound statements, similar to `if`-`else`
- `while` control flow
    1. If condition is false, skip over loop
    2. Execute statement
    3. If condition is false, break out of loop
    4. Go to step 2
- **Important:** Special cases
    - If the condition is always true, the loop will repeat forever
    If the condition is never true, the statement will never be executed

```c
int my_condition = 4;   /* == true */

int main() {
    // Check condition: if false, skip this
    while (my_condition) {
        fun();
        printf("%d ", my_condition);
        // Check condition: if false, break out of here
    }
    return 0;
}   // Output: 4 3 2 1

void fun() {
    my_condition--; // Decrement by 1
}
```

- `do`-`while` always executes statement once *before* checking for condition
- `do`-`while` control flow
    1. Execute statement
    2. If condition is false, break out of loop
    3. Go to step 1

```c
do {
    fun();
    printf("%d ", my_condition);
    // Check condition: if false, break out of here
} while (my_condition) // Output: 3 2 1 0
```

- `for`-loops extend `while` loops with an initial and loop statement
    - Follow the form `for ( <initial> ; <condition> ; <loop> ) <statement>`
- The *initial* statement is evaluated first, always
- The *loop* statement is evaluated after each iteration (every time the loop is ran)
- `for`-loop can also be expressed as a `while` loop

```c
int main() {
    int i = 0;
    while (i < 5) {
        printf("%d ", i);
        i++;
    }
    printf("\n");
    for (int j = 0; j < 5; j++) {
        printf("%d ", j);
    }
    return 0;
}   // Output: 0 1 2 3 4
    //         0 1 2 3 4
```

- `for`, `while`, and `do-while` loops can be *broken* out of prematurely using `break`

```c
int n = 3;
while (n > 0) { // Loop infinitely
    printf("a");
    if (n == 2)
        break;
    n--;
}   // Output: aa
```

## 9. Representation of Variables in Memory

- The *stack* is the underlying data structure keeping track of program state
    - Analogous to the stack used in assembly code
- The stack is a last-in-first-out (LIFO) stack, where each element is a stack frame that contains information on
    - Local variables
    - Function information
    - Function to return to

```c
int fun() {
    int n, m = 0;
    // See second stack for state here
    return 16;
}
int main() {
    // See first stack for state here
    printf("%d", fun());
    // See third stack for state here 
    return 0;
}

```

- In the `main` function above, the stack looks like

| Stack                                                                                     |
|:------------------------------------------------------------------------------------------|
| Function: `main`<br>Local variables: [<small>*none*</small>]<br>Caller: `_start`          |

- After `fun` is called, its scope is added to the top of the stack

| Stack                                                                                                     |
|:----------------------------------------------------------------------------------------------------------|
| Function: `main`<br>Local variables: [<small>*none*</small>]<br>Caller: `_start`                          |
| Function: `fun`<br>Local variables: [`n` = <small>*garbage value*</small>, `m` = `0`]<br>Caller: `main`   |

- Once control is *returned* to `main`, the element at the top of the stack (the last element) is removed
    - Assuming no other calls, any local variables declared will be in scope `main`

| Stack                                                                                     |
|:------------------------------------------------------------------------------------------|
| Function: `main`<br>Local variables: [<small>*none*</small>]<br>Caller: `_start`          |

- In memory, the stack is a contiguous (in one piece) array of bits
    - Each point in this array can be accessed by its *address*
- By using *pointers*, we manipulate the data at a certain address in the stack
- Appending `*` to a type designates it as a pointer type
- The *address-of* (`&`) operator is used to obtain the memory address of a variable in memory
- `*` is the *indirection* operator, used to *dereference* memory addresses
    - Dereferencing allows data at that address to be modified
    - Works even if it is not possible access the variable holding that data

```c
int main() {
    int my_int = 16;
    int *to_my_int = &my_int;
    printf("0x%x", to_my_int);    // Output: 0xbe16b8441617 (exact value may differ)
    printf("%d", my_int);   // Output: 16
    (*to_my_int)++;
    printf("%d", my_int);   // Output: 17
    return 0;
}
```

```txt
 0xbe16b8441617       16
(memory address)   (value)
 ┌───────────┐   ┌────────┐
 │ to_my_int ══> │ my_int │
 └───────────┘   └────────┘
     int *           int
```

- Integers can be added to/subtracted from pointers to get the corresponding address
    - Crucial for working with array elements
- *Arrays* are contiguous blocks of values
    - Declarations follow the form `<type> <id> [ <size>? ] <initializer>?`
- The *index* of an array element is its position in the array
    - **Important:** The first element in an array is at index **0**
- **Important:** Array variables are themselves a pointer to their first element
    - Because of this, arrays in the form `<type>[]` can be cast to `<type> *`
    - Often seen as function parameters (`printf`, `scanf`, etc.)
- Array elements given initial values using an *initializer list*
    - List of values enclosed in brackets (`{}`)
    - If array size is unspecified, array is of size of initializer list

```c
int first_element(int *);

int main() {
    int n[] = {1,2,3};

    printf("$d", first_element(n)); // Output: 1
    for (int i = 0; i < 3; i++) {
        printf("%d ", *(n + i));    // Get element 'i'
    }   // Output: 1 2 3
    return 0;
}

int first_element(int *array) {
    return *array;  // Get element pointed to by 'array'
}
```

```txt
           (array in stack)
            ┌───┬───┬───┐
int n[] ══> | 1 | 2 | 3 |
            └───┴───┴───┘

           Stack
  ───┬───┬───┬───┬───┬───
 ... | 1 | 2 | 3 | n | ...
  ───┴─⇑─┴───┴───┴─║─┴───
       ╚═══════════╝
```

- Furthermore, arrays can be given an explicit size **at declaration**
    - If initializer list is used, all members left uninitialized are set to 0

```c
int n[5] = {1,2,3};
for (int i = 0; i < 5; i++) {
    printf("%d ", n[i]);
} // Output: 1 2 3 0 0
```

- **Important:** Arrays whose size is specified *without* an initializer list contain garbage values
    - Care must be taken to properly initialize all elements

```c
int grades[12];
// printf("%d", *grades);   // Undefined behavior
*grades = 87;
printf("%d", *grades);  // Okay. Ensure all others are initialized before their use
```

- Arrays can *not* be assigned an initializer list outside of an array declaration

```c
int n[2];
// n = {6,7};   // Compilation error: Expected expression
```

- Array variables also can *not* be assigned another value
    - Pointers to the first element can be reassigned, however

```c
int n[] = {3,4,5};
int m[] = {6,7,8};
// n = m;   // Compilation error: Assignment to array type
int *to_m = m;  // Okay
```

- **Important:** Array types are not *inherently* pointer types
    - Although the value of an array-type variable is the address of its first element, there are subtle differences
- For array types, `sizeof` operation evaluates to total size of array, in bytes
    - For pointer types, evaluates to size of memory address

```c
// ...assume size of 'int' is 4 bytes, and size of memory address is 64 bits (8 bytes)

int n[] = {1,2,3,4,5};    // sizeof(n) == sizeof(int) * 5
int total_elements = sizeof(n) / sizeof(int)    /* == (4 * 5) / 4, or 5 */
int *first_element = n;
int addr_size = sizeof(m) / sizeof(int) /* == 8 / 4, or 2 (NOT the size of the array) */
```

- Strings, of type `char *` or `char[]`, are arrays of characters
    - Can be initialized just the same
- **Important:** All strings must have the null character (`'\0'`) be their last character
    - Also called the *null terminator*
    - Used by functions to determine when to stop reading characters from the string

```c
char message[] = "Ahoy!";   // 'message' contains 6 elements
while (*message != '\0') {
    printf("%c", *message);
    message++;  // Go to next character in array
}   // Output: Ahoy!

char signal[] = {'S', 'O', 'S', '\0'}
if (strcmp(message, signal) == 0) {
    puts("Elements are equal");
}   // Output: Elements are equal
```

- **Important:** String literals, like `"this"`, are themselves pointers to **read-only** arrays
    - Attempt to modify these arrows will crash the program

```c
char *chess = "Hi, world!";
*(chess + 1) = 'o'; // Runtime error: Segmentation fault (core dumped)
```

- Oftentimes, modifying read-only memory will throw a *segmentation fault*
    - Keep this in mind when debugging programs
- Strings can be made modifiable by explicitly declaring an array type instead of a pointer type

```c
char chess[] = "Hi, world!"
*(chess + 1) = 'o';
printf("%s", chess);    // Output: Ho, world!
```

- Array *subscripting* is the access of specific array elements via the `[]` operator
    - Shorthand for `*` and `+` operators

```c
int lucky_nums[] = {16,57, 144};

for (int i = 0; i < 3; i++) {
    printf("%d ", *(lucky_nums + i));   // Get element at index 'i'
}   // Output: 16 57 144
for (int i = 0; i < 5; i++) {
    printf("%d ", lucky_nums[i]);
}   // Output: 16 57 144
```

- Restricts on variable scope apply to local arrays, too
    - Cannot be accessed outside of original scope/function

```c
int main() {
    int placeholder[] = {0};
    fun();
    return 0;
}

void fun() {
    // placeholder[0] = 10; // Compilation error: Variable 'placeholder' not found
}
```

## 10. Console I/O

- C provides *escape sequences* for hard-to-type characters
    - Works for `char`s and strings alike

#### **Figure 3.** Common Escape Sequences
| Character         | Escape    |
|:------------------|:----------|
| newline           | `\n`      |
| carriage return   | `\r`      |
| tab               | `\t`      |
| backslash         | `\\`      |
| single quote      | `\'`      |
| double quote      | `\"`      |
| null character    | `\0`      |

<small>\**The full list of escape sequences can be found [here](https://en.wikipedia.org/wiki/Escape_sequences_in_C#Escape_sequences)*</small>

- The standard header file `stdio.h` provides functions to read from/write to the console

#### **Figure 4.** Common `stdio.h` Functions for Console I/O
| `stdio.h` Function        | Description                                                                                                   | Return Value                              |
|:--------------------------|:--------------------------------------------------------------------------------------------------------------|:------------------------------------------|
| `int printf(char *, ...)` | Prints the string to the console, as specified by its format specifiers.                                      | `0` on success, or non-zero on failure    |
| `int scanf(char *, ...)`  | Reads the values from the console according to the format specifiers, storing them in the addresses provided  | `0` on success, or non-zero on failure    |
| `int puts(char *)`        | Prints the string to the console, followed by a line break (`'\n'`)                                           | `0` on success, or non-zero on failure    |
| `int getchar()`           | Reads a single character from the console, including the line break character                                 | The character read                        |

<small>\**The full list of `stdio.h` functions can be found [here](https://en.cppreference.com/w/c/io)*</small>

- `printf` and `scanf` take, as their first argument, a string containing *format specifiers*
    - Each code, prefixed by a `%`, represents a value to be printed or read
- These two functions are *variadic*, they can take any number of arguments after their first one

```c
printf("%s is %d (0x%x)", /* variadic arguments: */ "The value", 21, 21);    // Output: The value is 21 (0x15)
```

#### **Figure 5.** Common Format Specifiers
| Type                                      | Format Specifiers |
|:------------------------------------------|:------------------|
| (percent sign)                            | `%%`              |
| `char`                                    | `%c`              |
| `int`                                     | `%d`              |
| `int` <small>*hex*</small>                | `%x` `%X`         |
| `int` <small>*octal*</small>              | `%o`              |
| `unsigned int`                            | `%u`              |
| `double`                                  | `%f` `%F`         |
| `double` <small>*sci notation*</small>    | `%e` `%E`         |
| `char *` <small>*string*</small>          | `%s`              |

<small>\**The full list of specifiers can be found [here](https://en.wikipedia.org/wiki/Printf#Format_specifier)*</small>

- **Important:** The order of format specifiers matters
    - Their position **must** correspond the position of the argument given

```c
int age = 21;
char *major = "cs";

printf("Age-%d\tMajor-%s", major, age);   // Runtime error: Specifier order does not agree with arguments
printf("Age-%d\tMajor-%s", age, major);   // Okay. Output: Age-21    Major-cs
```

- Similarly, `scanf` reads values as it sees format specifiers in its first argument
    - Any characters not part of a specifier are ignored
    - Input is not parsed until *enter* is pressed

```c
int input;
scanf("%d", &input);    // Address-of (&) operator supplies address of variable (a pointer)
printf("%d", input);    // Initialized by 'scanf', output is whatever user entered
```

- `puts` simply prints a string to the console, followed by a new line (`'\n'`)

```c
{
    puts("Hi, who is this?");
    puts("It's Bob :)");
}   // Output: Hi, who is this?
    //         It's Bob :)
```

- `getchar` reads a single character from the console
    - Does not stop when *enter* (newline, `'\n'`) is pressed, must be explicitly checked

```c
#define MAX_INPUT_SIZE = 100

// ...

char input[MAX_INPUT_SIZE];

for (int i = 0; i < MAX_INPUT_SIZE && ; i++) {
    char c = getchar();
    if (c == '\0') {
        break;
    }
    input[i] = c;
}
printf("%s", input);    // Output is whatever user entered
```