# AI Code Review Assignment (Python)

## Candidate
- Name: [Your Name]
- Approximate time spent: 90 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Division by zero error when input list is empty (len(orders) = 0)
- Calculates average using total order count instead of non-cancelled order count, leading to incorrect average

### Edge cases & risks
- Empty orders list causes ZeroDivisionError
- Orders with missing "status" or "amount" keys will cause KeyError
- Orders with non-numeric "amount" values will cause TypeError

### Code quality / design issues
- No input validation or error handling
- Does not account for the fact that cancelled orders should not be counted in denominator

## 2) Proposed Fixes / Improvements
### Summary of changes
- Handle empty orders list by returning 0.0
- Only count non-cancelled orders in the denominator when calculating average
- Add validation for "status" and "amount" keys to prevent KeyError
- Validate that amount is numeric to prevent TypeError
- Use .get() method for safer dictionary access

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

Test with empty list, list with all cancelled orders, list with mixed valid/cancelled orders, orders with invalid amounts, orders missing required keys, and normal valid orders to ensure correct calculation and error handling.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The explanation incorrectly states that cancelled orders are excluded from the calculation when they're still counted in the denominator
- Fails to mention that the function crashes with empty lists
- Does not mention the lack of input validation

### Rewritten explanation
- This function calculates the average value of non-cancelled orders by summing the amounts of valid orders and dividing by the count of non-cancelled orders. It handles empty lists by returning 0.0 and validates order data to prevent errors.

## 4) Final Judgment
- Decision: Reject
- Justification: The original code has critical bugs including division by zero and incorrect calculation logic that would produce wrong results even when not crashing.
- Confidence & unknowns: Confident in the assessment; the bugs are clear and significant.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Only checks for presence of '@' symbol without proper email validation
- Does not handle None values or non-string inputs

### Edge cases & risks
- Empty list is handled correctly but empty strings would be counted if they had '@'
- Inputs like 'user@domain', '@domain.com', 'user@' would be incorrectly counted as valid
- Non-string inputs would cause TypeError

### Code quality / design issues
- Extremely basic validation that doesn't follow email format rules
- No consideration for RFC-compliant email validation

## 2) Proposed Fixes / Improvements
### Summary of changes
- Add proper email validation that checks for both valid local and domain parts
- Handle non-string inputs by skipping them
- Check for proper email format including presence of both local part and domain with TLD
- Strip whitespace from email strings before validation

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 

### Testing Considerations
Test with valid emails, invalid emails (missing @, missing domain, missing TLD), empty strings, None values, non-string inputs, and mixed lists to ensure proper validation and counting.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- The original code does NOT safely ignore invalid entries - it has very weak validation
- Claims to handle empty input correctly, but this is true only by coincidence
- Misleadingly suggests proper email validation exists

### Rewritten explanation
- This function counts email addresses that contain an '@' symbol with a valid format - a non-empty local part and a domain part containing a period. It skips non-string inputs, empty strings, and malformed email addresses.

## 4) Final Judgment
- Decision: Reject
- Justification: The original code has critical validation issues that would count many invalid email formats as valid, completely undermining its purpose.
- Confidence & unknowns: Confident in the assessment; the validation is clearly inadequate for real-world use.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Division by zero error when input list is empty
- Divides by total values count instead of count of valid (non-None) values, leading to incorrect average calculation

### Edge cases & risks
- Empty list causes ZeroDivisionError
- Non-numeric values would cause ValueError when converted to float
- Mixed data types could cause unexpected behavior

### Code quality / design issues
- No input validation or error handling
- Incorrect denominator in average calculation

## 2) Proposed Fixes / Improvements
### Summary of changes
- Handle empty list by returning 0.0
- Only count valid (non-None and convertible to float) values in the denominator
- Add proper exception handling for non-numeric values
- Skip invalid values instead of crashing

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

Test with empty list, list with all None values, list with mixed valid/invalid values, non-numeric values, and normal valid values to ensure proper calculation and error handling.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- The explanation claims it safely handles mixed input types, but the original code crashes with non-numeric values
- Does not mention the division by zero issue with empty lists
- Falsely suggests that the average calculation is accurate when it uses wrong denominator

### Rewritten explanation
- This function calculates the average of valid numeric measurements by summing non-None values that can be converted to float, and dividing by the count of those valid values. It handles empty lists and invalid values gracefully.

## 4) Final Judgment
- Decision: Reject
- Justification: The original code has critical bugs including division by zero and incorrect calculation logic that would produce wrong results.
- Confidence & unknowns: Confident in the assessment; the bugs are clear and significant.
