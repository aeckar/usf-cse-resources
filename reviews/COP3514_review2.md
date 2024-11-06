# COP 3514 Program Design - Exam 2 Review

<p style="text-align:center">
    <a href="../textbooks/COP3514_textbook.pdf">textbook</a>
</p>

## 1. Overview of C++

- *C++* is a superset of C
    - Created by Bjarne Stroustrup in 1985
    - Adds object-oriented programming
- `g++` is a popular C++ compiler
- Due to Hurricane Milton, anything related to C++ *will not* be on any exam for Fall 2024
- Also due to the hurricane, file I/O will not be on exam 2 for Fall 2024

## 2. C++ Syntax
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

## 3. More C Concepts
### Array Iteration
```c
int arr[] = {1,2,3};
int arr_size = 3;

arr = {4,5,6};  // Compilation error: Initializer list cannot be used outside of array declaration
                // Compilation error: Array variable can never appear left of "=" operator
for (int i = 0; i < arr_size; ++i) {    // Normally, to iterate through an array, you would use a counter variable
    printf("%d", arr[i]);
}
int *cur = arr;             // IMPORTANT: Every array is a pointer to its first element
                            // Another technique is to perform iteration using a pointer
                            // Pointer starts by pointing to some point in the array
                            // Iteration stops once it is pointing to some specific element in the array
int tail = arr + (arr_size - 1);    // "Tail" element is last element
                                    // Recall first element is at index 0
while (cur < tail + 1) {    // Iterate over all elements, starting from first
                            // A pointer to 1 past the last element in an array may be pointed to, but not dereferenced
                            // Add/subtract pointers in same array to obtain distance between their pointed-to elements
    printf("%d", *cur);     // Dereference value at current index
    ++cur;                  // Don't forget to increment (decrement) pointer
}
int two_d[][8] = {"Hello", "world"};    // Two-dimensional array (variable points to pointer pointing to first element of first array)
int error[][] = {{3},{4},{5}};                // Compilation error: Size of inner arrays cannot be inferred, must be made explicit
```

### String Manipulation
```c
#include <stdio.h>                      // Import puts()
#include <string.h>                     // Contains utility functions related to strings

// ...

char *str = "Meet my outside COT, I bet you won't";
         // ['M', 'e', 'e', ..., 'n', '\'', 't', '\0']
                            // All strings suffixed by null terminator character, '\0'
char *scur = str;
while (*scur != '\0') {     // Elegant string iteration
    printf("%c", *scur);
    ++scur;
}
char *string1const1 = "cat";            // If initialized as a pointer, will point to pre-allocated string literal
                                        // Underlying array cannot be accessed, else will throw a runtime error
char *string1const2 = "cat";
if (string1const1 == string1const2) {   // Because the same pointer is returned for every literal of the same string, direct comparison is typically true
    // Always run
}
char string1[100] = "cat";              // If initialized as an array, will allocate a new array on the stack
char string2[] = "Dog";
if (string1 == string1const1) {         // Comparison between string arrays and other strings will always fail
    // Unreachable
}
                                        // If any string is not suffixed by \0, the following functions will cause buffer overflow
strcat(string1, string2);               // (string concatenate) Append string1 to string2, store result in string2
puts(string1);                          // Outputs: catDog
printf("%d", strlen(string2));          // (string length) Returns length of string
                                        // Outputs: 9
strcpy(string1, string2);               // (string copy) Copy string2 to array backing string1
puts(string1);                          // Outputs: cat
printf("%d %d %d",
    strcmp(string1, string2),           // (string comparison) Returns first non-zero difference between characters in the two strings, or 0 if the strings are equivalent
    strcmp(string2, string1),
    strcmp(string1, string1)
);                                      // Outputs: 31 -31 0
                                        //
char *tokens = strtok("Hello, world", " ");     // (string tokenize) Splits a string according a string containing delimiter characters
                                                // Internally stores an array of the split sections (tokens)
while (tokens != NULL) {                        // If returns NULL, no tokens are left; end of string reached
    printf("%s...", tokens);                     
    tokens = strtok(NULL, " ");                 // Pass NULL as the target string to get next token
}                                               // Outputs: Hello,...world...

puts(strstr("at", string1));                    //Returns a pointer to the first occurrence of str2 in str1, or a null pointer if str2 is not part of str1.
                                                // Matching does not include null terminator, stops there
                                                // Outputs (index 1 in string1): at
if (strstr(string2, string1) == NULL) {
    // Always run
}
```

### Command-line arguments
```bash
./a.out "Hello, world"  # Program name, in this case "./a.out", is always first argument
                        # IMPORTANT: If "./" is used, it is also part of the first argument
```

```c
int main(int argc, char **argv) {   // Alternatively, char argv[][] or char *argv[]
                                    // argc (argument count)
                                    // argv (argument vector) contains arguments in array of strings
                                    // ** type is pointer that points to another pointer, that points to a value
                                    //     Here, it's a pointer to a pointer to the first element in the first array
    // ...
}
```

### ASCII

- ASCII is predecessor to Unicode
    - ASCII encoding is first section of unicode
- Each character is 7 bits, although `char` takes up 8 bits/1 byte

```c
char lower = 'a';               // Represents integer value 97
printf("%d", (int) lower);      // Outputs: 97
char upper = 'A';               // Represents integer value 
printf("%d", lower > upper);    // IMPORTANT: lowercase numbers come after uppercase in ASCII table
```