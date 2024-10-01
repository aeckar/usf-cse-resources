# COP 3514 Program Design - Exam 1 Review

<ins>Textbook</ins>: *C Programming: A Modern Introduction (2nd ed.)* by K. N. King

### Preliminary - Accessing the Student Cluster

#### Windows Setup

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

#### Sending Files to/from the Cluster on Windows

1. Sign-in to the Cluster using the above directions
2. Open a Windows command prompt (cmd.exe) with PuTTY installed
3. Type `pscp -r <from directory> <netid>@sclogin1:<to directory>`

#### Using the Cluster

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

### 1. Introduction to C

- *C* is a high-level programming language
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

### 1a. *The C Preprocessor*

- Scans code for preprocessor directives <u>before</u> compilation
- `#include <filename>` inserts the entirety of a file at this line 
- `#define <id> <definition>` defines an identifier whose definition is inserted <u>as-is</u> at every location it is used
    - Macros, by convention, use *SCREAMING_SNAKE_CASE*
    - Typically reserved for constants
    - Complex operations should be enclosed in parentheses to avoid operator precedence issues

### 1b. *Header Files*

- Prd

### 2. Program Structure

- Pro

### 2a. *Low-Level Program Structure*

- Pro

### 3. Variables

- Pro

### 3a. *Primitive Types*

- Pro

Operators


### 3b. *The `bool` Type*

- Not a keyword, unlike other primitives
- Defined in the header file `stdbool.h`, it is a macro standing for the actual keyword `_Bool`
    - This is done to preserve compatibility with code created before booleans were added
- Prefer over using the integers `1` and `0`
- Any non-zero value is equal to `true`, while only zero is equal to `false`
- Casting a boolean back to a numeric type will only give `1` or `0`

Operators
+

### 4. Control flow

- Pro

### 5. Functions

- Pro

### 6. Arrays

- Pro

### 6a. *Arrays as Pointers*

- Pro

### 7. Pointers

- Pro
