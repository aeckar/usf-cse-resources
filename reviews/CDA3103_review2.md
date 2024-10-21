# CDA 3103 Computer Organization & Architecture - Exam 2 Review

<p style="text-align:center">
    <a href="../textbooks/CDA3103_textbook.pdf">textbook</a> |
    <a href="https://quizlet.com/845007313/cda-3103-exam-2-risc-v-logic-gate-circuits-flash-cards">quizlet</a>
</p>

### SI Unit Prefixes 
| Prefix    | Symbol    | Value         |
|-----------|-----------|---------------|
| femto-    | f         | $10^{-15}$    |
| pico-     | p         | $10^{-12}$    |
| nano-     | n         | $10^{-9}$     |
| micro-    | $\mu$     | $10^{-6}$     |
| milli-    | m         | $10^{-3}$     |
| kilo-     | k         | $10^3$        | 
| mega-     | M         | $10^6$        |
| giga-     | G         | $10^9$        |
| tera-     | T         | $10^{12}$     |
| peta-     | P         | $10^{15}$     |

## 1. Logic Gates and Multiplexers

- Boolean expressions can be represented as a diagram of *logic gates*
    - Composed of transistors

### Common Logic Gates
||||
|-|-|
| NOT |
| AND |||
| OR |
| 

## 2. Combinational Circuits

- Pro

## 3. Sequential Circuits

These are circuits that hold and use data (typically 1 bit) from their previous inputs to produce their next outputs.

There are multiple types, but all of them are going to be either synchronous or asynchronous. 
- **Synchronous circuits** respond to inputs only when the clock is in a rising state (going from 0 to 1). Most sequential circuits are synchronous.
- **Asynchronous circuits** respond to inputs all the time (they don't have a clock).

### Sequential Circuit Types

#### **Set-Reset Latch**

- Holds one bit of data. It is also the smallest circuit capable doing this.
- Is asynchronous. It doesn't have a clock.
- Can have an undefined state (its data is invalid).

**Circuit:**  

<img src="../images/CDA3103_sr_latch.png" alt="Set-Reset Latch" width="25%">  

**Truth table:**
| S (Set) | R (Reset) | Qt | Q(t+1) |
|:-------:|:---------:|:-----------------:|:-------------------:|
|   0     |     0     |         0         |          0          |
|   0     |     0     |         1         |          1          |
|   0     |     1     |         0         |          0          |
|   0     |     1     |         1         |          0          |
|   1     |     0     |         0         |          1          |
|   1     |     0     |         1         |          1          |
|   1     |     1     |         X         |        Invalid       |


#### Set-Reset Flip-Flop

#### D Flip-Flop

#### JK Flip-Flop









***UP-TO-DATE***