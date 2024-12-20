# COP 3514 Program Design - Exam 2 Review

<p style="text-align:center">
    <a href="../cop3514_textbook.pdf">textbook</a> |
    <a href="https://www.onlinegdb.com/online_c_compiler">c compiler</a> |
    <a href="https://www.onlinegdb.com/online_c++_compiler">c++ compiler</a>
</p>

## 1. Introduction to C++

- *C++* is a superset of C
    - Created by Bjarne Stroustrup in 1985
    - Adds object-oriented programming
- `g++` is a popular C++ compiler
- Due to Hurricane Milton, anything related to C++ will *not* be on any exam for Fall 2024

## 2. Array 

- Array *iteration* is the traversal through an array, one element at a time
    - Done so by use of a *counter variable*, typically named `i`
- For strings, the stop condition is reading the null character (`\0`)

```c
char *my_message[] = {"first", "second", "third"};
```

- Recall every array is itself a pointer to its first element
- Arrays can also be iterated through using pointer comparison
    - Keep track of current pointer using a variable
- To traverse forward, check if pointing to *tail* (last) element
    - Start with pointer to head, possibly the array variable itself
- To traverse backward, check if pointing to *head* (first) element
    - Start with pointer to tail

```c

```

### Array Iteration
```c
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

## 4. Advanced Format Specifiers

- In addition to type-based format specifiers, like `%d`, format specifiers as passed to `printf` and similar functions can be passed
    - Exclusion
    - Minimum # of characters

## 5. Command-line arguments

- 
```bash
./a.out "Hello, world"  # Program name, in this case "./a.out", is always first argument
                        # IMPORTANT: If "./" is used, it is also part of the first argument
```

-

```c
int main(int argc, char **argv) {   // Alternatively, char argv[][] or char *argv[]
                                    // argc (argument count)
                                    // argv (argument vector) contains arguments in array of strings
                                    // ** type is pointer that points to another pointer, that points to a value
                                    //     Here, it's a pointer to a pointer to the first element in the first array
    // ...
}
```
## 5. Two-Dimensional Arrays

- Arrays can contain other arrays
    - Such an array is called *two-dimensional*
- Two-dimensional

```c
int n_2d = {{}}
```

- ge

## 6. ASCII Character Codes

- ASCII is the character encoding most often used in C programming
    - Predecessor to Unicode
    - Spans first section of Unicode
- Each character is 7 bits, although `char` takes up 8 bits (1 byte)
    - Whether value is negative has no effect on encoded character

```c
char chr_a = 'a';
char int_a = 97;
if (chr_a == int_a) {
    printf("true");
}   // Output: true
```

- **Important:** Lowercase letters come *after* uppercase letters in the [ASCII table](https://www.asciitable.com/)

```c
char upper_a = 'A'; /* == 65 */
printf("%d", upper_a > chr_a);    // Output: 0 (false)
```