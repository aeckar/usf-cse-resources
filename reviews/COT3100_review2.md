# COT 3100 Discrete Structures - Exam 2 Review

<p style="text-align:center">
    <a href="../textbooks/COT3100_textbook.pdf">textbook</a> |
    <a href="https://quizlet.com/957758773/cot-3100-set-laws-identities-flash-cards">quizlet</a>
</p>

## 1. Set Logic & Proofs

- Sets are *mutually disjoint* if all are disjoint from all others
    - $A \cap B \cap C \cap ... \equiv \emptyset$
- A set can be *partitioned* into multiple sets:
    - That are mutually disjoint
    - Whose union is the original set

>**Example:** Some partitions of the set $\{1,2,3,4,5\}$ are:
>
>$\{\{1,2\},\{3,5\},\{4\}\}$
>
>$\{\{2\},\{1\},\{3,4,5\}\}$

- The *Cartesian product* of two sets is the set of all combinations of elements from either set
    - All elements as ordered pairs
    - Typically evaluated before other set operations

>**Example:** Perform the Cartesian product $\{1,2,3\} \times \{x,y,z\}$.
>
>```
>   1     2     3
> x (x,1) (x,2) (x,3)
> y (y,1) (y,2) (y,3)
> z (z,1) (z,2) (z,3)
>```
>
> $= \{(x,1), (x,2), \dots, (z,3)\} \checkmark$

- Set subtraction in the form $A - B$
    - "All elements in A that are not also an element in B"
- By combining identities of sets, logical statements can be created

### Common Set Identities
| Name                          | Identity                                                          |
|-------------------------------|-------------------------------------------------------------------|
|                               | $x \notin A \cup B \leftrightarrow x \notin A \land x \notin B$   |
|                               | $x \notin A \cap B \leftrightarrow x \notin A \lor x \notin B$    |
|                               | $x \notin A - B \leftrightarrow x \notin A \lor x \in B$          |
| Definition of union           | A $\cup$ B = { x \| x $\in$ A $\lor$ x $\in$ B }                  |
| Definition of intersection    | A $\cap$ B = { x \| x $\in$ A $\land$ x $\in$ B }                 |
| Definition of set difference  | A - B = { x \| x $\in$ A $\land$ x $\notin$ B }                   |

>**Example:** 
>
>
>
>
>

## 2. Relations on Sets

- For sets A and B, a *relation* from A to B is a subset, R, of A $\times$ B
such that every pair of elements satisfies some relationship ()
    - If x $\in$ A is related to y $\in$ B, expressed as x *R* y $\leftrightarrow$ (x,y) $\in$ R
    - If x is not related to y, expressed as x ~~*R*~~ y $\leftrightarrow$ (x,y) $\notin$ R
- Domain A and codomain B, or vice-versa

>**Example:** Both $\emptyset$ and all of A $\times$ B are extreme examples of relations from A to B,
>one with no relations and the other with every possible relation.

- x *R* y does not necessarily imply y *R* x
- Relationships not easily explainable, like decision by coin flip, can still be the foundation of a relation
- *Divides to* is a possible relationship that states "$x$ divides $y$ if $y$ is divisible by $x$"
    - Represented as $x | y$
- *Arrow diagram* used to represent relations

>**Example:**
>
>
>

reflexivity, - 
transitivity, -
and symmetry -

inverse relation

relation to cartesian product

equivalence relation as fulfilling reflexivity, transitivity, and symmetry

***WIP***