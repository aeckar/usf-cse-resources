# COP 3514 Program Design - Final Exam Review

<p style="text-align:center">
    <a href="../textbooks/COP3514_textbook.pdf">textbook</a>
</p>

## 1. File I/O

- Files can be opened in three modes:
    - **Read `r`:** Traverse characters in file in one direction
    - **Write `w`:** Write to file in one direction
    - **Append `a`:** Write to file, with changes placed at end of file
- These modes passed to `fopen` to denote how a file will be used

| Function                          | Purpose                                                   |
|-----------------------------------|-----------------------------------------------------------|
| `fgetc(FILE *)`                   | Reads a single character                                  |
| `fscanf(FILE *, char *, ...)`     | Reads one or more values according to the format string   |
| `fputc(int, FILE *)`              | Writes a single character                                 |
| `fprintf(FILE *, char *, ...)`    | Writes one or more values according to the format string  |

```c
#include <stdio.h>  // Contains utilities for reading/writing files

FILE *file = fopen("/file/path/here");  // Open file in desired mode
                                        // FILE * is a struct representing a file
                                        // No need to know FILE specifics
fclose(file);   // All files opened must be closed to prevent resource leak
```

## 2. Dynamic Memory Allocation

- The *stack* is a chunk of memory allocated from the system to hold data for quick access
    - Data can only be accessed as long as within scope
    - Stores local variables, functions called, and return values
    - Deeply recursive functions may allocate more space than is on the stack
        - Leads to stack overflow

```c

int n;  // Local variables set aside space on the stack to store data
```

- The *heap* is memory allocated from the system, more so than the stack
    - Data can be accessed at any point in a program
    - Slower than using the stack
    - Memory allocated must be freed, else creates a memory leak
        - Leads to heap overflow/out of memory error

```c
#include <stdlib.h> // Contains miscellaneous standard library utilities

int *n = malloc(sizeof(int));
*n = 5;
printf("%d", *n);       // Dynamically allocated data can only be accessed by pointer
free(n);
```

- Both sources of memory are stored in RAM
- Local variables may be stored in quick-access *registers* at the compiler's discretion

## 3. Function Pointers & Composition

linked list (struct)

function pointers

## 4. Project Organization

multifile programs

makefiles

***UP-TO-DATE***