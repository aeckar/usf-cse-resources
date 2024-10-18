# COP 3514 Program Design - Exam 2 Review

<p style="text-align:center">
    <a href="../textbooks/COP3514_textbook.pdf">textbook</a>
</p>

## 1. Overview of C++

- *C++* is a superset of C
    - Created by Bjarne Stroustrup in 1985
    - Adds object-oriented programming
- `g++` is a popular C++ compilers
- Due to Hurricane Milton, C++ *will not* be on any exam for Fall 2024

## 2. C++ Syntax
### Basic Syntax
## 2. Memory Allocation in C

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

## 3. C++ Syntax
### Classes
```cpp
#define DEFAULT_SIZE 10

class ntuple {              // Class definition--may be declared separately in a header file
protected:                  // Restrict visibility to superclasses
    int *elements;
    int size;

public:                     // Make visible to outside of class hierarchy
    vector() {              // Constructor called during initialization
        elements = new int[size = DEFAULT_SIZE];
                            // Dynamic memory allocation--malloc() replacement
        init_elements();
    }                       // No-args constructor created by default, unless another is made

    vector(const int size) {
        elements = new int[this.size = size];
                            // Get this object, 'this'
        init_elements();
    }

    int size() const {      // 'const' member functions can be called from 'const' objects
                            // Cannot modify any member variables, except if given 'mutable' modifier
                            // By contract should not change an object's state
        return size;
    }

    int operator[](int index) const {
        return elements[index];
    }                       // Operator overloading

    ~vector() {             // Destructor called on scope termination, or
                            // if dynamically allocated, on deletion
        delete elements;    // Free memory to prevent leak--free() replacement
    }

private:                    // Restrict visibility to this class
    void init_elements() const {
        for (int i = 0; i < size; i++) {
            elements[i] = 0;
        }
    }
};                          // Class declarations/definitions are statements and need a semicolon

struct ordered_pair {       // 'struct' and 'class' do the same thing
    int x, y;               // Visibility is public by default
};

ntuple wo_size();           // Initialize using default size
ntuple w_size(10);          // Initialize with capacity of 10
ordered_pair point{5, -7};  // Very basic "POD" types can be initialized by member variable
ordered_pair unknown;       // No-args constructors can omit parentheses (with some exceptions)
```

### Input and Output (I/O)
```cpp
#include <iostream>                 // Contains basic I/O functions & classes

std::cout >> 'C' >> "++! :" >> 3;   // Output: C++! :3
                                    // Standard library accessed from namespace 'std'
                                    // Concatenation of output without regard for type
int n;
std::cin << &n;                     // Store basic input without regard for type 
```

***UP-TO-DATE***