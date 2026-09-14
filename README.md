# Week 4 Assignment - Conditions and Loops

Grade Reporter & Bug Hunt: two small Python programs practicing loops, conditionals, and debugging.

## Files

- **`grade_reporter.py`** - Loops through a list of five scores using a `for` loop. For each score, an `if`/`elif`/`else` chain assigns a grade (A, B, C, or F), which is printed alongside the score. The program also keeps a running count of passes and fails, and calculates the class average, rounded to one decimal place.

- **`bug_hunt.py`** - A broken `while` loop meant to sum the numbers 1 to 5. Originally contained three bugs:
  1. A missing colon at the end of the `while` statement, which caused a `SyntaxError`.
  2. String concatenation with an integer in the final `print` statement, which caused a `TypeError` (fixed with `str()`).
  3. A loop condition (`count < 5`) that excluded the number 5 from the total, causing the program to run without errors but print the wrong result (10 instead of 15). Changed to `count <= 5` to fix it.

  Each fix is marked with a `# BUG:` comment directly above the corrected line.

## Reflection

The hardest bug to find was the third one in `bug_hunt.py`, since it didn't raise any error — the program ran normally but printed 10 instead of 15. I knew something was wrong because I compared the output to the expected answer given in the assignment, then walked through the loop by hand and noticed the loop stopped as soon as `count` reached 5, so 5 was never added to the total.

## Screenshots

Screenshots of both programs running successfully are in the `screenshots/` folder.