def ceil_positive(value):
    whole = int(value)
    if value > whole:
        return whole + 1
    return whole


def classes_for_full_attendance(attended, total, threshold):
    current_pct = (attended / total) * 100.0
    if current_pct >= threshold:
        return 0
    target_ratio = threshold / 100.0
    needed = ((target_ratio * total) - attended) / (1.0 - target_ratio)
    return max(0, ceil_positive(needed))


def classes_for_partial_pattern(attended, total, threshold, attend_every_n_skip_one=5):
    """Simulates attending (n - 1) out of every n upcoming classes."""
    curr_att = attended
    curr_tot = total
    steps = 0
    max_steps = 1000

    while ((curr_att / curr_tot) * 100.0) < threshold and steps < max_steps:
        steps += 1
        curr_tot += 1
        if steps % attend_every_n_skip_one != 0:
            curr_att += 1

    if ((curr_att / curr_tot) * 100.0) >= threshold:
        return steps
    return -1


if __name__ == "__main__":
    eligibility_threshold = 75.0
    student_records = [
        ("STU01", 30, 50),
        ("STU02", 40, 50),
        ("STU03", 21, 40),
    ]

    print(f"Eligibility Threshold: {eligibility_threshold:.1f}%\n")
    for sid, att, tot in student_records:
        curr_pct = (att / tot) * 100.0
        min_full = classes_for_full_attendance(att, tot, eligibility_threshold)
        min_4_of_5 = classes_for_partial_pattern(att, tot, eligibility_threshold, 5)

        print(f"Student: {sid} | Current: {curr_pct:.2f}% ({att}/{tot})")
        print(f"  - Consecutive classes at 100% attendance : {min_full}")
        if min_4_of_5 != -1:
            print(f"  - Classes needed (attending 4 of every 5) : {min_4_of_5}")
        else:
            print("  - Classes needed (attending 4 of every 5) : Not reachable")
