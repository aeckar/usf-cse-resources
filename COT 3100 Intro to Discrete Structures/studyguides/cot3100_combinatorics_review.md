|                        | Order Matters                            | Order Doesn't matter       |
|------------------------|------------------------------------------|----------------------------|
| Repetition Allowed     | Exponentiation <br> Permutations w/repetition | Combinations w/ Repetition |
| Repetition not <br> allowed | Permutations                             | Combinations               |


## Exponentiation | | Permutations w/ Repetition Allowed
##### Formula:  $n^r$
- where "r" represents the number of objects you are selecting and arranging from a set of "n" objects

##### Example: How many 3-digit numbers greater than 500 can be formed using 3, 4, 5, and 7?
- Since a three-digit number greater than 500 will have either 5 or 7 at its hundredth place, we have 2 choices for this place.
- There is no restriction on repetition of the digits, hence for the remaining 2 digits we have 4 choices each
- So, the ***total permutations*** are $2*4*4=32$


## Permutations
- Order Matters and Repetition is not allowed
##### Formula: $_nP_r = \frac{n!}{(n-r)!} $
- where "n" is the ***Total*** number of objects, "r" is the number objects chosen at once
- $0\le r \le n$

##### Example: How many 3-digit numbers divisible by 3 can be formed using digits 2, 4, 6, and 8 without repetition?
- For a number to be divisible by 3, the sum of its digits must be divisible by 3
- From the given set, various arrangements like 444 can be formed but since repetition isn't allowed we won't be considering them.
- We are left with just 2 cases i.e. 2, 4, 6 and 4, 6, 8
- Number of arrangements are 3! in each case
- Hence the total number of permutations are: $3! + 3! = 12$

## Combinations with Repetition
- Order in which elements are selected is not important, counting the total number of ways in which we can select some elements from a given set of elements.
- ***Stars and Bars*** is a good way of demonstrating the principle of combinations w/ repetition
##### Example: Say I want to choose from 5 colors total and I want to fill 20 items with those five colors. How many ways can I do that if repetition is allowed? 
- Well this isn't a typical combination problem because in normal combinations without repetition we assume that were removing a color choice as we move through our choices. That is not the case here.
- We can group these colors into 5 buckets by which we can distribute the 20 items in any ways we want
A visual representation may look something like this:
    Color 1|$\space$    Color 2 $\space$|  $\space$ Color 3    $\space$|$\space$   Color 4 $\space$|$\space$ Color 5 $\space$
- So we can place our 20 items however we like in these 5 buckets lets let "*" represent an individual item. What would that look like? Lets distribute them evenly for now so you can get the idea.
Color 1|$\space$    Color 2 $\space$|  $\space$ Color 3    $\space$|$\space$   Color 4 $\space$|$\space$ Color 5 
$****$ | $\space$ $****$ $\space$ | $\space$ $****$ $\space$| $\space$ $****$ $\space$ | $\space$ $****$

- Ok but how is that useful. Well lets take inventory of a few things here we have our 20 "$*$"s and each of them are separated by a divider bar **|** to signify a change in the Color group were looking at. Lets let **n** be the **amount of colors** were choosing from being five $n = 5$ . Hmm... well counting how many dividers we have would be four so **# of dividers = 4**. So we can express the number of dividers as always being **(n-1)** this gives us one piece of the formula that the stars and bars allows us to use. Let $(r = 20)$ is the amount of items where choosing from.
- So now we can arrive at the useful formula $\space\space _{r+n-1} C _r =\space _{20+4}C_{20} = \frac{24!}{20!(24-20)!} = 10626$
- So there are 10626 combinations of choosing colors for 20 items with repetition allowed
- **Stars and bars** method involves identifying how many categories or groups can be chosen and assigning that to **n** and identifying the amount of elements to be chosen being **r** and taking $r+n-1 \choose r$

## Combinations without Repetition
- Order still doesn't matter, thankfully much simpler to compute than w/ repetition. Similar to permutations but we have to remove the elements where the order mattered. For instance in a permutation of two letter combinations consisting of four possible letters we could imagine the possible combinations **ab** and **ba**, in a permutation since the order matters these are two distinct combinations so they count for 2 of the total. 
- Think of permutations like a password where the order has to be exact and even if you type in all the correct digits if the order isn't correct your password is wrong and it could represent someone elses password entirely.
- This however is **NOT** the case in combinations since the order doesn't matter there will be far fewer results to tabulate because we can not have the same set of values repeated twice. 
- For instance consider flipping a coin three times lets say your results were ***THT*** one time and ***HTT*** a different time. In a combinational problem both of these outcomes are considered the same you got 1 result that was Heads and two that were tails.
- Ok so now where do we go from here because theres a formula for this calculation just like the other 3 possibilities so how do we get that? 
- The formula comes from the idea that we have to remove the duplicate outcomes where the order is different but the values are the same.
- **Example: How many combinations of 3 letters can be formed from the string 'bit'?**
- Well lets approach this by listing out the permutations: $bit, bti, tbi, tib, itb, ibt$
- Ok that equals 6 which our math will agree with $_{3}P_{3} = \frac{n!}{(n-r)!} = \frac{3!}{(3-3)!} = \frac{3!}{0!} = 6$
- Theres something to notice about this example if were choosing 3 letters to fill 3 spots and we want to eliminate the amount of duplicate values that would end up leaving us with 1 solution. That works logically but know lets put a formula to it 

##### Formula: $ \space _nC_r =  \frac{n!}{r!(n-r)!}$
- This looks similar to the permutation formula right? it is somewhat with the addition of an **r!** in the denominator that is used to removed the duplicate combinations that could be in our our final result when calculated. Lets do another example.
- **Example: How many combinations of 3 letters can I make from the string 'binary'**
- First lets note that binary contains 6 distinct letters so let **n** = 6
- **r** will be used to represent the amount of possible places that our letters can occupy so for this problem that is 3. So the formula will look like this
$_6C_3 = \frac{6!}{3!(6-3)!} = \frac{6*5*4*3!}{3!*3!}= \frac{6*5*4}{3!} = 20$
- Therefore we have 20 possible combinations to choose 3 letters from 6 possible letters