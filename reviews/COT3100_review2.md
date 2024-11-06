# COT 3100 Discrete Structures - Exam 2 Review

<p style="text-align:center">
    <a href="../textbooks/COT3100_textbook.pdf">textbook</a> |
    <a href="https://quizlet.com/957758773/cot-3100-set-laws-identities-flash-cards">quizlet</a>
</p>

## 1. Set Logic

- The following can be used in place of identities in formal logic
    - "By definition of ..."
### Set Operators & Constants
| Form                  | Name                  | Set-Builder Notation                                                              |
|-----------------------|-----------------------|-----------------------------------------------------------------------------------|
| A $\cup$ B            | union                 | { x \| x $\in$ A $\lor$ x $\in$ B }                                               |
| A $\cap$ B            | intersection          | { x \| x $\in$ A $\land$ x $\in$ B }                                              |
| A - B                 | difference            | { x \| x $\in$ A $\land$ x $\notin$ B }                                           |
| A $\times$ B          | cartesian product     | { (x,y) \| x $\in$ A, y $\in$ B }                                                 |
| A $\Delta$ B          | symmetric difference  | { x \| (x $\in$ A $\land$ x $\notin$ B) $\lor$ (x $\in$ B $\land$ x $\notin$ A) } |
| $\emptyset$           | empty set             | { x \| *false* }                                                                  |
| $\textbf{\textbf{U}}$ | universal set         | { x \| *true* }                                                                   |

- Recall order-of-operations for sets is undefined
- Cartesian product can be found using a table

>**Example:** Perform the Cartesian product $\{1,2,3\} \times \{x,y,z\}$.
>
>| *y* \ *x*    | 1     | 2     | 3     |
>|:------------:|:-----:|:-----:|:-----:|
>| x            | (x,1) | (x,2) | (x,3) |
>| y            | (y,1) | (y,2) | (y,3) |
>| z            | (z,1) | (z,2) | (z,3) |
>
> $= \{(x,1), (x,2), \dots, (z,3)\} \checkmark$

### Set Identities
| Name                  | Intersection Form                                         | Union Form                                                         |
|-----------------------|-----------------------------------------------------------|--------------------------------------------------------------------|
| Identity Law          | A $\cap$ $\textbf{U}$ = A                                 | A $\cup$ $\emptyset$ = A                                           |
| Universal Bound Law   | A $\cap$ $\emptyset$ = $\emptyset$                        | A $\cup$ $\textbf{U}$ = $\textbf{U}$                               |
| Idempotent Law        | A $\cap$ A = A                                            | A $\cup$ A = A                                                     |
| Inverse Law           | A $\cap A^C$ = $\emptyset$                                | A $\cup A^C$ = $\textbf{U}$                                        |
| Commutative Law       | A $\cap$ B = B $\cap$ A                                   | A $\cup$ B = B $\cup$ A                                            |
| Associative Law       | (A $\cap$ B) $\cap$ C = A $\cap$ (B $\cap$ C)             | (A $\cup$ B) $\cup$ C = A $\cup$ (B $\cup$ C)                      |
| Distributive Law      | A $\cup$ (B $\cap$ C) = (A $\cup$ B) $\cap$ (A $\cup$ C)  | A $\cap$ (B $\cup$ C) = (A $\cap$ B) $\cup$ (A $\cap$ C)           |
| Absorption Law        | A $\cap$ (A $\cup$ B) = A                                 | A $\cup$ (A $\cap$ B) = A                                          |
| De Morgan's Law       | $(A \cap B)^C$ = $A^C$ $\cup$ $B^C$                       | $(A \cup B)^C$ = $A^C \cap B^C$                                    |

| Name                          | Form                                  |
|-------------------------------|---------------------------------------|
| Double Complement Law         | $(A^C)^C$ = C                         |
| Set Difference Law            | A - B = A $\cup$ $B^C$                |
| Symmetric Difference Law      | A $\Delta$ B = (A - B) $\cup$ (B - A) |
| Reflexive Law                 | A $\subseteq$ A                       |

- To double-check identities, draw a Venn diagram inside of the universal set, $\textbf{U}$

>**Example:** Prove TODO by drawing a Venn diagram.
>
>

- Sets are *mutually disjoint* if all are disjoint from all others
    - $A \cap B \cap C \cap ... \equiv \emptyset$
- A set can be *partitioned* into multiple sets:
    - That are mutually disjoint
    - Whose union is the original set

>**Example:** List two possible partitions of $\{1,2,3,4,5\}$.
>
>$\{\{1,2\},\{3,5\},\{4\}\}$<br>
>$\{\{2\},\{1\},\{3,4,5\}\} \checkmark$ 

- Power set P(x) is set of all subsets of x
Power set of empty set is set containing only empty set
| p(A) | = 2^n where n = |A|

>**Example:** Derive the power set of { TODO }.
>
>

### Common Set Identities
| Name                          | Identity                                                          | Alternate Form                                                    |
|-------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Definition of union           | A $\cup$ B = { x \| x $\in$ A $\lor$ x $\in$ B }                  | $x \in A \cup B \leftrightarrow x \in A \lor x \in B$             |
| Definition of intersection    | A $\cap$ B = { x \| x $\in$ A $\land$ x $\in$ B }                 | $x \in A \cap B \leftrightarrow x \in A \land x \in B$            |
| Definition of set difference  | A - B = { x \| x $\in$ A $\land$ x $\notin$ B }                   | $x \in A - B \leftrightarrow x \in A \land x \notin B$            |
| Definition of set equality    | $A = B \leftrightarrow A \subseteq B \land B \subseteq A$         |                                                                   |

## 2. Relations on Sets
- A *relation* is a subset of the cartesian product of two sets
    - Each pair of elements satisfies some condition (if true, a *relationship*)
    - First set is domain, second is codomain
- For some relation *R*
    - If x $\in$ A is related to y $\in$ B, expressed as x *R* y $\leftrightarrow$ (x,y) $\in$ R
    - If x is not related to y, expressed as x ~~*R*~~ y $\leftrightarrow$ (x,y) $\notin$ R
    - x *R* y does not necessarily imply y *R* x
- Relation from A to A itself is relation *on* A
    - **Ex:** The operator $<$ is a relation on $\R$, a subset of $\R \times \R = \R^2$
- *Divides to* is a possible relationship that states "$x$ divides $y$ if $y$ is divisible by $x$"
    - Represented as $x | y$ or $\frac{x}{y} \in \Z$

### Properties of Relations
| Property              | Definition                            |
|-----------------------|---------------------------------------|
| symmetric             |
| reflexive             | 
| transitive            |
| equivalence           | symmetric, reflexive, and transitive  |
| inverse ($R^{-1}$)    |

## 3. Graphical Representations of Relations
- *Arrow diagram* used to represent relations

>**Example:** Draw the arrow diagram of the relation TODO
>
>
>

- For every element in a relation, (*x*, *y*), a *directed graph* diagrams the relationship of each unique *x* to a unique *y*
    - Each domain me

>**Example:** Draw the directed graph of the relation TODO
>