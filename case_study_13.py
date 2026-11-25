def simulate_atm(opening_balance, transactions, per_txn_limit=15000.0, daily_limit=25000.0):
    balance = float(opening_balance)
    daily_withdrawn = 0.0
    total_deposited = 0.0
    approved = 0
    rejected = 0
    audit_log = []

    for txn_type, amount in transactions:
        kind = txn_type.strip().upper()
        if amount <= 0:
            rejected += 1
            audit_log.append(("REJECTED", kind, amount, "Amount must be greater than zero", round(balance, 2)))
            continue

        if kind == "DEPOSIT":
            balance += amount
            total_deposited += amount
            approved += 1
            audit_log.append(("APPROVED", kind, amount, "Deposit credited", round(balance, 2)))

        elif kind == "WITHDRAW":
            if amount > per_txn_limit:
                rejected += 1
                audit_log.append(("REJECTED", kind, amount, f"Exceeds per-txn limit ({per_txn_limit:.2f})", round(balance, 2)))
            elif (daily_withdrawn + amount) > daily_limit:
                rejected += 1
                audit_log.append(("REJECTED", kind, amount, f"Exceeds daily limit ({daily_limit:.2f})", round(balance, 2)))
            elif amount > balance:
                rejected += 1
                audit_log.append(("REJECTED", kind, amount, "Insufficient funds", round(balance, 2)))
            else:
                balance -= amount
                daily_withdrawn += amount
                approved += 1
                audit_log.append(("APPROVED", kind, amount, "Withdrawal dispensed", round(balance, 2)))

        else:
            rejected += 1
            audit_log.append(("REJECTED", kind, amount, "Unsupported transaction type", round(balance, 2)))

    summary = (
        round(float(opening_balance), 2),
        round(balance, 2),
        round(total_deposited, 2),
        round(daily_withdrawn, 2),
        approved,
        rejected,
    )
    return audit_log, summary


if __name__ == "__main__":
    txns = [
        ("deposit", 5000.0),
        ("withdraw", 18000.0),
        ("withdraw", 12000.0),
        ("withdraw", 14000.0),
        ("withdraw", 5000.0),
        ("withdraw", -100.0),
    ]

    log, summary = simulate_atm(10000.0, txns)
    open_bal, close_bal, tot_dep, tot_wd, app_cnt, rej_cnt = summary

    print("=== ATM Transaction Log ===")
    for status, kind, amt, reason, bal in log:
        print(f"[{status:<8}] {kind:<8} Rs.{amt:<8.2f} | Bal: Rs.{bal:<8.2f} | {reason}")

    print("\n=== Session Summary ===")
    print(f"Opening Balance     : Rs. {open_bal:.2f}")
    print(f"Closing Balance     : Rs. {close_bal:.2f}")
    print(f"Total Deposited     : Rs. {tot_dep:.2f}")
    print(f"Total Withdrawn     : Rs. {tot_wd:.2f}")
    print(f"Approved / Rejected : {app_cnt} / {rej_cnt}")
