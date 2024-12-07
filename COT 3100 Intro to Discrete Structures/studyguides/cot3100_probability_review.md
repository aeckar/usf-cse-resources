# Step-by-Step Approach for Probability Problems
<ol>
<li>Understand the problem</li>
    <ul>
        <li> <strong>Question</strong>: What is the problem asking me to find?</li>
            <ul>
                <li> A single probability? (e.g.,P(A))</li>
                <li> A joint probability? (e.g., P(A ∩ B))</li>
                <li> A conditional probability? (e.g., P(A|B) )</li>
                <li> A complement? (e.g., P( A<sup>c</sup> ) )</li>
                <li> An expected value or a count of outcomes? </li>
            </ul>
        <li> Write down the key events and assign probabilities to them if possible.</li>
    </ul>

<hr>

<li>Analyze the events</li>
    <ul>
        <li> <strong>Question</strong>: What events are involved?</li>
            <ul>
                <li>Identify key events, such as A, B, C, etc., and define them clearly</li>
                <li>Determine whether these events are independent, dependent, mutually exclusive, or overlapping:</li>
                    <ul>
                        <li><strong>Independent</strong>: Does P(A|B) = P(A)? If yes, events are independent.</li>
                        <li><strong>Dependent</strong>: If not independent, use conditional probabilities like P(A|B).</li>
                        <li><strong>Mutually Exclusive</strong>: Does (A ∩ B) = ∅? If yes, P(A ∩ B).</li>
                        <li><strong>Overlapping</strong>: If not mutually exclusive, find overlaps P(A ∩ B).</li>
                    </ul>
            </ul>
    </ul>

<hr>

<li>Break Down the Problem</li>
    <ul>
        <li> <strong>Question</strong>: Is this a complex problem that needs to be broken into smaller parts?</li>
            <ul>
                <li>For Example: </li>
                    <ul>
                        <li>If dealing with "at least one," use the complement rule: P(at least one) = 1 - P(none).</li>
                        <li>For "exactly <em>k</em>" successes, consider using the binomial formula or combinatorics.</li>
                        <li>For "multiple steps," draw a probability tree diagram or list possible outcomes.</li>
                    </ul>
            </ul>
    </ul>

<hr>

<li>Identify the Correct Formula</li>
    <ul>
        <li> <strong>Question</strong>: Which formula(s) can i use? </li>
            <ul>
                <li>For basic probabilities:</li>
                    <ul>
                        <li>P(A<sup>c</sup>) = 1 - P(A) (Complement Rule)</li>
                        <li>P(A ∪ B) = P(A) + P(B) - P(A ∩ B) (Union of Two Events)</li>
                        <li>P(A ∩ B) = P(A) * P(B|A) (General Multiplication Rule)</li>
                        <li>For independent events: P(A ∩ B) = P(A) * P(B)</li>
                        <li>P(A|B) = <sup>P(A ∩ B)</sup> &frasl; <sub>P(B)</sub> (Conditional probability)</li>
                    </ul>
                <li>For repeated trials or success/failure problems:</li>
                    <ul>
                        <li>Binomial Formula: P(X = k) = (<sub>n</sub>C<sub>k</sub>) * p<sup>k</sup> * (1 - p)<sup>n - k</sup></li>
                        <li>Complement rule for "at least one" or similar cases.</li>
                    </ul>
                <li>For expected values:</li>
                    <ul>
                        <li>Use the weighted average formula: E(X) = ∑ x<sub>i</sub> * P(x<sub>i</sub>).
                    </ul>
            </ul>
    </ul>

<hr>

<li>Evaluate Constraints or Conditions</li>
    <ul>
        <li> <strong>Question</strong>: Does the problem involve restrictions or constraints?</li>
            <ul>
                <li>E.g., Are events drawn "with replacement" or "without replacement"? (This affects independence.)</li>
                <li>Are all outcomes equally likely, or do they have different probabilities?</li>
            </ul>
    </ul>

<hr>

<li>Solve Step-by-Step</li>
    <ul>
        <li> <strong>Question</strong>: What is the simplest step I can take next?</li>
            <ul>
                <li>Calculate the probability of individual events first.</li>
                <li>Combine events using formulas as necessary</li>
                <li>Solve using logical sequence</li>
            </ul>
    </ul>

<hr>

<li>Verify Your Answer</li>
    <ul>
        <li> <strong>Question</strong>: Does my answer make sense?</li>
            <ul>
                <li>Probabilities must lie between 0 and 1 (or between 0% and 100%).</li>
                <li>Double-check for overlooked complements or missing outcomes.</li>
                <li>Revisit whether the question asks for exact probabilities, percentages, or expected values. </li>
            </ul>
    </ul>
</ol>

<hr>
<h1> Sample Questions to Ask Yourself for Each Type of Problem</h1>
<hr>

<h3>Basic Probability</h3>
    <ul>
        <li>Do I need the probability of one event, the union/intersection of events, or the complement?</li>
        <li>Are the events independent or dependent?</li>
    </ul>
<h3>Conditional Probability</h3>
    <ul>
        <li>What is the condition? Write it clearly.</li>
        <li>Am I using P(A|B) = <sup>P(A ∩ B)</sup> &frasl; <sub>P(B)</sub>?</li>
    </ul>
<h3>"At Least" or "At Most"</h3>
    <ul>
        <li>Can I use the complement rule (e.g., "at least one" = 1 - P(none) )?</li>
        <li>Do I need to compute the individual probabilities or use a shortcut like the binomial formulas?</li>
    </ul>
<h3>Counting Problems (Combinatorics)</h3>
     <ul>
        <li>Are all outcomes equally likely</li>
        <li>Do I need permutations (n!) or combinations ( <sub>n</sub>C<sub>r</sub> )</li>
        <li> Is the selection "with" or "without" replacement?</li>
    </ul>
<h3> Repeated Trials </h3>
    <ul>
        <li>Can I use the binomial distribution?</li>
        <li>Are the trials independent?</li>
    </ul>
<h3>Expected Value</h3>
    <ul>
        <li>What are the possible outcomes and their associated probabilities?</li>
        <li>Use E (X) = ∑ x<sub>i</sub> * P( x<sub>i</sub> )</li>
    </ul>

<hr>
<h1> Example Problem Walkthrough </h1>
<hr>
<h4> Problem: </h4>
<p> A fair die is rolled three times. What is the probability of rolling at least one "6"?</p>

<h5>Step-by-Step</h5>
    <ol>
    <li>Understand the Problem:</li>
        <ul>
            <li>"At least one 6" = P(at least one 6) = 1 - P(no 6s).</li>
        </ul>
    <li>Analyze Events:</li>
        <ul>
            <li>Each die roll is independent.</li>
            <li>Probability of rolling no 6 on one roll: P(not 6) = 5/6</li>
        </ul>
    <li>Break Down Problem:</li>
        <ul>
            <li>Probability of no 6s on three rolls: (5/6)<sup>3</sup>.</li>
        </ul>
    <li>Apply Formula:</li>
        <ul>
            <li>P(at least one 6) = 1 - (5/6)<sup>3</sup> = 1 - 125/216.</li>
        </ul>
    <li>Solve and Verify</li>
        <ul>
            <li>P(at least one 6) = 91/216 ≈ 0.4213 = 42.13%.</li>
        </ul>
    </ol>
By asking questions at each stage, you can systematically solve most probability problems!