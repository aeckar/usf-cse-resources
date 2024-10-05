# COP 3514 Program Design - Exam 1 Review

<ins>Textbook</ins>: *C Programming: A Modern Introduction (2nd ed.)* by K. N. King

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

### Variables
```c
getchar();          // All statements must be followed by a semicolon
int n = 1;          // Variable declarations follow the form `<type> <name> <initializer?>`
int k;              // Variables not given an initial value are given a "garbage" value
                    // Access to garbage values is undefined and may throw an error
k = 0;              // To avoid accessing garbage values, initialize all variables at their declaration or be extra careful
const int i = 5;    // Variables can be made `const` so their values do not change
```

### Scopes
```c
{                   // Compound statements define a section of code containing multiple statements
                    // Variables defined in its scope are "local" and can only be accessed from within it    
    int n = 1;
}                   // End of compound statement
printf("%d", n);    // Compilation error: symbol "n" not found
```

### Functions
```c
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
if (cond) fun1() else fun2();   //  `else` can be appended to `if` statements, executing the alternative if the condition is false
if (cond) {                     // `if` and `else` can execute compound statements
    print_msg(":CAUGHT:");
}
```

### Loops
```c
while(cond) fun1();         // While the condition is true, the statement is executed
                            // If the condition is true forever, the loop will repeat forever
                            // If the condition is never true, the statement will never be executed
while (cond) {              // `while`, `do-while`, and `for` loops can execute compound statements
    print_msg(":CAUGHT:");  // Control flow: Check condition: if false, exit loop; else, execute statement then check condition: if false...
}
do fun1() while (cond);     // `do-while`
for (int i = 0)
```

### Header Files
```c


```

### Arrays
```c

```

### Pointers
```c
int n = 5;
int * n_addr = &n   // A "pointer" is a address of some value in memory
                    // To get the memory address of a variable, use the ampersand operator
*n_addr = 8;        // Indirection operator (*) allows changing of value at the specified address
printf("%d", n);    // Prints "8"
```

## 1a. *The C Preprocessor*

- Scans code for preprocessor directives <u>before</u> compilation
- `#include <filename>` inserts the entirety of a file at this line 
- `#define <id> <definition>` defines an identifier whose definition is inserted <u>as-is</u> at every location it is used
    - Macros, by convention, use *SCREAMING_SNAKE_CASE*
    - Typically reserved for constants
    - Complex operations should be enclosed in parentheses to avoid operator precedence issues


### *Primitive Types*

## 4. Control flow

- Use `if`-statements to perform a procedure if a conditon is true
    - Condition implicitly converted to `bool`
    - Action may be a *nested scope* (enclosed in curly brackets)

```c
if ( <condition> ) <action> ;
```

- `else` can be appended to `if`-statements to perform some other procedure given that the previous condition is false
    - Procedures may be other `if`-statements
```c
if <...> else <alternative> ;
if <...> else if <...> else if <...> ; // if-else chain
```

- `while`-loops repeat some procedure for how many times some condition is true
- `do-while`-loops are the same, but always perform the procedure at least once
  - Condition is checked at end of procedure instead of beginning 

```c
while ( <condition> ) <action> ;
do <action> while ( <condition> );
```

- `for`-loops extend on `while`-loops by adding
    - Condition, init, and iterate are all
    - If condition is not given, defaults to `true`

```c
for ( <init?> ; <condition?> ; <iterate?>) <action> ;

<init?>                            // Equal to
while ( <condition? | true> ) {
    <action> ;
    <iterate?> ;
};
```