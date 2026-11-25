# Case Study 29: Password Policy Validation Engine

## Problem Statement
Evaluate sample password strings against minimum length, character-category, repetition, and prohibited-substring rules, and explain each failed condition.

## Objectives
- Validate candidate passwords against length, uppercase, lowercase, digit, and special-character rules.
- Detect consecutive repeated characters and prohibited substrings.
- Report clear, human-readable reasons for every failed rule.

## Assumptions
- Minimum required password length is `8` characters.
- Required character categories: at least one uppercase letter (`A-Z`), one lowercase letter (`a-z`), one digit (`0-9`), and one special character from `"!@#$%^&*()-_=+"`.
- More than `2` identical consecutive characters (i.e., `3` or more in a row, such as `"aaa"` or `"111"`) violate the repetition rule.
- Prohibited substrings are checked in lowercase (e.g., `"password"`, `"admin"`, `"qwerty"`, `"1234"`).

## Algorithm
1. Define a list of prohibited substrings and a string of allowed special characters.
2. For each candidate password string, initialize a `reasons = []` list.
3. Check length (`len(pwd) >= 8`), uppercase, lowercase, digit, and special character presence using loops and string comparisons.
4. Scan `pwd` with a loop to check if any character repeats 3 or more times consecutively.
5. Lowercase `pwd` (`pwd.lower()`) and check whether any prohibited substring appears using `in`.
6. Mark the password as `"VALID"` if `reasons` is empty, or `"INVALID"` with all collected reasons.

## Flowchart
```text
[Start]
   |
   v
[Read candidate password string]
   |
   v
[Check length >= 8, uppercase, lowercase, digit, special char]
   |
   v
[Check >= 3 consecutive identical characters]
   |
   v
[Check prohibited substrings in lowercase password]
   |
   +--> (Any rule failed?) --Yes--> [Record failure reasons -> INVALID]
   |         |
   |         No
   v
[Mark as VALID]
   |
   v
[Print validation report]
   |
   v
[Stop]
```

## Pseudocode
```text
BEGIN
    specials = "!@#$%^&*()-_=+"
    banned = ["password", "admin", "qwerty", "1234"]
    passwords = ["SafePass#9", "weak", "AAAbbb1!x", "MyPassword1!"]

    FOR each pwd IN passwords DO
        reasons = []
        IF LENGTH(pwd) < 8 THEN
            APPEND "Minimum length is 8 characters" TO reasons
        END IF

        has_upper = FALSE
        has_lower = FALSE
        has_digit = FALSE
        has_special = FALSE
        run_len = 1
        max_run = 1

        FOR i = 0 TO LENGTH(pwd) - 1 DO
            ch = pwd[i]
            IF ch >= "A" AND ch <= "Z" THEN has_upper = TRUE
            ELSE IF ch >= "a" AND ch <= "z" THEN has_lower = TRUE
            ELSE IF ch >= "0" AND ch <= "9" THEN has_digit = TRUE
            ELSE IF ch IN specials THEN has_special = TRUE
            END IF

            IF i > 0 AND pwd[i] == pwd[i - 1] THEN
                run_len = run_len + 1
                IF run_len > max_run THEN max_run = run_len END IF
            ELSE
                run_len = 1
            END IF
        END FOR

        IF NOT has_upper THEN APPEND "Missing uppercase letter" TO reasons END IF
        IF NOT has_lower THEN APPEND "Missing lowercase letter" TO reasons END IF
        IF NOT has_digit THEN APPEND "Missing digit" TO reasons END IF
        IF NOT has_special THEN APPEND "Missing special character" TO reasons END IF
        IF max_run >= 3 THEN APPEND "Contains 3 or more repeating characters" TO reasons END IF

        low_pwd = LOWERCASE(pwd)
        FOR each bad IN banned DO
            IF bad IN low_pwd THEN
                APPEND "Contains prohibited substring: " + bad TO reasons
            END IF
        END FOR

        IF LENGTH(reasons) == 0 THEN
            PRINT pwd, "-> VALID"
        ELSE
            PRINT pwd, "-> INVALID", reasons
        END IF
    END FOR
END
```



## Test Cases
| Test Case | Password Input | Expected Result |
| :--- | :--- | :--- |
| TC-1 (Strong password) | `"SafePass#9"` | `VALID` |
| TC-2 (Short & missing categories) | `"weak"` | `INVALID` (length < 8, missing uppercase, digit, special char) |
| TC-3 (Consecutive repetition) | `"AAAbbb1!x"` | `INVALID` (3 or more consecutive repeating characters) |
| TC-4 (Prohibited substring) | `"MyPassword1!"` | `INVALID` (contains prohibited substring `"password"`) |

## Sample Output
```text
=== Password Policy Validation Report ===
Password     : SafePass#9
Status       : VALID

Password     : weak
Status       : INVALID
Reasons      :
  - Minimum length is 8 characters
  - Missing uppercase letter
  - Missing digit
  - Missing special character

Password     : AAAbbb1!x
Status       : INVALID
Reasons      :
  - Contains 3 or more consecutive repeating characters

Password     : MyPassword1!
Status       : INVALID
Reasons      :
  - Contains prohibited substring: 'password'
```


## Conclusion
Character-by-character scanning paired with string normalization (`lower()`) and substring checks provides a clear, rule-by-rule password audit using basic string and list operations.
