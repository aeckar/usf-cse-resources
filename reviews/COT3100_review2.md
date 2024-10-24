# COT 3100 Discrete Structures - Exam 2 Review

<p style="text-align:center">
    <a href="../textbooks/COT3100_textbook.pdf">textbook</a> |
    <a href="https://quizlet.com/957758773/cot-3100-set-laws-identities-flash-cards">quizlet</a>
</p>

## 1. Set Logic

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

- By combining identities of sets, logical statements can be created

| Common Identities     \\\\TODO move                                            |
|-------------------------------------------------------------------|
| $x \notin A \cup B \leftrightarrow x \notin A \land x \notin B$   |
| $x \notin A \cap B \leftrightarrow x \notin A \lor x \notin B$    |
| $x \notin A - B \leftrightarrow x \notin A \lor x \in B$          |

### Common Identities
| Name                          | Identity  |
|-------------------------------|-----------|
| Definition of union           |           |
| Definition of intersection    |           |
| Definition of exclusion       |           |

- The *Cartesian product* of two sets is the set of all combinations of elements from either set
    - All elements as ordered pairs

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

