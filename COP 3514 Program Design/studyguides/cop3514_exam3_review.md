# COP 3514 Program Design - Final Exam Review

<p style="text-align:center">
    <a href="../cop3514_textbook.pdf">textbook</a> |
    <a href="https://www.onlinegdb.com/online_c_compiler">c compiler</a>
</p>

## 1. Composite Structures

- Programmers can define their own, composite types using the `struct` keyword
    - `struct`s contain *member variables*, similar to properties in object-oriented languages
- Member variables accessed using the `.` operator
- **Important:** Member variables hold garbage values on declaration of a `struct`
    - Care must be taken to ensure **all** member variables are initialized properly

```c
#define MAX_NAME_LENGTH 99

struct person { // 'person' type
    int birth_year;
    char name[MAX_NAME_LENGTH + 1 /* null character */];
    double balance;
};

int main() {
    struct person mike; // Currently, members contain garbage values
    mike.birth_year = 2001;
    mike.balance = 0.62;
    strcpy(mike.name, "Mike");
    printf("%s, %d", mike.name, mike.birth_year);   // Output: Mike, 2001
    return 0;
}
```

- One can create pointers to structs just like regular values
    - Through dereference, member variables of an existing instance can be modified

```c
struct person *to_mike = &mike;
(*to_mike).birth_year = 1999;
printf("%d", (*to_mike).birth_year);    // Output: 1999
```

- The `->` operator provides a convenient syntax for accessing members of a struct being pointed to
    - Shorthand for `*` and `.` operators

```c
strcpy(to_mike->name, "Michael");
printf("%s", to_mike->name);    // Output: Michael
```

- When passing `struct`s to functions, it is generally best to pass by reference
- Because `struct` declarations are statements, they must be followed by a semicolon (`;`)

## 2. File Handling

- The standard header file `stdio.h` provides functions to read from/write to files

#### **Figure 1.** Common `stdio.h` Functions for File I/O
| Function                              | Purpose                                                                   | Modes                 |
|:--------------------------------------|:--------------------------------------------------------------------------|:----------------------|
| `fprintf(FILE *, char *, ...)`        | Writes one or more values according to the format string                  | `w` `a`               |
| `fscanf(FILE *, char *, ...)`         | Reads one or more values according to the format string                   | `r`                   |
| `fputc(int, FILE *)`                  | Writes a single character                                                 | `w` `a`               |
| `fgetc(FILE *)`                       | Reads a single character                                                  | `r`                   |
| `fputs(char *, FILE *)`               | Writes the string to the file, not including the null character (`'\0'`)  | `w` `a`               |
| `fputs(char *, int count, FILE *)`    | Reads at most `count - 1` characters from the file into the string        | `r`                   |
| `feof(FILE *)`                        | Returns true if at the end of the given file                              | <small>*all*</small>  |
| `fclose(FILE *)`                      | Gives control of a file back to the operating system                      | <small>*n/a*</small>  |

- *Mode strings* passed to `fopen` to denote how a file will be used

#### **Figure 2.** `fopen` File Modes
| Mode      | Specifier | Description                                                                           |
|:---------:|:---------:|:--------------------------------------------------------------------------------------|
| read      | `r`       | Read characters from file, assuming the file exists                                   |
| write     | `w`       | Write characters to file, creating a new file if one does not exist                   |
| append    | `a`       | Write characters at the end of the file, creating a new file if one does not exist    |

- `FILE` is a structure defined in `stdio.h` that represents a file in memory
    - Accessed through pointers, `FILE *`, although these do not need to be `free`d
    - **Important:** All file pointers **must** be closed using `fclose`

```c
#include <stdio.h>  // Import file input/output utilities

// ...

FILE *file = fopen("/file/path/here", "w"); // Open file for writing, or make a new one if does not exist
fprintf("%d", 69);
fclose(file);   // All files opened must be closed to prevent resource leak
// File contents: 69
```

- `-1`, as returned by `fgetc`, represents the end of the file, `EOF`

```c
// File contents: Hello!\nWorld!

FILE *my_file = fopen("./my/file.md", "r");
int c;
while ((c = fgetc(my_file)) != -1) {    // Read all characters from file
    printf("%c", c);
}   // Output: Hello!\nWorld!
fclose(my_file);    // Important! Prevent resource leak
```

- `fprintf` and `fscanf` work like their console counterparts
- **Important:** If `fputs` reads a newline (`'\n'`) character, it stops reading into the array
    - The newline character is *not* stored in the string

```c
// File contents: Hello\nWorld!

#define MAX_LINE_LENGTH 100

FILE *source = fopen("main.c", "r");
char line[MAX_LINE_LENGTH];
while (!feof()) {
    fgets(line, MAX_LINE_LENGTH, source);   // Overwrite characters in array for each line
    printf("%s... ", line);
}   // Output: Hello... World!...
fclose(source);
```

## 3. Dynamic Memory Allocation

- The `sizeof` operator does two things
    - For value with an array type, such as `char[]`, evaluates to total size of array, in bytes
    - For all other values, evaluates to size of that value, in bytes
- **Important:** Invoking `sizeof` on pointer values does *not* evaluate to size of memory block being pointed to
    - Instead, returns size of a memory address

```c
// ...assume size of 'int' is 4 bytes, and size of memory address is 64 bits (8 bytes)

int int_size = sizeof(int); // == 4
int n[] = {1,2,3,4,5};    // sizeof(n) == sizeof(int) * 5
int total_elements = sizeof(n) / sizeof(int)    /* == (4 * 5) / 4, or 5 */
int *first_element = n;
int addr_size = sizeof(m) / sizeof(int) /* == 8 / 4, or 2 (NOT the size of the array) */
```

- The *stack* is a chunk of memory allocated from the system to hold data for quick access
    - Data can only be accessed as long as within scope
    - Stores local variables, functions called, and return values

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
   ──┬──────────────────┬───┬───┬───┬───┬───────────────────────────────────────────┐
 ... | (return address) | 1 | 2 | 3 | n |        (remaining space in stack)         |
   ──┴──────────────────┴─⇑─┴───┴───┴─║─┴───────────────────────────────────────────┘
                          ╚═══════════╝
```

- Infinitely recursive functions may allocate more space than is on the stack
    - Leads to stack overflow
- The *heap* is memory allocated from the system not on the stack
    - Data can be accessed at any point in a program
    - Slower than using the stack, as it is random-access instead of last-in-first-out
- Memory allocated must be freed, else creates a memory leak
    - Leads to heap overflow/out of memory error
- Heap-allocated memory must be initialized to prevent access to garbage values, just like stack-allocated (local) memory

```c
#include <stdlib.h> // Import dynamic memory allocation utilities

int *n = malloc(sizeof(int) * 2);   // Allocate a block capable of holding two integers on the heap 
n[0] = 5;
*(n + 1) = 6;   // Same as n[1] = 6
{
    printf("%d", *n);       // Dynamically allocated data can only be accessed by pointer or subscript
}   // Output: 5
free(n);
```

```txt
                       Heap
           ┌─────────────────────────┐
int *n ══╗ |            ┌──────────┐ | <─┬─ other malloc'd blocks of memory
         ║ |            └──────────┘ |   |
         ║ |  ┌───┬───┐              |   |
         ╚══> | 5 | 6 |       ┌──┐   |   |
           |  └───┴───┘       |  |   | <─┘
           |                  └──┘   |
           └─────────────────────────┘
```

## 4. Memory Safety Violations

- **Important:** A *dangling pointer* is use of a pointer whose address is an already `free`d block of memory
    - See [here](https://stackoverflow.com/questions/17997228/what-is-a-dangling-pointer)

```c
int *num = malloc(sizeof(int));
*num = 5;
printf("%d", *num); // Output: 5

int *alias = num;
free(num);
num = NULL;
printf("%d", *alias);   // Runtime error: value pointed to by 'alias' is undefined
```

```txt
Step 1. Variables point to same address in heap.

                          Heap
              ┌─────────────────────────┐
              |  ┌───┐     ┌──────────┐ |
  int *num ════> | 5 |     |          | |
              |  └───┘     └──────────┘ |
              |    ⇑    ┌──┐            |
  int *alias ══════╝    |  |            |
              |         └──┘            |
              └─────────────────────────┘

Step 2. Memory at that address is returned to system using free().

                         Heap
         NULL ┌─────────────────────────┐
          ⇑   |  ┌┄┄┄┐     ┌──────────┐ |
int *num ═╝   |  ┊   ┊     |          | |
              |  └┄┄┄┘     └──────────┘ |
              |    ⇑    ┌──┐            |
int *alias ════════╝    |  |            |
              |         └──┘            |
              └─────────────────────────┘

Step 3. 'alias' is mistaken to still be pointing to useable memory. Any values read are undefined.

                         Heap
         NULL ┌─────────────────────────┐
          ⇑   |            ┌──────────┐ |
int *num ═╝   |            |          | |
              |            └──────────┘ |
              |    ⇑    ┌──┐            |
int *alias ═════X══╝    |  |            |
              |         └──┘            |
              └─────────────────────────┘
```

- **Important:** A *memory leak* is when data allocated using `malloc` is never freed
    - See [here](https://stackoverflow.com/questions/3373854/what-is-a-memory-leak)
- Without `free`ing that data, the block of memory is no longer usable by another other program, even if that one terminates
    - Can cause system to run out of useable memory

## 5. Introduction to Linked Lists

- A *linked list* is a data structure where each element is its own structure, called a *node*
    - The variable representing the list, like an array, is a pointer to the first element
- Every node contains member variables containing information specific to that element
- **Important:** When inserting/removing elements in a linked list, elements must remain linked
- An empty list is represented by a `NULL` pointer
- A *stack* is a list that can only insert or remove elements from one end
    - Last-in-first-out (LIFO) order
- A *queue* is a list that inserts elements at one end and removes elements from the other
    - First-in-first-out (FIFO) order
    - *"First come, first serve"*
- In the following sections, the terms *element* and *node* will be used interchangeably

## 6. Singly-Linked Lists

### ***i.* Introduction**

- In a *singly-linked* list, every node holds a pointer to the next element
    - For the last element, the next element is `NULL`
- The final exam will primarily deal with singly-linked lists

```txt
     Element 0              Element 1              Element 2
┌───────────┬──────┐   ┌───────────┬──────┐   ┌───────────┬──────┐
│  members  | next ══> │  members  | next ══> │  members  | next ══> NULL
└───────────┴──────┘   └───────────┴──────┘   └───────────┴──────┘
         ⇑
 struct node *list
```

- Typical layout of a singly-linked node is below

```c
struct node {
    // member variables here
    struct node *next;  // Next node in list, or NULL if this is the last element
};
```

- An example node `struct` is below

```c
#define NAME_LEN 100
#define NETID_LEN 40

struct person {
	char name[NAME_LEN+1], netid[NETID_LEN+1];
	int attempts;
	struct person *next;
};
```

### ***ii.* Get Head Element**

- The *head* of a list is its first element
- As a pointer to its first element, the head of a linked list is itself
    - Analogous to how an array works

```c
struct person *list = malloc(sizeof(struct person))
struct person *head = list;    // Points to first person

strcpy(head->name, "Mike");
strcpy(head->netid, "Hawk");
head->attempts = 1;
head->next = NULL;  // IMPORTANT: remember to initialize pointer to next node

int size = 1;
struct person *current_node = head;
for (int i = 0; current_node != NULL /* stop if there is no next element */ && i < size; i++) {
    printf("%s (attempt %d)", current_node->name, current_node->attempts + 1);
    current_node = current_node->next;
}   // Output: Mike (attempt 3)
```

- Here, `current_node` is a pointer to the element the program is currently at
    - **Important:** Does not hold the actual value of the element structure
- In diagram form, the above list looks like the following

```txt
List elements: [Mike]

        (head)
     ┌─────────┬──┐
     │ "Mike"  │  │
     │ "mhawk" |  ══> NULL
     │ 2       |  │
     └─────────┴──┘
          ⇑
  struct person *list
```

### ***iii.* Traversal/Get Tail Element**

- The *tail* of a list is its last element
- To get the tail node, keep track of the current node until the `next` node is `NULL`
- On the way to the tail element, every element is visited
    - Can be used to obtain values contained by every node
- The function the following procedures are in returns the new head element

```c
// List elements: [Mike, Barry, Steve]

if (list == NULL) { // List is empty, there is no tail
    return NULL;    // Return null in place of head
}

current_node = head
while (current_node->next != NULL) {    // Go to next element until at tail
    current_node = current_node->next;
}
// Current node is tail element
printf("%s (attempt %d)", current_node->name, current_node->attempts + 1);  // Output: Steve (attempt = 1)
```

```txt
List elements: [Mike, Barry, Steve]

        (head)                               (tail)
     ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐
     │ "Mike"  │  │   │ "Barry"   │  │   │ "Steve"  │  │
     │ "mhawk" |  ══> │ "bockner" │  ══> │ "ssmith" |  ══> NULL
     │ 2       |  │   │ 1         │  │   │ 0        │  │
     └─────────┴──┘   └───────────┴──┘   └──────────┴──┘
           ⇑
   struct person *list
```

### ***iv.* Insertion**

- Elements can be inserted into the list according to a specified ordering
- By inserting at beginning or end of list, stack or queue can be implemented
- Insertion of a new `person` to the list in descending order according to `attempts`, for multiple scenarios is below
    - If a duplicate is found, new node is placed at the end

```c
// List elements: [Mike, Barry, Steve]

if (list == NULL) { // List is empty
    return NULL;
}

struct person *new_node = malloc(sizeof(struct person));
strcpy(new_node->name, "John");
strcpy(new_node->netid, "jpork");
new_node->attempts = 1;
new_node->next = NULL;

current_node = head;
struct node *previous = NULL;
while (current_node->attempts >= new_node->attempts) {
    if (current_node->next == NULL) {
        // At this point, current node is tail AND is greater than/equal to new node
        current_node->next = new_node
        return head;    // Return old head
    }
    previous = current_node;    // On next iteration, this element will be the previous one
    current_node = current_node->next;  // Move to next element
}
if (previous == NULL) {
    // At this point, (first node)->attempts < new_node->attempts
    // Designate new node as head
    new_node->next = head;
    return new_node;    // Return new head
}
previous->next = new_student;   // Link previous to new node
new_node->next = current_node;  // Link new node to current
return head;    // Return old head
```

```txt
List elements: [Mike, Barry, Steve]

Element to be inserted
   ┌─────────┬──┐
   | "John"  |  |
   | "jpork" |  ══> NULL
   | 1       |  |
   └─────────┴──┘

Step 0. Original list
   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐
   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  | 
   | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══> NULL
   | 2       |  |   | 2         |  |   | 0        |  |
   └─────────┴──┘   └───────────┴──┘   └──────────┴──┘ 
         ⇑
 struct node *list (list variable)

Step 1. Compare the new node to the first node.
If the current is greater than/equal to the new one, insert new node before that one.
Otherwise, continue.

   ┌─────────┬──┐
   | "John"  |  |
   | "jpork" |  ══> NULL
   | 1       |  |
   └─────────┴──┘
         ↕
   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐
   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  | 
   | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══> NULL
   | 2       |  |   | 2         |  |   | 0        |  |
   └─────────┴──┘   └───────────┴──┘   └──────────┴──┘ 
         ⇑
 struct node *list

Step 2. Compare the new node to the first node.
If the current is greater than/equal to the new one, insert new node before that one.
Otherwise, continue.

                    ┌─────────┬──┐
                    | "John"  |  |
                    | "jpork" |  ══> NULL
                    | 1       |  |
                    └─────────┴──┘
                          ↕
   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐
   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  | 
   | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══> NULL
   | 2       |  |   | 2         |  |   | 0        |  |
   └─────────┴──┘   └───────────┴──┘   └──────────┴──┘ 
         ⇑
 struct node *list

Step 3. Compare the new node to the first node.
If the current is greater than/equal to the new one, insert new node before that one.
Otherwise, continue.

                                       ┌─────────┬──┐
                                       | "John"  |  |
                                       | "jpork" |  ══> NULL
                                       | 1       |  |
                                       └─────────┴──┘
                                             ↕
   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐
   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  | 
   | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══> NULL
   | 2       |  |   | 2         |  |   | 0        |  |
   └─────────┴──┘   └───────────┴──┘   └──────────┴──┘ 
         ⇑
 struct node *list

Step 4. Node with value less than new node found. Link previous to new node, and new node to current node.

                                          ┌─────────┬──┐
                                          | "John"  |  |
                                     ╔══> | "jpork" |  ══╗
                                     ║    | 1       |  | ║
                                     ║    └─────────┴──┘ ║
                                     ║  ╔════════════════╝
   ┌─────────┬──┐   ┌───────────┬──┐ ║  ║   ┌──────────┬──┐
   | "Mike"  |  |   | "Barry"   |  | ║  ║   | "Steve"  |  | 
   | "mhawk" |  ══> | "bockner" |  ══╝  ╚═> | "ssmith" |  ══> NULL
   | 2       |  |   | 2         |  |        | 0        |  |
   └─────────┴──┘   └───────────┴──┘        └──────────┴──┘ 
         ⇑
 struct node *list

Step 5. Insertion is successful.

   ┌─────────┬──┐   ┌───────────┬──┐   ┌─────────┬──┐   ┌──────────┬──┐
   | "Mike"  |  |   | "Barry"   |  |   | "John"  |  |   | "Steve"  |  | 
   | "mhawk" |  ══> | "bockner" |  ══> | "jpork" |  ══> | "ssmith" |  ══> NULL
   | 2       |  |   | 2         |  |   | 1       |  |   | 0        |  |
   └─────────┴──┘   └───────────┴──┘   └─────────┴──┘   └──────────┴──┘
         ⇑
 struct node *list 
```

- For insertion at the beginning of the list, the new node is linked to the head element
    - The new node becomes the first element, so it becomes the new head

```txt
List elements: [Mike, Barry, Steve]

Element to be inserted
   ┌─────────┬──┐
   | "Rich"  |  |
   | "rbig"  |  ══> NULL
   | 3       |  |
   └─────────┴──┘

Step 0. Original list

   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐
   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  | 
   | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══> NULL
   | 2       |  |   | 2         |  |   | 0        |  |
   └─────────┴──┘   └───────────┴──┘   └──────────┴──┘ 
         ⇑
 struct node *list

Step 1. Compare the new node to the first node.
If the current is greater than/equal to the new one, insert new node before that one.
Otherwise, continue.

   ┌─────────┬──┐
   | "Rich"  |  |
   | "rbig"  |  ══> NULL
   | 3       |  |
   └─────────┴──┘
         ↕
   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐
   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  | 
   | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══> NULL
   | 2       |  |   | 2         |  |   | 0        |  |
   └─────────┴──┘   └───────────┴──┘   └──────────┴──┘ 
         ⇑
 struct node *list

Step 2. Node with value less than new node found. Link new node to current node.
There is no previous node, so there is no need to link it to the new node.

   ┌─────────┬──┐
   | "Rich"  |  |
   | "rbig"  |  ══╗
   | 3       |  | ║
   └─────────┴──┘ ║
 ╔════════════════╝
 ║   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐
 ║   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  | 
 ╚═> | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══> NULL
     | 2       |  |   | 2         |  |   | 0        |  |
     └─────────┴──┘   └───────────┴──┘   └──────────┴──┘ 
           ⇑
   struct node *list

Step 5. Insertion is successful. Update list variable to point to new head.

   ┌─────────┬──┐   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐
   | "Rich"  |  |   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  | 
   | "rbig"  |  ══> | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══> NULL
   | 3       |  |   | 2       |  |   | 2         |  |   | 0        |  |
   └─────────┴──┘   └─────────┴──┘   └───────────┴──┘   └──────────┴──┘ 
         ⇑
         ╚═════════════════╗
                   struct node *list
```

- Insertion at the end of the list requires traversal to the end of the list, before the tail element is linked to the new node
    - Thew new node becomes the last element, so it becomes the new tail

```txt
List elements: [Mike, Barry, Steve]

Element to be inserted
   ┌─────────┬──┐
   | "Anita" |  |
   | "abath" |  ══> NULL
   | 0       |  |
   └─────────┴──┘

Step 0. Original list

   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐
   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  | 
   | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══> NULL
   | 2       |  |   | 2         |  |   | 0        |  |
   └─────────┴──┘   └───────────┴──┘   └──────────┴──┘ 
         ⇑
 struct node *list

Step 1. Compare the new node to the first node.
If the current is greater than/equal to the new one, insert new node before that one.
Otherwise, continue.

   ┌─────────┬──┐
   | "Anita" |  |
   | "abath" |  ══> NULL
   | 0       |  |
   └─────────┴──┘
         ↕
   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐
   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  | 
   | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══> NULL
   | 2       |  |   | 2         |  |   | 0        |  |
   └─────────┴──┘   └───────────┴──┘   └──────────┴──┘ 
         ⇑
 struct node *list

Step 2. Compare the new node to the first node.
If the current is greater than/equal to the new one, insert new node before that one.
Otherwise, continue.

                    ┌─────────┬──┐
                    | "Anita" |  |
                    | "abath" |  ══> NULL
                    | 0       |  |
                    └─────────┴──┘
                          ↕
   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐
   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  | 
   | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══> NULL
   | 2       |  |   | 2         |  |   | 0        |  |
   └─────────┴──┘   └───────────┴──┘   └──────────┴──┘ 
         ⇑
 struct node *list

Step 3. Compare the new node to the first node.
If the current is greater than/equal to the new one, insert new node before that one.
Otherwise, continue.

                                       ┌─────────┬──┐
                                       | "Anita" |  |
                                       | "abath" |  ══> NULL
                                       | 0       |  |
                                       └─────────┴──┘
                                             ↕
   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐
   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  | 
   | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══> NULL
   | 2       |  |   | 2         |  |   | 0        |  |
   └─────────┴──┘   └───────────┴──┘   └──────────┴──┘ 
         ⇑
 struct node *list

Step 4. There is no next node. Link tail element to new node.

                                       ┌─────────┬──┐
                                       | "Anita" |  |
                                   ╔═> | "abath" |  ══> NULL
                                   ║   | 0       |  |
                                   ║   └─────────┴──┘
                                   ╚═══════════════════╗
   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐ ║
   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  | ║
   | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══╝
   | 2       |  |   | 2         |  |   | 0        |  |
   └─────────┴──┘   └───────────┴──┘   └──────────┴──┘ 
         ⇑
 struct node *list

Step 5. Iteration is successful.
List variable does not need to be updated since head remains the same.

   ┌─────────┬──┐   ┌───────────┬──┐   ┌──────────┬──┐   ┌──────────┬──┐
   | "Mike"  |  |   | "Barry"   |  |   | "Steve"  |  |   | "Anita"  |  | 
   | "mhawk" |  ══> | "bockner" |  ══> | "ssmith" |  ══> | "abath"  |  ══> NULL
   | 2       |  |   | 2         |  |   | 0        |  |   | 0        |  |
   └─────────┴──┘   └───────────┴──┘   └──────────┴──┘   └──────────┴──┘
         ⇑
 struct node *list ✓
```

### ***v.* Deletion**

- For the first node that satisfies some condition, remove it from the list
    - Requires `free`ing of the node being deleted
- Condition can be whether the node is the head or tail, ensuring that either is always deleted
    - Useful for implementing stacks, queues
- Traverse the list, checking each node for agreement with the condition, similar to with insertion

```c
// List elements: [Mike, Barry, Steve]
// Delete element with attempts == attempt_query

int attempt_query;

// ...

if (list == NULL) { // List is empty
    return NULL;
}

current_node = head;
struct node *previous = NULL;
while (current_node->attempts != attempt_query) {
    if (current_node->next == NULL) {
        // At this point, current node is tail AND does not agree with condition
        // No elements satisfy the condition
        return head;    // Return old head
    }
    previous = current_node;    // On next iteration, this element will be the previous one
    current_node = current_node->next;  // Move to next element
}
if (previous == NULL) {
    // At this point, (first node)->attempts == attempt_query
    // Designate next node as head
    struct node *head = current_node->next;
    free(current_node);
    return head;    // Return new head
}
previous->next = current_node->next;   // Link previous to next node
free(current_node);
return head;    // Return old head
```

- The above algorithm can be modified to delete the last node that agrees with the condition
    - Assumes list is sorted

```c
current_node = head;
struct node *previous = NULL;
for (;;) {  // Loop until broken out of. Could also be replaced with 'while (1)'
    if (current_node->next == NULL) {
        return head;
    }
    if (current_node->attempts == attempt_query && current_node->next->attempts != attempt_query) {
        break;  // We've found the last node in agreement
    }
    previous = current_node;
    current_node = current_node->next;
}
if (previous == NULL) {
    struct node *head = current_node->next;
    free(current_node);
    return head;
}
previous->next = current_node->next;
free(current_node);
return head;
```

- If the head satisfies the condition
    1. Update the list variable to point to the next element, or `NULL` if that was the only node
    2. `free` the old head element
- If only the tail satisfies the condition
    1. Update the node previous to the tail to point to `NULL`
    2. `free` the old tail element

## 7. Doubly-Linked Lists

- *Doubly-linked*, every node holds a pointer to its next and previous element
    - For the first element, the previous element is `NULL`

```txt
               Element 0                   Element 1                   Element 2
       ┌──────┬─────────┬──────┐   ┌──────┬─────────┬──────┐   ┌──────┬─────────┬──────┐
       | prev | members | next ══> | prev | members | next ══> | prev | members | next ══> NULL
NULL <══      |         |      │ <══      |         |      │ <══      |         |      │
       └──────┴─────────┴──────┘   └──────┴─────────┴──────┘   └──────┴─────────┴──────┘
                   ⇑
               node *list
```

- Typical layout of a doubly-linked node is below

```c
struct node {
    // member variables here
    struct node *prev;  // Previous node in list, or NULL if this is the first element
    struct node *next;  // Next node in list or NULL
}
```

- Operations on doubly-linked lists is the same as singly-linked, except `prev` must be updated on insertion/deletion
    - Wherever `next` is reassigned, the node being pointed to by `next` must have its `prev` point to the node holding that `next`

## 9. Function Pointers

- In an executable, functions have a defined memory address just like variables
    - In assembly, a call to a function is a jump a label of that same name

```c
void fun() {
    return;
}

int main() {
    fun();
    return 0;
}
```

```assembly
fun:
    lw   ra, (sp)
    addi sp, sp, 4
    jr   ra             # return to 'main'

main:
    addi sp, sp, -4
    sw   ra, (sp)
    jal  fun            # Move program counter (PC) to address of 'fun'
```

- A *function pointer* resolves the address of the function in question
    - Can be obtained by using the name of the function directly
- A common use-case for function pointers is the `qsort` function, defined in the standard header file `stdlib.h`
    - Implements the **q**uick**sort** sorting algorithm

```c
void qsort(void* ptr, size_t count, size_t size, int (*comp)(const void*, const void*));
```

#### **Figure .** `qsort` Parameters
| Parameter | Description                                                                       |
|:----------|:----------------------------------------------------------------------------------|
| `ptr`     | A pointer to the array to sort                                                    |
| `count`   | The number of elements in the array                                               |
| `size`    | The size of each element in the array, in bytes (derived using `sizeof`)          |
| `comp`    | A pointer to a function returning `int` and taking two `const void *` arguments   |

- The `comp` function, whose pointer is used
    - Must not modify the values whose pointers are passed to it
    - Must return consistent results when called using the same arguments

```c
#include <stdio.h>
#include <stdlib.h>

int compare_ints(const void *a, const void *b) {
    int arg1 = *(const int *)a;
    int arg2 = *(const int *)b;
    return arg1 - arg2
}   // Function pointer is 'compare_ints'

int main(void) {
    int numbers[] = {5,2,8,1,9};
    int total_nums = sizeof(numbers) / sizeof(numbers[0]);

    qsort(numbers, total_nums, sizeof(int) /* size of each element, in bytes */, compare_ints);
    for (int i = 0; i < size; i++) {
        printf("%d ", numbers[i]);
    }   // Output: 1 2 5 8 9
    return 0;
}
```

## 10. Software Engineering Principles

- Programs can be viewed as a collection of modules
- A *module* is a collection of services, each of which provides a certain, useful functionality
    - **Ex:** a module implementing the I/O functionality defined in `stdio.h`
- Other modules in the program that depend on those services
    - Known as *clients*
    - Hold a dependency on the module providing those services
- The *interface* of a module is the public description of its services
    - *"What services can this module provide to other modules?"*
- In C, the interface of a module often consists of the function prototypes in a header file
    - `.h` files expose function prototypes, `extern` variables, and `struct` declarations to `.c` files in other modules
- The *implementation* of a module contains the code that provides the functionality of services
    - Interface refers to this code
- In C, the implementation of a module is often the `.c` files that header files refer to

```txt
┄ = "depends on"

              (Module 1)                                          (Module 2)
      [Client of system modules]                             [Client of Module 1]
  ┌────────────────────────────────────┐            ┌────────────────────────────────────┐
  |  ┌──────────────────┐    ┌──────────────────┐   |  ┌──────────────────┐    ┌──────────────────┐
  |  | (Implementation) |    |    (Interface)   |   |  | (Implementation) |    |    (Interface)   |
  |  | professors.c     | ┄> | professors.h     | <┄┄┄ | main.c           |    | int main()       |
  |  | students.c       |    | students.h       |   |  |                  |    |                  |
  |  └──────────────────┘    └──────────────────┘   |  └──────────────────┘    └──────────────────┘
  |           ┆                        |            |                                    |    ⇡
  |           ┆                        |            |                                    |    ┆
  └───────────┆────────────────────────┘            └────────────────────────────────────┘    ┆
              ⇣                                                                               ┆
       (system modules)                                                                       ┆
                                                            main ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘
       <stdio.h>    <stdlib.h>                       (binary executable)
       <stdbool.h>  <string.h>
```

- Modules, interfaces, and implementations are abstract concepts without direct counterparts in the C language
- Code *abstraction* is the creation of simple interfaces to complex program logic
    - Enables the use of an implementation without having to know how much of how it works
    - **Ex:** C itself abstracts away much of assembly
- Goals of code abstraction
    - Hiding complex details from user
    - Creating simple, high-level user interfaces
    - Facilitating software maintenance
- In this sense, software *maintenance* is the continuous improvement and debugging of software over time
- It is recommended to split programs into modules for the following reasons
    - **Abstraction:** Only the interface is visible to other modules
    - **Reusability:** Modules requiring the same services can share the same module dependency
    - **Maintainability:** Changes to one module should not affect another
- *Cohesion* refers to how closely related the components of a module are to each other
    - *"Do they serve a similar purpose?"*
- *Coupling* is the degree of interdependence between two or more modules
    - *"How important is this module to the implementation of the other?"*
- Modules in a well-designed program should be *highly cohesive* and have *low coupling*

## 12. Object Files & Linking

- Conversion from source code to executable
    1. Each `.c` source file compiled to `.s` assembly code
    2. Each `.s` file assembled into a `.o` binary object
    3. The `.o` files are combined by the linker to create a binary executable
- On Windows, object files can also be of the extension `.obj`

```txt
C source file             Assembly Code            Object Code
  ┌──────┐                  ┌──────┐                ┌──────┐
  |  .c  | → compilation →  |  .s  | →  assembly  → |  .o  |
  └──────┘                  └──────┘                └──────┘
```

- Normally, when the compiler is invoked without any arguments, all three steps are done at once
- Pass the `-c` argument to run steps 1 and 2 only
    - Useful for files not containing the `main` function

```bash
gcc -c booltest.c   # Outputs an object file with the default name 'booltest.o'
```

- Object files are not executable yet, must be passed to linker first
- The *linker* is a program that combines object files into a single binary executable
    - On Unix, the command `ld` invokes the linker
- For a given object file, if it references instructions in another object file, the linker makes sure to include those instructions
    - Header (`.h`) files provide these references, which are then resolved during linking

```txt
┄ = "depends on"
⇑ = "compiles, then assembles to"
╶ = "linked to"

           (local utility library)
                ┌────────────┐
                | students.c |
                └────────────┘
                      ⇓
                ┌────────────┐
                | students.o |╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶┐
  (system)      └────────────┘                     ╵
      ⇡               ⇡                            ╵
┌───────────┐   ┌────────────┐                     ╵
|  stdio.h  |   | students.h |                     ╵
└───────────┘   └────────────┘                     ╵
      ⇡               ⇡                            ╵
      └┄┄┄┄┄┄┄┬┄┄┄┄┄┄┄┘                            ↓
        ┌────────────┐    ┌────────────┐      ┌──────────┐
        |   main.c   | ═> |   main.o   | ╶╶╶> |   main   |
        └────────────┘    └────────────┘      └──────────┘
                                           (binary executable)
```

- When provided with multiple object files, the compiler invokes the linker

```bash
ls  # List files in current directory
>boolean.c boolean.o booltest.c booltest.o
gcc booltest.o boolean.o    # Output an executable with the default name 'a.out'
```

- The `-o` argument can be passed to the compiler to name the final executable
    - If not provided, is given a default name, usually `a.out`

```bash
gcc -o booltest booltest.o boolean.o    # Outputs an executable with the assigned name 'booltest'
ls
>booltest boolean.c boolean.o booltest.c booltest.o
```

- A file *depends* on another one if `#include`s it, or requires any `extern`al variables or functions
    - All function prototypes are `extern` by default, so if it is not defined, it is resolved during linking

```c
// main.c

void fun_1();   // 'extern' by default
extern void fun_2();    // redundant 'extern' modifier
extern int n;   // Must be made 'extern' explicitly so that a new copy is not stored in this object file

int main() {
    fun_1();
    fun_2();
    n = 3;
    return 0;
}
```

```bash
gcc -c fun.c    # Assemble source of external declarations to 'fun.o'
gcc -c main.c   # Outputs 'main.o'
gcc main.o fun.o    # Output final executable
```

- Within header files like `stdio.h`, functions like `printf` are defined as external declarations to be resolved during linking
- If the `extern` declaration cannot be found during linking, an error will be raised
    - Error will be output as `undefined symbol` or `undefined reference`
- `main` function is required of final executable
    - If missing, linking fails, typically with message `undefined reference to 'main'`
- Common reasons for linking failure include:
    - Misspelling of functions or variables
    - The library, whose interface is a header file, cannot be found/is not installed

## 12. Makefiles & Automation

- *Makefiles* are files containing sequences of commands used to build a program
    - On Unix, processed using the `make` command
- One per directory, named `Makefile` or `makefile`
- Makefiles automate the build process by
    - Deciding which parts of a program need to be recompiled
    - Recognizing file dependencies
    - Listing what commands need to be executed
- Procedures in a makefile are grouped into *rules*, each of which is in the form shown below

```txt
<target>: <file dependencies>
    <command 1>
    <command 2>
    <...>
```

- The *target* is the name of the rule, which can be run explicitly using `make <target>`
- All other lines in a rule are the *commands* to be executed
    - Only done so if one of its dependent files is changed
    - **Important:** Each command must be indented using a TAB character, *not* 4 spaces

```bash
booltest: booltest.o boolean.o  # If these two files do not change, it is unnecessary to invoke this target again
    gcc -o booltest booltest.o boolean.o    # Commands run on invocation

booltest.o: booltest.c boolean.h
    gcc -c booltest.c

boolean.o: boolean.c boolean.h
    gcc -c boolean.c
```

- To run the first target, simply run `make`
    - Order of all other rules is arbitrary
- To run a specific target, run `make <target>`

```bash
cat Makefile
>clean:
>    rm booltest booltest.o boolean.o
make clean
```