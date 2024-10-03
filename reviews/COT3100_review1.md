# COT 3100 Discrete Structures - Exam 1 Review

<ins>Textbook</ins>: *Discrete Mathematics with Applications (5th ed.)* by Susanna Epp

### Logic Symbols and their Meanings
| Symbol        | Pronunciation         |
|---------------|-----------------------|
| T             | *true*                |
| F             | *false*               |
| $\therefore$  | *therefore*           |
| $\in$         | *in*                  |
| $\supseteq$   | *is a superset of*    |
| $\subseteq$   | *is a subset of*      |
| \|            | *such that*           |
| $\forall$     | *for all*             |
| $\exists$     | *there exists a*      |

## 1. Set Theory

- A *set* is some collection collection of elements
    - Can contain other sets
    - Typically denoted by a capital letter

>**Example:** Sets cannot be created from ambiguous conditions.
>
> A set of "good" students cannot exist because *good* is a subjective measure.

- Infinite sets can be denoted using ellipses ($\ldots$)
- $\empty$ is the empty (null) set, containing no elements
- **U** is the universal set, containing all possible elements
- *Subsets* are sets whose elements can all be found within another set
    - Other set is a *superset*
    - A set is always a sub- and superset of itself
- Denoting a set with duplicate entries is legal
    - Can be reduced to the same notation with unique elements

### Common Sets of Numbers
| Symbol    | Elements              | Examples                                                  |
|-----------|-----------------------|-----------------------------------------------------------|
| C         | complex numbers       | 2 + 7i                                                    |
| $\R$      | real numbers          | $\pi$, 16                                                 |
| $\Z$      | integers              | -3, 0, 24                                                 |
| Q         | rational numbers      | 0.25, 9                                                   |
| $^+, ^-$  | positives, negatives  | $R^+ = (0, \infty)$ is set of all positive real numbers   |

- $C \supseteq \R \supseteq W \supseteq \Z$
- Sets denoted in either
    - **Roster notation:** $\{ e_1,e_2,e_3, \ldots , e_n \}$
    - **Set builder notation:** $\{ var \space type? | condition \}$
        - **Ex:** $\{ x \in \Z | x \lt 7 \} = \{ \ldots ,4,5,6 \}$

## 2. Statements, Forms, and Deductive Reasoning

- A *statement* (proposition) is something that can be given a truth value
    - Can be given variable values, typically denoted *p* and *q*
- *Domain* is set of all possible statement variables

>**Example:** Self-referential sentences cannot be given a truth value, so they can never be statements.
>
>"This sentence is true" is not a statement by this logic.

### Types of statements
| Type          | Claim                                     | Example                                                   |
|---------------|-------------------------------------------|-----------------------------------------------------------|
| universal     | property is true for every element        | *Every person in this class is a USF student*             |
| existential   | property is true for at least one element | *Some person in this class is not a USF student*          |
| conditional   | consequent is true if antecedent is true  | *If a person is in this class, they are a USF student*    |

### Statement Vocabulary
| Term                      | Definition                                                                                    | Example                                       |
|---------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| tautology                 | A statement that is always true regardless of statement variables                             | p $\lor$ ~p                                   |
| contradiction             | A statement that is always false regardless of statement variables                            | p $\land$ ~p                                  |
| condition (antecedent)    | A statement variable that if true, the hypothesis must also be true                           | p $\rightarrow$ q, where p is the condition   |
| hypothesis (consequent)   | An event that may happen if its condition is false, but must happen if its condition is true  | p $\rightarrow$ q, where q is the hypothesis  |

- Two statements are *logically equivalent* ($\equiv$) if they always produce same truth value, given same inputs
- Neither-or implies conjunction of complements

### Logical Operators
| Notation              | Alternate Notation    | Name          | Pronunciations                | Condition for Truth                               | Common Equivalences                               |
|-----------------------|-----------------------|---------------|-------------------------------|---------------------------------------------------|---------------------------------------------------|
| ~p                    | $\neg$                | negation      | *not p*                       | p is false                                        |                                                   |
| p $\land$ q           | &                     | conjunction   | *p and q*, *p but q*          | Both p and q are true                             |                                                   |
| p $\lor$ q            |                       | disjunction   | *p or q*, *p unless q*        | p or q are true                                   | q $\rightarrow$ p, p $\rightarrow$ q              |
| p $\rightarrow$ q     | $\implies$            | conditional   | *if p, then q*, *p implies q* | Always true, unless p is true and q is false      | ~p $\lor$ q                                       |
| p $\leftrightarrow$ q | $\iff$                | biconditional | *p, if and only if, q*        | Both p and q are true, or both p and q are false  | (p $\rightarrow$ q) $\land$ (q $\rightarrow$ p)   |

### Transformations of $p \rightarrow q$
| Name              | Form                  |
|-------------------|-----------------------|
| Negation          | p $\land$ ~q          |
| Contrapositive    | ~q $\rightarrow$ ~p   |
| Converse          | q $\rightarrow$ p     |
| Inverse           | ~p $\rightarrow$ ~q   |

## 3. Inductive Reasoning

######################

TODO

######################

Valid/invalid argument form
Formal argument form
An argument form is valid iff whenever statements are substituted that make all premises true, the conclusion is also true

Modus ponens
Modus tollens
etc.

Premise 1
Premise 2…
Therefore conclusion

For every singular statement variable, include in permutation for truth table

If logical equivalent, the biconditional is true
Premises -> to the left of “therefore”
Conclusions -> to the right of “therefore”

Generalization
specialization
inverse error
converse error
proof by division into cases
deduction
de morgans laws

vacuous truth ("truth by default")

