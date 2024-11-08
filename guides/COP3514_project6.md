# COP 3514 - Project 6 Guide

*Original by Jing Wang of the University of South Florida*

**Disclaimer:** This is a guide *not* a solution.
Different approaches to problems you may face in this project are outlined below,
but not concrete solutions are not.
This is not the *only* way to look at this project, and you are encouraged to explore alternatives.

## Preliminary

Project 6, covering much of what we have learned in the course so far, is our most involved project yet.
It's very easy to look at the instructions and be overwhelmed by the task at hand.
Rather than thinking of this project as a one large complex problem, think of it as many smaller,
more manageable problems. Approach each problem one by one and slowly piece together the bigger picture.

## Plain-English Directions

The end goal of this program is to take a string of text from a file and convert it into a list of tokens (numbers). This project can be broken down into three main objectives:

**Objective 1:**

- On line 1, you will need to print the number of unique words, *N*.

**Objective 2:**

- On the following *N* lines print those *N* unique words in **alphabetical order**, each on a newline.

**Objective 3:**

- For each sentence you will need to print a single line of numbers separated by spaces referring to each word's position in the alphabetized list, in the order the words appear in the original input file. This number is referred to as a word's **token**. When printing the tokens, you must print a newline after every period.

All of these will be printed to an output file, not the console. Both the input file and the output file will be passed as **command line arguments**. The maximum length of the input file is 10,000 characters. There are no capital letters and the only non-alphabetical characters will be whitespace (`' '` and `'\n'`) and periods (`'.'`).

**Example:**

#### Command line: 
`./a.out file.in file.out`

#### file.in: 

```
one two three. 
two one.
```

#### file.out: 

```
3
one
three
two
1 3 2
3 1
```

There are three components to the output file in the example above:

- The number of unique words (1 line)
- *N* unique words (Next *N* lines)
- For *M* sentences, each sentence with its word replaced by its position in the above list (*M* lines)

## Guide

This guide will be broken down into multiple sections, each explaning a separate part of the project. 

**Note:** The only code in any of the sections below will be something done in class or a simple demonstration of a concept.

### **File Input**

***

The characters in the input file need a way to get into your C program. To do this you will need some code to handle reading lines from a file.

Here is a simple example of a C program that reads a file and prints each line:

```c
#include <stdio.h>
#define MAX_LEN 1000

int main() {
    char content[MAX_LEN + 1];

    FILE* fp = fopen("text.txt", "r");
    if(fp == NULL) {
        printf("File opening failed");
        return 1;
    }

    while(fgets(content, MAX_LEN, fp)) {
        printf("%s", content);
    }

    fclose(fp);
    return 0;
}
```

In this example, each line of the string is stored in `char content[]`.

Now, you need the whole file, not just one line. You can concatenate each line to a larger string to get the whole input string.

Recall the concatenate function built in class:

```c
void concatenate(char *s1, char *s2) {
    char *p, *q;
    for(p = s1; *p != '\0'; p++);

    for(q = s2; *q != '\0'; q++, p++) {
        *p = *q;
    }
    *p = '\0';
}
```

Using a combination of these two functions a whole file can be read into one string.

### **String Processing**

***

Remember, a string is simply an array of characters with a null terminator (`\0`) at the end. Printing every character in a string array string would look something like this: `string\0`. What if more characters are put after the null terminator to make something like this: `string\0test\0`?

Here is a C program built to demonstrate this:

```c
#include <stdio.h>

int main() {
    char str[] = "string\0test\0";
    char* word1 = &str[0];
    char* word2 = &str[7];

    printf("Word 1 is: %s\n", word1);
    printf("Word 2 is: %s", word2);

    return 0;
}
```

With this technique, more than one word can be stored in a single array. All you need to do is store pointers to specific parts of the string array.

Now, how is this helpful? The main string can now be divided up into its individual words by replacing whitespace or punctuation with null terminating characters and storing pointers to the start of each word. 

***The pointers to individual words can be stored in an array.***

### **Sorting**

***

Once you have an array of word pointers, the array needs to be sorted into alphabetical order. Pretty much any common sorting algorithm can be used to do this. A very common and simple example is ***bubble sort*** (pictured below).

```c
void bubbleSort(int a[], int n) {
    int i, j, temp;
    int swapped;

    for (i = 0; i < n - 1; i++) {
        swapped = 0;

        for (j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                swapped = 1;
            }
        }

        if (swapped == 0)
            break;
    }
}
```

For our array of strings, the swapping condition (the condition checked by the nested `if` statement) will need to be modified. The two words being compared need to be checked for alphabetical order. To do this, a function can be used to compare two strings.

This function needs to take in two `char` pointers as arguments and compare each character of the two strings until a difference is found or a null terminator is encountered. This function will return 1 if the strings are out of alphabetical order, -1 if they are in the correct order and 0 if they are the same string. The function must also return 1 if word 1 is **longer** than word 2 and word 2 fits inside word 1 (Ex. "in" and "inside". If "inside" was word 1 and "in" was word 2 they would need to be swapped because the shorter word must be first.) Here's an example of this function in ***pseudo-code***:

```
int word_comp(char* word1, char* word2) {
    initialize ch1 and ch2 with word1 and word2 respectively

    while (*ch1 and *ch2 aren't null terminators) 
        if (*ch1 comes before *ch2 alphabetically)     
            return -1;        
        
        if (*ch1 comes after *ch2 alphabetically) 
            return 1;          

        ch1++, ch2++;

    if (*ch1 and *ch2 are both null terminators after the while loop) 
        return 0;       
    
    if (*ch2 ended before *ch1) 
        return 1;               
    
    return 0;                 
}
```

### **Duplication Removal**

***

Once your array is sorted, the duplicates must be removed. Because the array of words is already sorted, the duplicates will be right next to each other. In the original example in the project instructions above, the sorted array would look like this:

```
one
one
three
two
two
```

To remove the duplicates, create a new indexing variable separate from the main index used to loop through the array. Compare each word in the array with the word at the new array index just created. If they are equal, skip and if they are different, copy the current word to the new indexing variable plus 1. Here's an example using the words above to hopefully clear this concept up:

The first element can be skipped since it's always unique. Now compare `array[0]` with `array[1]` ("one" and "one"). They are the same word so it's skipped. Now compare `array[0]` with `array[2]` ("one" and "three"). They are different so `array[0 + 1]` is set to `array[2]`. The array now looks like this:

```
one
three
three
two
two
```

To continue, compare `array[1]` with `array[3]` ("three" and "two"). They are different so set `array[1 + 1]` to `array[3]`. Next compare `array[2]` with `array[4]` ("two" and "two"). They are the same word so it's skipped. This is the final array:

```
one
three
two
two
two
```

Notice the last word, "two", is repeating. To fix this you can keep track of how many unique words there are. In this case there are 3 unique words. 

***This is the first value that needs to be printed to the output file!***

When using this array, make sure to use it with the proper size (that being the number of unique words).
If you want to clean things up, you can loop through the array again and set the remaining pointers to `NULL`.

Every word in this newly sorted array can be printed using a simple `for` loop.

### **File Output**

***

File output is surprisingly straight forward in C. All you need to do is open the output file for writing and use `fprintf()` instead of `printf()`.

```c
#include <stdio.h>

int main() {
    FILE* fw = fopen("text.txt", "w");
    if(fw == NULL) {
        printf("File opening failed");
        return 1;
    }

    fprintf(fw, "Hello World\n");

    //your code goes here

    //make sure to close file at the end of main
    fclose(fw);
    return 0;
}
```

### **Tokenizing**

***

There are many ways to do this part. The goal is to compare every word in the original string with the new sorted and filtered array of words.
The token is equal to how far into the sorted array the current word is located. Here's an example:

Say the current word in the string is "two" and the sorted array of words is `one three two`. You would need to go 3 elements deep to find the word "two"; therefore, the token is 3.

A `for` loop can be used to match a given word with its position in the sorted array. Use the comparison function used for the sorting algorithm to find when the two words are equal.

### Below are some common issues when tokenizing and potential fixes:

#### How do I loop through the original string word by word?

- The simplest solution is to have two arrays of strings. One holding the original order of the words and one holding the sorted order of the words. This way you can loop through each word easily with a `for` loop.

#### How do I know when to print a newline?

- This can be tricky because if you're using an array holding just words it's likely all periods are gone. Periods should always be followed by a space or a newline meaning, depending on how you set up your string processing algorithm, there should be **two** null terminators at the end of a sentence. This means on every word, you can check if the two characters before it are `\0`. If they are, print a newline. This issue is very dependent on how your program is set up so it's likely you may need to find your own solution to this problem.

### **Using Structures**

***

Structures are not technically required for this project; however, using them may prove to be useful. Structures (also called structs) are used when grouping data could be helpful. In this project for example, you may want to group a word's pointer with its token. You can think of a struct like a class that can only have member variables (no functions). Here are some examples of structs, and how they can be used in C:

```c
#include <stdio.h>

//Struct declaration

struct Entity {
    int a;
    int b;
    char c;
};

int main() {

    struct Entity entity1;      //Struct instance

    entity1.a = 2;
    entity1.b = 3;
    entity1.c = 'a';

    printf("%d\n", entity1.a);
    printf("%d\n", entity1.b);
    printf("%c\n", entity1.c);

    //You can also make pointers to structs.

    struct Entity* entity1_ptr = &entity1;

    //The arrow operator ('->') will dereference a pointer to a struct 
    //and access a member variable within that struct at the same time.

    entity1_ptr->a = 4;         //entity1_ptr->a == (*entity1_ptr).a
    entity1_ptr->b = 5;
    entity1_ptr->c = 'b';

    printf("%d\n", entity1_ptr->a);
    printf("%d\n", entity1_ptr->b);
    printf("%c\n", entity1_ptr->c);

    return 0;
}
```

You can also create arrays of structs, which may be helpful in this project.

```c
#include <stdio.h>
#define SIZE 5

//You can also create a struct using this syntax.
//It eliminates the need to type "struct" before every instance of the struct.

typedef struct {
    int a;
    int b;
    char c;
} Entity;

int main() {

    //Notice the word "struct" is missing from the declaration.
    Entity entity_arr[SIZE];

    for (int i = 0; i < SIZE; i++) {
        entity_arr[i].a = i;
        entity_arr[i].b = (i + 1);
        entity_arr[i].c = 'a' + i;
    }

    for (int i = 0; i < SIZE; i++) {
        printf("%d\n", entity_arr[i].a);
        printf("%d\n", entity_arr[i].b);
        printf("%c\n", entity_arr[i].c);
    }

    return 0;
}
```

Again, using structs is not required, but they can help organize your code and better manage data.

## Conclusion

Remember, this is just a general outline to be used to create your own solution. Experimentation is encouraged and to some extent, required. If you have any additional questions feel free to ask them in the discord.

Good luck :)
