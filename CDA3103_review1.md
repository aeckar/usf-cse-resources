# CDA 3103 Computer Organization & Architecture - Exam 1 Review

### 1. Positional Number Systems

| Number System | Base (Radix)  | Digits    | Bits per digit            | Literal Form      | C literal |
|---------------|---------------|-----------|---------------------------|-------------------|-----------|
| Binary        | 2             | 0, 1      | 1                         | N<sub>2</sub>     | 0bN       |
| Octal         | 8             | 0-7       | 3                         | N<sub>8</sub>     | 0oN       |
| Decimal       | 10            | 0-9       | <small>*varies*</small>   | N<sub>10</sub>    | N         |
| Hexadecimal   | 16            | 0-9, A-F  | 4                         | N<sub>16</sub>    | 0xN       |

- Digits A-F in hexadecimal
    - Corresponding to values 10-15
    - Also representable as a-f
- Numbers in these systems represents as a sum of products
    - Each digit multiplied by its positional value

>**Example:** Convert $147.A_{16}$ to decimal.
>
>| Position  | 2                | 1                 | 0                 | -1                    |
>|-----------|------------------|-------------------|-------------------|-----------------------|
>| Digit     | 1                | 4                 | 7                 | A                     |
>| Product   | $1 \bullet 16^2$ | $4 \bullet 16^1$  | $7 \bullet 16^0$  | $10 \bullet 16^{-1}$  |
>
>$16^2 + (4 \bullet 16) + 7 + \frac{10}{16} = 327.625_{10} \checkmark$

### 2. Binary Representation of Numbers

- *Binary* is the representation of numbers in base-2
    - Also represent closed and open or on and off, respectively
    - Binary digits, a.k.a. *"bits"*
- *Most-significant bit* (MSB) is leftmost bit
- *Least-significant bit* (LSB) is rightmost bit
- Computers represent binary in three ways:

| Name           | Representation of Negatives  |
|----------------|------------------------------|
| Sign-Magnitude | MSB is `1`                   |
| 1's Complement | Flip all bits                |
| 2's Complement | Flip all bits, add 1         |

- Positive numbers are the same between representations
- Conversions from decimal to binary:
    1. Convert absolute value of number to binary (see below)
    2. If negative, perform the action specific to the representation

>**Example:** Convert $137_{10}$ to binary, padded to 16 bits.
>
>Closest powers of 2 are 128, 64, 32, 16, 8, 4, 2, 1 
>```c
>⌊137 / 128⌋ = 1 // Since 128 = 2^7, bit at position 7 is 1
>137 - 128 = 9 
>⌊9 / 8⌋ = 1     // Divide by next smallest power of 2; Since 8 = 2^3, bit at position 3 is 1
>9 - 8 = 1
>⌊1 / 1⌋ = 1     // Divide by next smallest power of 2; Since 1 = 2^0, bit at position 0 is 1
>```
>
>| Position  | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
>|-----------|---|---|---|---|---|---|---|---|
>| Digit     | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
> 
>$137_{10} = 10001001_2 = 0000000010001001_2 \checkmark$

- Overflow is when final carry is 1
    - May cause numbers to "wrap around" to a different sign
- Addition without overflow is the same between representations
    - Going from right-to-left, add each bit according to the table below

| # of 1's  | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| Result    | 0 | 1 | 0 | 1 |
| Carry     | 0 | 0 | 1 | 1 |

- Subtraction is the same, except second number is negated according to representation
- For sign-magnitude results, you just have to know the result and resulting sign
- For 1's complement, overflow is added to number at position 0
- For 2's complement, overflow is disregarded

>**Example:** Subtract $23_{10}$ from $-13_{10}$ using 1's complement.
>
>$-13_{10} = -(00001101_2) = 11110010_2$
>
>$-(23_{10}) = -(00010111_2) = 11101000_2$
>```c
>  111 
>   11110010
> - 11101000
>-----------
>   11011010 \\ Adding overflow of 1, we get 11011011
>```
>$11011011_2 = -(00100100_2) = -36_{10} \checkmark$

### 3. Boolean Algebra

- In computers, bits `1` and `0` are stand-ins for *true* and *false*, respectively
- *Elementary operations* are product, sum, and complement
    - Combine to create Boolean (logical) expressions
- Existence of both AND and OR forms for each identity is *Duality Principle*

#### Common Boolean Operations
| Operation         | Shorthand | Notation          | C Equivalent  | Meaning                   |
|-------------------|-----------|-------------------|---------------|---------------------------|
| Boolean Product   | AND       | x $\bullet$ y, xy | `x && y`      | x *and* y                 |
| Boolean Sum       | OR        | x + y             | `x \|\| y`    | x *or* y                  |
| Complement        | NOT       | x', $\bar{x}$     | `~x`          | *not* x                   |
| Exclusive OR      | XOR       | x $\oplus$ y      | `x ^ y`       | x *or* y, *but not both*  |

#### Boolean Identities
| Name                  | AND (CPOS) Form           | OR (CSOP) Form            |
|-----------------------|---------------------------|---------------------------|
| Identity Law          | 1x = x                    | 0 + x = x                 |
| Null (Dominance) Law  | 0x = 0                    | 1 + x = 1                 |
| Idempotent Law        | xx = x                    | x + x = x                 |
| Inverse Law           | xx' = 0                   | x + x' = 1                |
| Commutative Law       | xy = yx                   | x + y = y + x             |
| Associative Law       | (xy)z = x(yz)             | (x + y) + z = xy + xz     |
| Distributive Law      | x + (yz) = (x + y)(x + z) | x(y + z) = xy + xz        |
| Absorption Law        | x(x + y) = x              | x + xy = x                |
| DeMorgan's Law        | (xy)' = x' + y'           | (x + y)' = x'y'           |
| Double Complement Law | x'' = x                   | <small>*same*</small>     |

#### Other Boolean Properties
| Name              | Property                  |
|-------------------|---------------------------|
| Mutual Exclusion  | x + x'y = x + y           |
| Consensus         | xy + y'z + xz = xy + y'z  |
| Definition of XOR | x $\oplus$ y = x'y + xy'  |

- Mutual exclusion is another form of the Absorption Law
- *Boolean functions* accept Boolean variables (conditions) and produce a new condition
    - Rely on the Boolean expressions they are defined as
- *Truth tables* present every possible combination of Boolean variables (x, y, z, ...)
    - Number of possible combinations (rows) equal to $2^n$, where $n$ is number of variables
    - It helps to list the combinations as they are below, as they translate well to K-maps

>**Example:** Create a truth table for $F(x,y,z) = xy' + z(x' + y)$
>
>| x | y | z | F |
>|---|---|---|---|
>| 0 | 0 | 0 | 0 |
>| 0 | 0 | 1 | 1 |
>| 0 | 1 | 0 | 0 |
>| 0 | 1 | 1 | 1 |
>| 1 | 0 | 0 | 1 |
>| 1 | 0 | 1 | 1 |
>| 1 | 1 | 0 | 0 |
>| 1 | 1 | 1 | 1 |

### 4. Simplifying Boolean Expressions

- *Sum-of-Product* (SOP) is form $wx + yz$
    - A.k.a. *"1-dominant"*; if any term is `1`, the expression equals `1`
    - Generally easier to work with
- *Product-of-Sum* (POS) if form $(w + x)(y + z)$
    - A.k.a. *"0-dominant"*; if any term is `0`, the expression equals `0`

>**Example:** Convert $xy' + z$ to canonical sum-of-products (CSOP) form.
>
>```c
>xy' + z =
>xy'(z + z') + z(x + x')(y + y') =          // Inverse Law 
>xy'z + xy'z' + xyz + x'yz + xy'z + x'y'z = // Distributive Law
>xy'z + xy'z' + xyz + x'yz + x'y'z          // Idempotent Law
>```

- The form of an expression is *canonical* when it is in simplest form and every term contains all variables
    - Each product, when simplified, is a term
- *Karnaugh maps* (K-maps) can be used to simplify expressions intuitively
    - Products can be formed from groups of bits of size $2^n, n \in \Z$
    - It might be helpful to create a truth table first and then convert it to a K-map
- By using identities, K-maps, or truth tables, Boolean expressions can be converted to their simplest form
    - Each row in a truth table corresponds to a term
    - Use to easily convert function to CSOP

>**Example:** Use Boolean identities to simplify $F(x,y,z) = (x' + y + z')' + xy'z' + yz + xyz$.
>
>| F(x,y,z) | = (x' + y + z')' + xy'z' + yz + xyz   |                   |
>|----------|---------------------------------------|-------------------|
>|          | = xy'z + xy'z' + yz + xyz             | DeMorgan's Law    |
>|          | = xy'z + xy'z' + yz                   | Absorption Law    |
>|          | = xy'(z + z') + yz                    | Distributive Law  |
>|          | = xy' + yz $\checkmark$               | Inverse Law       |

>**Example:** Use a K-map to simplify $F(x,y,z) = y(x'z + xz) + x'yz' + xy'z$.
>
>| x \ yz   | 0 0   | 0 1                           | 1 0                           | 1 1                           |
>|----------|-------|-------------------------------|-------------------------------|-------------------------------|
>| **0**    | 0     | 0                             | <font color="pink">1</font>   | <font color="pink">1</font>   |
>| **1**    | 0     | <font color="cyan">1</font>   |  0                            | <font color="cyan">1</font>   |
>
>Combining the groups into sizes of $2^n$, we see that in the pink group, y and x are the same in both cases,
>which allows us to transform it into the minterm x'y.
>
>When we do the same for the cyan group, we get xz.
>
>From this, we can assert that the function is x'y + xz $\checkmark$

- SOP's can be represented by their minterms
    - Represented as elements in $\sum{m}(...)$
    - Every row in truth table where *F* is `1`, as a product; for each variable, if it is `1`, complement it
- POS's can be represented by their maxterms
    - Represented as elements in $\prod{M}(...)$
    - Every row in truth table where *F* is `0`, as a sum; for each variable, if it is `0`, complement it
- Elements of formal representations of the above represented as decimal integers
    - Converted from binary to base-10

>**Example:** List the minterms and maxterms of the function represented by the truth table.
>
>| x | y | F |
>|---|---|---|
>| 0 | 0 | 0 |
>| 0 | 1 | 1 |
>| 1 | 0 | 1 |
>| 1 | 1 | 1 |
>
>Minterms are $\sum{m}(1,2,3)$ (from 01, 10, 11), or x'y + xy' + xy
>
>Maxterms are $\prod{M}(0)$ (from 00), or x + y