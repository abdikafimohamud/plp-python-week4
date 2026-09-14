count = 1
total = 0

# BUG: missing colon at the end of the while statement, Python needs it to start the loop block
# BUG: condition was "count < 5", which stops the loop after count reaches 5,
# so 5 never gets added to total. Changed to "count <= 5" to include it.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: total is an int, can't concatenate it directly to a string with +, so convert it with str()
print("Sum of 1 to 5 is: " + str(total))