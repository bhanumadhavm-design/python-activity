def evaluate_submissions(answer_key, submissions, correct_marks=4.0, negative_marks=1.0):
    key = answer_key.strip().upper()
    max_score = len(key) * correct_marks
    evaluated = []

    for student_id, response in submissions:
        cleaned = response.strip().upper()
        if len(cleaned) != len(key):
            raise ValueError(
                f"Response length ({len(cleaned)}) does not match answer key length ({len(key)}) for {student_id}."
            )

        correct = 0
        incorrect = 0
        unanswered = 0

        for idx in range(len(key)):
            ans = cleaned[idx]
            if ans == "-":
                unanswered += 1
            elif ans == key[idx]:
                correct += 1
            else:
                incorrect += 1

        net_score = (correct * correct_marks) - (incorrect * negative_marks)
        percentage = (net_score / max_score) * 100.0 if max_score > 0 else 0.0
        evaluated.append(
            (student_id, correct, incorrect, unanswered, round(net_score, 2), round(percentage, 2))
        )

    return evaluated, max_score


if __name__ == "__main__":
    official_key = "ABCDABCDAB"
    student_responses = [
        ("S01", "ABCDABCDAB"),
        ("S02", "AB-DACBD-B"),
        ("S03", "DDDDDDDDDD"),
    ]

    results, total_possible = evaluate_submissions(official_key, student_responses)

    print(f"Answer Key: {official_key} ({len(official_key)} Questions, Max Marks: {total_possible:.1f})\n")
    print(f"{'Student':<7} | {'Correct':<7} | {'Wrong':<5} | {'Skipped':<7} | {'Score':<6} | {'Percentage'}")
    print("-" * 59)
    for sid, corr, wrong, skip, score, pct in results:
        print(f"{sid:<7} | {corr:<7} | {wrong:<5} | {skip:<7} | {score:<6.2f} | {pct:.2f}%")
