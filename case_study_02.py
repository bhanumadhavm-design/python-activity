def calculate_slab_charge(units):
    if units <= 100:
        return units * 3.0
    elif units <= 250:
        return (100 * 3.0) + ((units - 100) * 4.5)
    elif units <= 500:
        return (100 * 3.0) + (150 * 4.5) + ((units - 250) * 6.0)
    else:
        return (100 * 3.0) + (150 * 4.5) + (250 * 6.0) + ((units - 500) * 7.5)


def process_electricity_bills(monthly_readings, fixed_charge=75.0, spike_threshold=35.0):
    billing_records = []
    alerts = []

    for month, units in monthly_readings:
        if units < 0:
            raise ValueError("Units consumed cannot be negative.")
        energy_charge = calculate_slab_charge(units)
        subtotal = energy_charge + fixed_charge

        if units <= 120:
            final_bill = subtotal * 0.95
        elif units > 500:
            final_bill = subtotal * 1.08
        else:
            final_bill = subtotal

        billing_records.append((month, units, round(final_bill, 2)))

    for idx in range(1, len(billing_records)):
        prev_month, prev_units, _ = billing_records[idx - 1]
        curr_month, curr_units, _ = billing_records[idx]
        if prev_units > 0:
            pct_increase = ((curr_units - prev_units) / prev_units) * 100
            if pct_increase > spike_threshold:
                alerts.append((prev_month, curr_month, round(pct_increase, 2)))

    return billing_records, alerts


if __name__ == "__main__":
    sample_data = [
        ("Jan", 95),
        ("Feb", 180),
        ("Mar", 240),
        ("Apr", 520),
    ]
    records, spike_alerts = process_electricity_bills(sample_data)

    print("=== Monthly Electricity Billing Summary ===")
    for month, units, bill in records:
        print(f"{month:<6} | Units: {units:<4} | Bill: Rs. {bill:.2f}")

    print("\n=== Unusual Consumption Increases (>35%) ===")
    if not spike_alerts:
        print("No unusual increases detected.")
    else:
        for m1, m2, pct in spike_alerts:
            print(f"{m1} -> {m2}: +{pct:.2f}% increase in consumption")
