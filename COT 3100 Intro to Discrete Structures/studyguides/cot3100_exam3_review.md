# COT 3100 Discrete Structures - Final Exam Review

<p style="text-align:center">
    <a href="../cot3100_textbook.pdf">textbook</a>
</p>

**Notice:** This review is a stub. You can help by contributing to the repository.

<!-- Inline tEx cannot be placed within asterisks in GFM. -->
<!-- GFM requires a newline before block tEx to render correctly. -->

## 1. Applications of Modular Arithmetic

### ***i.* Introduction**

- Recall $a | b$ is the relation such that there exists some $x$ where $ax = b$
    - *"* $a$ *divides* $b$ *"*
- The statement $a \equiv b \space (mod \space n)$ is true if $a \space mod \space n = b \space mod \space n$
    - *"* $a$ *is equivalent to* $b$ *"*
- For Fall 2024, encryption will *not* be on the exam

#### **Theorem 1.** Equivalent Statements
>**Given:** $a$, $b$, and $n$ are integers<br>
>**Given:** $n > 1$
>
>The following are all equivalent (all are true, or all are false)
>1. $n | (a - b)$
>2. $a \equiv b \space (mod \space n)$
>3. $a = b + kn$ for some integer *k*
>4. *a* and *b* have the same (nonnegative) remainder when divided by *n*
>5. $a \space mod \space n = b \space mod \space n$

### ***ii.* The Caesar Cipher**

- *Plaintext* is not encrypted
    - When encrypted, becomes *ciphertext*
- *Caesar cipher* used to encrypt and decrypt text
- To convert a character to its encrypted form, $C$
    1. Convert letter to its ordinal (position in alphabet)
    2. Add 3
    3. Modulo by 26 (if *x*, *y*, or *z*, wrap around)
    4. Convert new ordinal to its letter
- To convert a character to its decrypted form, $M$
    1. Convert letter to its ordinal
    2. Subtract 3
    3. Modulo by 26
    4. Convert new ordinal to its letter

#### **Theorem 2-3.** Caesar Cipher Encryption & Decryption Algorithms
>**Given:** $C$ is ciphertext, and $M$ is plaintext<br>
>
>$$
>C = (n_M + 3) \space mod \space 26
>$$
>
>$$
>M = (n_C - 3) \space mod \space 26
>$$

#### **Figure 1.** Letter-Ordinal Mappings $(n \space mod \space 26)$
<p style="text-align:center">
    <img src="../images/COT3100_letter_ordinals.png" alt="Each letter to its ordinal">
</p>

>**Example 1.** Encrypt the message *"hello"* using the Caesar cipher
>
>h $\rightarrow$ 8,
>e $\rightarrow$ 5,
>l $\rightarrow$ 12,
>o $\rightarrow$ 15
>
>Since no letter is *x*, *y*, or *z*, we know we will not have to wrap around.
>
>Adding three, we obtain the numbers 11, 8, 15, and 18.<br>
>Converting these to letters, we get *"khoor"*. $\checkmark$

### ***iii.* The RSA Cipher**

- Two numbers are *relatively prime* when they have no other common factors but 1
    - Their greatest common divisor (GCD) is 1
- *RSA Encryption* uses a public-private key system
    - $(pq, e)$ is the public key
    - $(pq, d)$ is the private key

#### **Theorems 5-6.** RSA Encryption & Decryption Algorithms
>**Given:** $C$ is ciphertext, and $M$ is plaintext<br>
>**Given:** $p$ and $q$ are large, almost certainly prime numbers<br>
>**Given:** $e$ is a positive integer relatively prime to $(p - 1)(q - 1)$<br>
>**Given:** $d$ is a positive integer such that $de \space mod \space (p - 1)(q - 1) = 1$<br>
>
>$$
>C = M^e \space mod \space pq
>$$
>
>$$
>M = C^d \space mod \space pq
>$$

### ***iv.* The Extended Euclidean Algorithm** 

- The *Euclidean Algorithm* efsegfeskofkgsogops

## 2. Combinatorics

- The *multiplication rule* states that, when combining choices, the total number of options is the product of each number of options
    - *"If there are $n_1$ ways to do one task and $n_2$ ways to do another, ..., there are $n_1 \cdot n_2 \cdot {\dots} \cdot n_k$ ways to do both tasks."*
- If $m \leq n$, there are $n - m + 1$ integers from $m$ to $n$, inclusive
    - By dividing lists of multiples, you can derive a contiguous list whose size can be determined by the above theorem

>**Example .** What is the probability that a randomly selected 3-digit integer will be divisible by 5?
>
>Because the 3-digit integers range from [100,999], we can say $m$ is 100 and $n$ is 999.
>
>$999 - 100 + 1 = 900$ integers between 100 and 999
>
>Thereafter, we derive the multiples of 5 between 100 and 999.
>
>$100, 105, \dots, 995 \rightarrow \frac{100, 105, \dots, 995}{5} \rightarrow 20, 21, \dots, 199$
>
>Because the new list is contiguous (no integers are missing between $m$ and $n$),
>we can say $m$ is 20 and $n$ is 199, and find the number of multiples.
>
>$199 - 20 + 1 = 180$
>
>$180$ is the number of times the event occurs, and $900$ is the total number of events.
>From this, we can derive the probability.
>
>$\frac{180}{900} = \frac{1}{5} \checkmark$

- If $m \leq n$, there are $⌊\frac{n}{x}⌋ - ⌈\frac{m}{x}⌉ + 1$ integers in $[m,n]$ divisible by $x$
- By drawing a *possibility tree*, every possibility in a series of events can be found

>**Example .** Consider a tournament played in five games between teams $A$ and
>$B$, which can be won by winning two games in a row or winning three games.
>How many ways can the tournament be played?
>
>![A tree containing all possibilities](../images/COT3100_possibility_tree.png)
>
>From this, we can derive the set of possible tournaments as
>
>$\{AA, ABAA, ABABA, ABABB, ABB, BAA, BABAA, BABAB, BABB, BB\} \checkmark$

#### **Theorem .** Inclusion-Exclusion Principle
>For two overlapping sets, the cardinality of their union is given as
>
>$$
>|A \cup B| = |A| + |B| - |A \cap B|
>$$
>
>For three, mutually overlapping sets, the cardinality of their union is given as
>
>$$
>|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|
>$$

- When simplifying fractions containing factorials, it can help to reduce the factorial into a smaller one
    - **Ex:** $\frac{22!}{20! \cdot 2!} = \frac{22 \cdot 21 \cdot 20!}{20! \cdot 2!} = \frac{22 \cdot 21}{2!} = 231 \checkmark$
- The number of *combinations* describes the possible selections of $r$ items from a list of $n$ elements, without respect to order
    - *r-combination of an n-element set*
    - Pronounced *"*$n$ *choose* $r$*"*

#### **Theorem 4.** Counting Combinations
>**Given:** $n$ and $r$ are non-negative integers<br>
>**Given:** $r \leq n$
>
>$$
>C(n,r) = n \space C \space r = {n \choose r} = \frac{n!}{r!(n -  r)!}
>$$
>
>$$
>n \space C \space r = \frac{n \space P \space r}{r!}
>$$

- The number of *permutations* describes the possible selections of $r$ items from a list of $n$ elements, where order matters
    - *r-permutation of an n-element set*
- Order matters when selecting for specific roles, variables, etc.

#### **Theorem 5.** Counting Permutations
>**Given:** $n$ and $r$ are non-negative integers<br>
>**Given:** $r \leq n$
>
>$$
>P(n,r) = n \space P \space r = \frac{n!}{(n - r)!}
>$$
>
>$$
>n \space P \space r = (n \space C \space r)r!
>$$

#### **Figure .** Different Ways of Choosing $k$ Elements from $n$
|                                   | Order Matters         | Order Does *Not* Matter   |
|:----------------------------------|:---------------------:|:-------------------------:|
| **Repetition is Allowed**         | $n_k$                 | ${k + n - 1} \choose k$   |
| **Repetition is *Not* Allowed**   | $n \space P \space k$ | $n \choose k$             |

- When finding the number of solutions to a problem in the form $x_1 + x_2 + \dots + x_k = n$

## 5. Probability

### ***i.* Introduction**

- For an event *A*, $P(A)$ is the probability that $A$ occurs
    - $P(A^C)$ is the event it does not occur
- Events obey [set identities](./cot3100_exam2_review.md)
- The *sample space*, $S$, is the set of all possible events
- The *null space*, $\emptyset$, is the set of no events
- On the exam, do *not* reduce probabilities except when asked

#### **Theorem .** Axioms of Probability
>The following are assumed to be unconditionally true:
>1. $0 \leq P(A) \leq 1$
>2. $P(\emptyset) = 0$ and $P(S) = 1$
>3. If $A \cap B = \emptyset$ then $P(A \cup B) = P(A) + P(B)$

#### **Theorem .** The Probability of an Event
>**Given:** $A$ is some event
>
>$$
>P(A) = \frac{|A|}{|S|} = \frac{\text{no. of times }A\text{ occurs}}{\text{no. of total events}}
>$$

#### **Figure 2.** Basic Principles of Probabilities
| Principle                                                 |
|-----------------------------------------------------------|
| $P(A \cup B) = P(A) + P(B) - P(A \cap B)$                 |
| $P(A \cap B) = P(A) \cdot P(B\|A) = P(B) \cdot P(A\|B)$   |
| $P(A^C) = 1 - P(A)$                                       |
| If $B \subseteq A$ then $P(B\|A) = \frac{P(B)}{P(A)}$     |

>**Example 2.** Three people have been exposed to a certain illness. Once exposed, a person has a 50-50 chance of actually becoming ill.
>
> a) What is the probability that exactly one of the people becomes ill?
>
> $P(1 \space \text{ill}) = {3 \choose 1}(\frac{1}{2}^1)(\frac{1}{2}^2) = \frac{3}{8} \checkmark$
>
> b) What is the probability that at least two of the people become ill?
>
> $P(\geq 2 \space \text{ill}) = P(2) + P(3) = {3 \choose 2}(\frac{1}{2}^2)(\frac{1}{2}^1) + {3 \choose 3}(\frac{1}{2}^3)(\frac{1}{2}^0) = \frac{1}{2} \checkmark$
>
> c) What is the probability that none of the three people becomes ill?
>
> $P(0 \space \text{ill}) = {3 \choose 0}(\frac{1}{2}^0)(\frac{1}{2}^3) = \frac{1}{8} \checkmark$

#### **Figure 3.** Properties of Events
| Property              | Meaning                                       | Formulas                                                          |
|:----------------------|:----------------------------------------------|:------------------------------------------------------------------|
| Mutually exclusive    | $A$ and $B$ cannot occur at the same time     | $P(A \cup B) = P(A) + P(B)$<br>$P(A \cap B) = 0$                  |
| Overlapping           | $A$ and $B$ *can* occur at the same time      | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$<br>$P(A \cap B) > 0$    |
| Independent           | The occurrence of $A$ has no effect on $P(B)$ | $P(A \cap B) = P(A) \cdot P(B)$                                   |
| Dependent             | The occurrence of $A$ *changes* $P(B)$        | $P(A \cap B) = P(A) \cdot P(B\|A)$                                |

<small>\**These properties can also be applied to any number of events*</small>

#### **Theorem 6.** Probability of Mutually Exclusive Event
>**Given:** $A$ and $B$ are mutually exclusive events<br>
>**Given:** $N$ is the total number of elements<br>
>**Given:** $n_A$ and $n_B$ is the number of elements for which events $A$ and $B$ hold true, respectively
>
>$$
>P(n_A \cdot A) = {N \choose n_A} \cdot P(A)^{n_A} \cdot P(B)^{n_B}
>$$

### ***ii.* Conditional Probability & Bayes' Theorem**

- $P(A|B)$ is the probability that $A$ occurs, given $B$ occurs
    - *"The conditional probability of* $B$ *given* $A$ *"*
    - $B$ is the *restricted sample space*

#### **Theorem .** Conditional Probability
>**Given:** $P(B) \neq 0$
>
>$$
>P(B|A) = \frac{P(B \cap A)}{P(A)}
>$$

#### **Theorem 7.** Bayes' Theorem
>$$
>P(B|A) = \frac{P(A|B) \cdot P(B)}{P(A)}
>$$

#### **Theorem .** Formula for Binomial Probability
>**Given:** $n$ is the number of trials, and $k$ is the number of successes<br>
>**Given:** $p$ is the probability of success for a single trial
>
>$$
>P(X = k) = {n \choose k} p^k (1 - p)^{n - k}
>$$

- Ensure that when performing multiple trials, you account for any decrease in population size
    - **Ex:** A ball is picked at random without replacement

#### **Theorem .** Law of Total Probability
>**Given:** $A$ is some event<br>
>**Given:**  
>
>$$
>P(A) = P(A|B_1) P(B_1) + P(A|B_2)P(B_2) + \dots + P(A|B_k)P(B_k)
>$$