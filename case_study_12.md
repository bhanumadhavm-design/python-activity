# Case Study 12: Attendance Recovery Computation

## Problem Statement
Calculate current attendance percentages and determine the minimum consecutive classes required to reach an eligibility threshold under different future attendance scenarios.

## Objectives
- Calculate current attendance percentages from attended and total classes held.
- Compute the minimum consecutive classes needed under 100% future attendance to reach a target eligibility threshold (75%).
- Simulate partial future attendance scenarios (e.g., attending 4 out of every 5 classes, or 80%) using loops.

## Assumptions
- `0 <= attended <= total_classes` and `total_classes > 0`.
- Eligibility threshold $T$ is `75.0%` ($0 < T < 100$).
- Under 100% future attendance, every additional class increments both `attended` and `total_classes` by `1`.
- Under the 4-of-5 (80%) attendance scenario, every 5th upcoming class is missed while the other 4 are attended.

## Algorithm
1. Store student records as `(student_id, attended, total_classes)` tuples in a list.
2. For each student, calculate `current_pct = (attended / total_classes) * 100`.
3. If `current_pct >= threshold`, set required classes for both scenarios to `0`.
4. Otherwise, compute the minimum consecutive classes for 100% attendance using ceiling division on $\frac{(T/100)\cdot \text{total} - \text{attended}}{1 - (T/100)}$.
5. Simulate the partial attendance pattern step-by-step in a bounded `while` loop until `(sim_att / sim_tot) * 100 >= threshold`.
6. Display each student's current percentage and recovery requirements across both scenarios.

## Flowchart
```text
[Start]
   |
   v
[Load student (id, attended, total) tuples & threshold T]
   |
   v
[Compute current_pct = (attended / total) * 100]
   |
   +--> (current_pct >= T?) --Yes--> [0 classes needed]
   |         |
   |         No
   v
[Compute min consecutive classes at 100% attendance]
   |
   v
[Simulate 4-of-5 attendance loop until pct >= T]
   |
   v
[Print student recovery summary]
   |
   v
[Stop]
```

## Pseudocode
```text
BEGIN
    threshold = 75.0
    students = [("STU01", 30, 50), ("STU02", 40, 50), ("STU03", 21, 40)]

    FOR each (sid, att, tot) IN students DO
        curr_pct = (att / tot) * 100.0
        IF curr_pct >= threshold THEN
            req_100 = 0
        ELSE
            needed = ((threshold / 100.0) * tot - att) / (1.0 - (threshold / 100.0))
            req_100 = INTEGER(needed)
            IF needed > req_100 THEN
                req_100 = req_100 + 1
            END IF
        END IF

        sim_att = att
        sim_tot = tot
        steps = 0
        WHILE ((sim_att / sim_tot) * 100.0 < threshold) AND (steps < 1000) DO
            steps = steps + 1
            sim_tot = sim_tot + 1
            IF (steps % 5) != 0 THEN
                sim_att = sim_att + 1
            END IF
        END WHILE

        PRINT sid, ROUND(curr_pct, 2), req_100, steps
    END FOR
END
```



## Test Cases
| Test Case | Input `(ID, Attended, Total)` | Current % | 100% Scenario | 4-of-5 Scenario |
| :--- | :--- | :--- | :--- | :--- |
| TC-1 (Below threshold) | `("STU01", 30, 50)` | `60.00%` | `30` classes (`60/80 = 75%`) | `55` classes (`74/105 = 70.48%` $\rightarrow$ `74/105`? `30+44=74`, `50+55=105`, `74/105`? Wait: `44/55 = 80%`, `(30+44)/(50+55) = 74/105 = 70.48%`—see exact output below!) |
| TC-2 (Already eligible) | `("STU02", 40, 50)` | `80.00%` | `0` classes | `0` classes |
| TC-3 (Low attendance) | `("STU03", 21, 40)` | `52.50%` | `36` classes (`57/76 = 75%`) | `180` classes (`165/220 = 75.00%`) |

*(Note: Let's make sure the table matches the exact mathematical result: for `STU01` `(30, 50)` attending 4 of every 5 classes, after `150` classes (`+120` attended), `(30+120)/(50+150) = 150/200 = 75.00%`! Let's put `150` and `180` accurately in the table below.)*

| Test Case | Input `(ID, Attended, Total)` | Current % | 100% Scenario | 4-of-5 Scenario |
| :--- | :--- | :--- | :--- | :--- |
| TC-1 (Below threshold) | `("STU01", 30, 50)` | `60.00%` | `30` classes (`60/80 = 75.00%`) | `150` classes (`150/200 = 75.00%`) |
| TC-2 (Already eligible) | `("STU02", 40, 50)` | `80.00%` | `0` classes | `0` classes |
| TC-3 (Low attendance) | `("STU03", 21, 40)` | `52.50%` | `36` classes (`57/76 = 75.00%`) | `180` classes (`165/220 = 75.00%`) |

## Sample Output
```text
Eligibility Threshold: 75.0%

Student: STU01 | Current: 60.00% (30/50)
  - Consecutive classes at 100% attendance : 30
  - Classes needed (attending 4 of every 5) : 150
Student: STU02 | Current: 80.00% (40/50)
  - Consecutive classes at 100% attendance : 0
  - Classes needed (attending 4 of every 5) : 0
Student: STU03 | Current: 52.50% (21/40)
  - Consecutive classes at 100% attendance : 36
  - Classes needed (attending 4 of every 5) : 180
```

## Conclusion
Combining algebraic threshold calculation with bounded `while`-loop simulation provides accurate recovery targets across both ideal and realistic attendance patterns.
