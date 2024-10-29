# COP 3514 Program Design - Exam 1 Review

<p style="text-align:center">
    <a href="../textbooks/COP3514_textbook.pdf">textbook</a>
</p>

## Preliminary - Accessing the Student Cluster

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

## 1. Overview of C

- *C* is a procedural, high-level programming language
    - Created 1972 by Dennis Ritchie to replace B
- Compiles directly to assembly
    - Thereafter compiled to binary
- `gcc` and `clang` are popular *compilers*
    - Converts code to optimized assembly code specific to a computer architecture

>**Example:** Compiling a program
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

## 2. C Syntax

### *Primitive Types*
```c
                    //  Description     | Minimum Size in Memory (Bits)
                    // -----------------+-------------------------------
bool b;             //  truth value     | 8                             --> requires #include <stdbool.h>
char c;             //  ASCII character | 8
short s;            //  small integer   | 16
int i;              //  integer         | 16
long l;             //  large integer   | 32
long long ll;       //  huge integer    | 64
float f;            //  small decimal   | n/a, typically 32
double d;           //  decimal         | no smaller than `float`, typically 64
long double ld;     //  large decimal   | no smaller than `double`
void * p;           //  untyped pointer | n/a, architecture-specific

unsigned int ui;    // `unsigned` modifier denotes that the integer is non-negative. Increases maximum value
signed int si;      // `signed` modifier Should never be used, as all integers are signed by default
bool cond = true;   // Boolean values
```

### Variables
```c
getchar();          // All statements must be followed by a semicolon
int n = 1;          // Variable declarations follow the form `<type> <name> <initializer?>`
                    // C is strongly-typed, so every variable must be assigned a type
int k;              // Variables not given an initial value are given a "garbage" value
                    // Access to garbage values is undefined and may throw an error
k = 0;              // To avoid accessing garbage values, initialize all variables at their declaration or be extra careful
const int i = 5;    // Variables can be made `const` so their values do not change
int my_int = 9;     // Variables follow snake_case by convention
```

### Preprocessor Directives
```c
#include <stdio.h>  // Inserts entire header (.h) file at this location
                    // Header files provide function and `struct` declarations for those defined in other, linked binaries (see `ld`)
#define PI 3.14     // Macros define tokens which are replaced with their definition (in this case, 3.14) at every point they are used
                    // Follow SCREAMING_SNAKE_CASE by convention
                    // All preprocessor directives evaluated BEFORE compilation
```

### Compound Statements
```c
{                   // Compound statements define a section of code containing multiple statements
                    // Variables defined in its scope are "local" and can only be accessed from within it    
    int n = 1;
}                   // End of compound statement
printf("%d", n);    // Compilation error: symbol "n" not found
```

### Functions
```c
int n = 5;                      // Variables defined outside of a function are "global" and can be accessed from any function
                                // Are discouraged. For constants, use macros instead
int add(int, int);              // Function header/prototype defines name, return type, and parameters of a function
                                // Parameter names are optional for headers/prototypes only
                                // Unlike definitions, is a statement and therefore requires a semicolon
                                // Headers/prototypes are required when function is used before its definition

int add(int x, int y) {         // This is a function definition
                                // Functions are named, reusable blocks of code
                                // Follow the form `<return type> <name> ( <parameters?> ) { <statements?> }`
                                // If no header/prototype exists, declares function at the same time
    return x + y;               // Returns result to original call site
}

void print_msg(char *msg) {     // Empty parentheses implies there are no parameters
                                // Functions follow snake_case by convention
                                // The type `void` denotes that the function does not return a value
                                // Can be made explicit by use of `void print_hello(void)`
    printf(msg);
}                               // Functions returning nothing do not need an explicit return statement
                                // However, if an early return is needed, do so like `return;`

int main() {                    // This specific function is always first function called in any program
    printf("%d", add(2, 3));    // Prints "5"
    print_msg("Hello, world!"); // Values passed to a function at the call site are called "arguments" instead of parameters
    return 0;                   // Return value of 0 implies success, non-zero return implies error
                                // Once the main function returns, the program terminates
}
```

### Conditional/Selection Statements
```c
int true_value = 1;             // Any non-zero value is considered "true"
int false_value = 0;            // 0 is always considered "false"
int cond = cond();              // Some random conditional value
if (cond) fun1();               // `if` statements execute a procedure if some condition is true
if (cond) fun1() else fun2();   // `else` can be appended to `if` statements, executing the alternative if the condition is false
if (cond) {                     // `if` and `else` can execute compound statements
    print_msg(":CAUGHT:");
}
char a = 'a';
char z = 'z';
char chr = pick_one(a, z);
switch (chr) {                  // `switch` statement 
                                // A glorified `if-else` chain
    case 'a':                   // If `chr` is 'a', control flow will move to here
        print_msg("a");         // All statements hereafter in the `switch` statement will be executed
        break;                  // `break` to ensure next `case` labels are not also executed
    case 'z':
        print_msg("z");
        break;
    default:                    // Control flow moved to this label if variable disagrees with all other `case` values
        print_msg(":CAUGHT:");
        break;
}
switch (chr) {
    case 'a':                   // If `break` is not last statement before the next `case` label, executes next label
                                // Fall-through to the next label
    case 'z':                   // If `chr` is 'a', this label will also be executed
        print_msg(":skull:");
        print_msg(":CAUGHT:");
                                // `break` is not required (but is encouraged) for last label
}
switch (chr) {
    default:                    // Default label is always executed if comes before another label, and `break` is not specified beforehand
        break;
    case 'a':                   // Control flow will never be here
}
```

### Operators
```c
/*
  Operator    | Precedence    | Associativity
 -------------+---------------+-----------------
  ++ --       |               | 
  ()          |               | 
  []          |       1       |   Left-to-right
  .           |               | 
  ->          |               | 
 -------------+---------------+-----------------
  ++ --       |               | 
  + -         |               | 
  ! ~         |               | 
  (typecast)  |       2       |   Right-to-left
  *           |               | 
  &           |               | 
  sizeof      |               | 
 -------------+---------------+-----------------
  * / %       |       3       |
 -------------+---------------|
  + -         |       4       |
 -------------+---------------|
  << >>       |       5       |
 -------------+---------------|
  < <=        |       6       | 
  > >=        |               |   Left-to-right
 -------------+---------------|
  == !=       |       7       |
 -------------+---------------|
  &&          |       8       |
 -------------+---------------|
  ||          |       9       |
 -------------+---------------+-----------------
  =           |               |
  += -=       |       10      |   Right-to-left
  *= /= %=    |               |
  <<= >>=     |               |
 -------------+---------------+-----------------
  ,           |       11      |   Left-to-right
*/

```

### Loops
```c
while (cond) fun1();        // While the condition is true, the statement is executed
                            // If the condition is true forever, the loop will repeat forever
                            // If the condition is never true, the statement will never be executed
while (cond);               // `while` and `for`, but not `do-while` loops do not require a statement
while (cond) {              // `while`, `do-while`, and `for` loops can execute compound statements
    print_msg(":CAUGHT:");  // Control flow: check condition: if false, exit loop; else, execute statement then check condition: if false...
}
do fun1() while (cond);     // `do-while` executes the statement first, then checks the condition
int iterations = 16;
for (int i = 0; i < iterations; i++) fun1();    // `for` loop configuration in the form `<setup?> ; <condition?> ; <iterator?>`
                                                // Each part of configuration is optional
                                                // Control flow: Execute setup, check condition: if false, exit loop;
                                                //     else, execute statement, then execute iterator, then check condition: if false...
for (;;)                                        // By omitting all configuration, an infinite loop is created
```

### Console Input and Output (I/O)
```c 
/*
 For full list, see https://en.wikipedia.org/wiki/Printf#Format_specifier

  Type                  | Format Specifier(s)
 -----------------------+---------------------
  percent literal       | %%
  int                   | %d
  int (hexadecimal)     | %x, %X
  int (octal)           | %o
  unsigned int          | %u
  double                | %f, %F
  double (scientific)   | %e, %E
  char * (string)       | %s
*/

#include <stdio.h>              // `stdio.h` header provides I/O functions

int n = 1;
printf("%s: %d", "Value", n);   // `printf` and similar functions ending in "f" take a variable # of arguments
                                // Parses values and prints them to the console
                                // Prints "Value: 1"
scanf("%d", &n);                // Parses input from the console and stores it in the address of `n`, changing its value
getchar();                      // Retrieves single character input from the console
                                // Characters are not actually retrieved until input is "flushed" (ENTER is pressed)
```

### Pointers
```c
int n = 5;
int * n_addr = &n   // A "pointer" is a address of some value in memory
                    // To get the memory address of a variable, use the ampersand operator
*n_addr = 8;        // Indirection operator (*) allows changing of value at the specified address
printf("%d", n);    // Prints "8"
```

### Arrays
```c
int arr[];              // Declares `n_arr` to be an array of integers
arr[0];                 // IMPORTANT: Arrays start at index 0
                        // They are pointers to the first element
                        // Accessing any element without providing a capacity on declaration, or
                        //     providing an initializer list, or
                        //     allocating the array dynamically is undefined
                        // Arrays contain no size information or bounds-checking
int arr[10];            // Declares an array capable of holding 10 integers
                        // IMPORTANT: At this point, array filled with garbage values
int arr[] = {1,2,3};    // Declares an array capable of holding 3 integers
                        // Each element initialized according to the initializer list
char *s = ":CAUGHT:";   // Strings are arrays of characters
                        // Modification of string literal arrays is undefined
char s[] = {            // These elements can be modified
    ':','C','A','U',
    'G','H','T',':'
};
int *element0;
{
    int scoped_arr[10];
    element0 = scoped_arr;
}
*element0;              // Runtime error: arrays not dynamically allocated cannot
                        // be accessed once their original scope has terminated
```