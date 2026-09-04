# Enter your code here. Read input from STDIN. Print output to STDOUT

actual_day, actual_month, actual_year = map(int, input().split())
expected_day, expected_month, expected_year = map(int, input().split())

if actual_year > expected_year:
    fine = 10000

elif actual_year == expected_year and actual_month > expected_month:
    fine = 500 * (actual_month - expected_month)

elif actual_year == expected_year and actual_month == expected_month and actual_day > expected_day:
    fine = 15 * (actual_day - expected_day)

else:
    fine = 0

print(fine)