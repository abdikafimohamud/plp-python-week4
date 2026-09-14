scores = [72, 45, 90, 61, 38]

pass_count = 0
fail_count = 0
total = 0

for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(f"Score: {score} -> Grade: {grade}")

    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1

    total += score

average = round(total / len(scores), 1)

print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")
print(f"Average: {average}")