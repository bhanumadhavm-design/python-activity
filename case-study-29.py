def validate_password(password, min_length=8):
    special_chars = "!@#$%^&*()-_=+"
    prohibited_substrings = ["password", "admin", "qwerty", "1234"]
    reasons = []

    if len(password) < min_length:
        reasons.append(f"Minimum length is {min_length} characters")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    current_run = 1
    max_run = 1

    for idx in range(len(password)):
        ch = password[idx]
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_digit = True
        elif ch in special_chars:
            has_special = True

        if idx > 0 and password[idx] == password[idx - 1]:
            current_run += 1
            if current_run > max_run:
                max_run = current_run
        else:
            current_run = 1

    if not has_upper:
        reasons.append("Missing uppercase letter")
    if not has_lower:
        reasons.append("Missing lowercase letter")
    if not has_digit:
        reasons.append("Missing digit")
    if not has_special:
        reasons.append("Missing special character")
    if max_run >= 3:
        reasons.append("Contains 3 or more consecutive repeating characters")

    lowered = password.lower()
    for bad_word in prohibited_substrings:
        if bad_word in lowered:
            reasons.append(f"Contains prohibited substring: '{bad_word}'")

    is_valid = len(reasons) == 0
    return (password, is_valid, reasons)


if __name__ == "__main__":
    candidates = [
        "SafePass#9",
        "weak",
        "AAAbbb1!x",
        "MyPassword1!",
    ]

    print("=== Password Policy Validation Report ===")
    for candidate in candidates:
        pwd, valid, fail_reasons = validate_password(candidate)
        status = "VALID" if valid else "INVALID"
        print(f"\nPassword     : {pwd}")
        print(f"Status       : {status}")
        if not valid:
            print("Reasons      :")
            for r in fail_reasons:
                print(f"  - {r}")
