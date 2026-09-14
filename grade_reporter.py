scores = [72, 45, 90, 61, 38]

pass_count = 0
fail_count = 0
total = 0

for score in scores:
    if score >= 80:
        grade = "A"
        pass_count += 1
    elif score >= 70:
        grade = "B"
        pass_count += 1
    elif score >= 50:
        grade = "C"
        pass_count += 1
    else:
        grade = "F"
        fail_count += 1

    print(f"Score: {score} -> Grade: {grade}")

    total += score

average = round(total / len(scores), 1)

print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")
print(f"Average: {average}")