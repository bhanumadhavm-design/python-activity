# Case Study 2: Progressive Electricity Billing

## Problem Statement
Calculate household electricity bills across multiple months using progressive consumption slabs, fixed charges, surcharges, and rebates, then compare bills across several months and identify unusual consumption increases.

## Objectives
- Compute monthly energy charges across progressive unit slabs.
- Apply fixed meter charges, rebates for low usage, and surcharges for high usage.
- Compare consecutive months to flag unusual spikes in consumption.

## Assumptions
- Units consumed are non-negative integers.
- Progressive slabs:
  - `0–100` units: Rs. 3.00/unit
  - `101–250` units: Rs. 4.50/unit
  - `251–500` units: Rs. 6.00/unit
  - Above `500` units: Rs. 7.50/unit
- Fixed monthly charge is Rs. 75.00.
- A 5% rebate applies on the subtotal if units consumed $\le 120$; an 8% surcharge applies if units consumed $> 500$.
- An increase of more than **35%** over the previous month's units is flagged as an unusual increase.

## Algorithm
1. Store monthly readings as a list of `(month_name, units)` tuples.
2. For each month, calculate slab-wise energy charges using conditional branches.
3. Add the fixed charge to compute the subtotal, then apply the 5% rebate (units $\le 120$) or 8% surcharge (units $> 500$).
4. Store `(month_name, units, final_bill)` in a results list.
5. Iterate through consecutive months in the results list to compute percentage change in units and record pairs exceeding 35%.
6. Display the formatted monthly billing table and any flagged unusual increases.

## Flowchart
```text
[Start]
   |
   v
[Load monthly (month, units) tuples]
   |
   v
[For each month: compute slab cost + fixed charge]
   |
   +--> (units <= 120?) --Yes--> [Apply 5% rebate]
   |         |
   |         No
   |         v
   +--> (units > 500?)  --Yes--> [Apply 8% surcharge]
   |         |
   |         No
   v
[Append (month, units, bill) to records list]
   |
   v
[Loop consecutive months: check if unit jump > 35%]
   |
   v
[Print summary & unusual increases]
   |
   v
[Stop]
```

## Pseudocode
```text
BEGIN
    monthly_data = [("Jan", 95), ("Feb", 180), ("Mar", 240), ("Apr", 520)]
    fixed_charge = 75.0
    records = []

    FOR each (month, units) IN monthly_data DO
        IF units <= 100 THEN
            cost = units * 3.0
        ELSE IF units <= 250 THEN
            cost = 100 * 3.0 + (units - 100) * 4.5
        ELSE IF units <= 500 THEN
            cost = 100 * 3.0 + 150 * 4.5 + (units - 250) * 6.0
        ELSE
            cost = 100 * 3.0 + 150 * 4.5 + 250 * 6.0 + (units - 500) * 7.5
        END IF

        subtotal = cost + fixed_charge
        IF units <= 120 THEN
            total = subtotal * 0.95
        ELSE IF units > 500 THEN
            total = subtotal * 1.08
        ELSE
            total = subtotal
        END IF

        APPEND (month, units, ROUND(total, 2)) TO records
    END FOR

    FOR each (m, u, b) IN records DO
        PRINT m, u, b
    END FOR

    FOR i = 1 TO LENGTH(records) - 1 DO
        prev_m, prev_u, _ = records[i - 1]
        curr_m, curr_u, _ = records[i]
        IF prev_u > 0 THEN
            pct_change = ((curr_u - prev_u) / prev_u) * 100
            IF pct_change > 35.0 THEN
                PRINT prev_m, "->", curr_m, ROUND(pct_change, 2), "%"
            END IF
        END IF
    END FOR
END
```


## Test Cases
| Test Case | Input `(Month, Units)` | Expected Outcome |
| :--- | :--- | :--- |
| TC-1 (Rebate slab) | `("Jan", 95)` | Slab `285.0` + Fixed `75.0` = `360.0`; 5% rebate $\rightarrow$ `Rs. 342.00` |
| TC-2 (Mid slabs + spike) | `("Feb", 180)` after `95` | `300 + 360 + 75` = `Rs. 735.00`; `+89.47%` spike flagged |
| TC-3 (Surcharge slab + spike) | `("Apr", 520)` after `240` | `2625 + 75 = 2700`; 8% surcharge $\rightarrow$ `Rs. 2916.00`; `+116.67%` spike flagged |

## Sample Output
```text
=== Monthly Electricity Billing Summary ===
Jan    | Units: 95   | Bill: Rs. 342.00
Feb    | Units: 180  | Bill: Rs. 735.00
Mar    | Units: 240  | Bill: Rs. 1005.00
Apr    | Units: 520  | Bill: Rs. 2916.00

=== Unusual Consumption Increases (>35%) ===
Jan -> Feb: +89.47% increase in consumption
Mar -> Apr: +116.67% increase in consumption
```


## Conclusion
This program demonstrates progressive slab evaluation, conditional rebates/surcharges, and consecutive-period anomaly detection using only lists, tuples, tuple unpacking, conditionals, and loops.
