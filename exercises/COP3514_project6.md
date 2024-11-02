# COP 3514 - Project 6 Guide

*Original by Jing Wang of the University of South Florida*

Project 6, covering much of what we have learned in the course so far, is our most involved project yet. It's very easy to look at the instructions and be overwhelmed by the task at hand. Rather than thinking of this project as a one large complex problem, think of it as many smaller, more managable problems. Approach each problem one by one and slowly piece together the bigger picture.

Note this is a guide *not* a solution. Different approaches to various problems you may face with this project will be outlined below, concrete solutions will not. Keep in mind this is not the *only* way to look at this project and you are encouraged to explore alternatives.

## Simplified Directions

The goal of this program is to take a string of text from a file and convert it into a list of tokens (numbers). Along
with printing the tokens you will need to sort the words of the string in aphabetical order, print the number of unique words, *N*, and print those *N* words each on a newline. A word's **token** is its position aphabetically relative to the list of *N* unique words. When printing the tokens, you must print a newline after every period. All of these will be printed to an output file, not the console. The maximum length of the input file is 10,000 characters. There are no capital letters and the only delimiters will be whitespace (' ' and '\n) and periods ('.').

<u>**Example:**</u>

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

## Guide

*Note: The only code in any of the sections below will be something done in class or a simple demonstraion of a concept.*

### **File Input**

You're going to need to get the characters that are in the input file into your C program. To do this you will need some code to handle reading lines from a file.

A simple example of some code that reads a file:

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

Now, we need the whole file, not just one line. We can concatenate each line to a larger string to get the whole string.

Recall the concatenate function we built in class:

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

Using a combination of these two functions you should be able to read any whole file into a string.

### **String Processing**

Remember a string is simply an array of characters with a null terminator (`\0`) at the end. Printing every character in a string array string would look something like this "string\0". What if we put more characters after the null terminator and make something like this "string\0test\0"? Here's a C program that does just that:

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

With this technique, you can store more than one word in a single string. All you need to do is store pointers to specific parts of the string array.

Now, how is this helpful? We can now divide the main string up into its individual words by replacing whitespace or punctuation with null terminating characters and storing pointers to the start of each word. 

***You can store the pointers in an array.***

### **Sorting**

Once you have an array of word pointers, you're going to have to sort them into aphabetical order. You can use pretty much any common sorting algorithm you want to do this. A very common and simple example is ***bubble sort*** (pictured below).

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

For our array of strings we're going to need to modify the swapping condition. We need to see if the two words being compared are not in alphabetical order. To do this, we can make a function that will compare two strings. We need this function to take in two `char` pointers as arguments and compare each character of the two strings until a difference is found or a null terminator is encountered. This function will return 1 if the strings are out of alphabetical order, -1 if they are in the correct order and 0 if they are the same string. We must also return 1 if word 1 is **longer** than word 2 and word 2 fits inside word 1 (Ex. "in" and "inside". If "inside" was word 1 and "in" was word 2 they would need to be swapped because the shorter word must be first.) Here's an example of this function in ***pseudo-code***:

```
int word_comp(char* word1, char* word2) {
    initiallize ch1 and ch2 with word1 and word2 respectively

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

Once your array is sorted, you can remove the duplicates. Because the array of words is already sorted, the duplicates will be right next to each other. In the original example in the project instructions above the sorted array would look like this:

```
one
one
three
two
two
```

To remove the duplicates, create a new indexing variable separate from the main index used to loop through the array. Compare each word in the array with the word at the new array index you just created. If they are equal, skip and if they are diffent move the current word to your new indexing variable plus 1. If that was confusing, here's an example using the values above:

We can skip the first element since it's always unique. Now we compare `array[0]` with `array[1]` ("one" and "one"). They are the same word so we skip it and move on to the next word. Now we compare `array[0]` with `array[2]` ("one" and "three"). They are different so we set `array[0 + 1]` to `array[2]`. The array now looks like this:

```
one
three
three
two
two
```

To continue, we compare `array[1]` with `array[3]` ("three" and "two"). They are different so we set `array[1 + 1]` with `array[3]`. Next we compare `array[2]` with `array[4]` ("two" and "two"). They are the same word so we skip it. This is the final array:

```
one
three
two
two
two
```

Notice the last word, "two", is repeating. To fix this we can keep track of how many unique words there are. In this case there are 3 unique words. 

***This is the first value we need to print to the output file!***

When using this array, make sure to use it with the proper size (that being the number of unique words).
If you want to clean things up, you can loop through the array again and set the remaining pointers to `NULL`.

You can print every word in this new array using a simple `for` loop.

### File Output

File output is suprisingly straight foward in C. All you need to do is open the output file for writing and use `fprintf()` instead of `printf()`.

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

There are many ways to do this part. The goal is to compare every word in the original string with your new sorted and filtered array of words.
The token is equal to how far into the sorted array you go before you find the current word in the array. Here's an example:

Say the current word in the string is "two" and my sorted array of words is `one three two`. You would need to go 3 elements deep to find the word "two", therefore the token is 3.

You can use a `for` loop to match a given word with its position in the sorted array. Use the comparison function used for the sorting algorithm to find when the two words are equal.

### Below are some common issues when tokenizing and potential fixes:

#### How do I loop through the original string word by word?

- The simplest solution is to have two arrays of strings. One holding the original order of the words and one holding the sorted order of the words. This way you can loop through each word easily with a `for` loop.

#### How do I know when to print a newline?

- This can be tricky because if you're using an array holding just words it's likely all periods are gone. Periods should always be followed by a space or a newline meaning, depending on how you set up your string processing algorithm, there should be **two** null terminators at the end of a sentence. This means on every word, you can check if the two characters before it are `\0`. If they are, print a newline.

## Conclusion

Once again, this is just a general outline to be used to create your own solution. Experimentation is encouraged and to some extent, required. If you have any additional questions feel free to ask them in the discord.

Good luck :)
