# Leap Year Checker

The Leap Year Checker is a Python script that allows you to check whether a given year is a leap year or a normal year. 
A leap year occurs every four years, except for years that are divisible by 100 but not divisible by 400.

## Leap Year Determination Logic
The script uses the following logic to determine whether a given year is a leap year:

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:

    / Year is a leap year

else:

    / Year is not a leap year
### Explanation of the logic:

~The year is considered a leap year if it is divisible by 4 but not divisible by 100.

~Alternatively, if the year is divisible by 400, it is also a leap year.

## Example Output
Below are some examples of the output you can expect from the script:

Which year do you want to check? 2020

Leap year.

Because 2020 is cleanly divisible by 4 and not by 100.



Which year do you want to check? 1900

Normal year.

Because 1900 is NOT divisible by 4 or is divisible by 100 but not by 400.


## Contribution
Contributions to this project are welcome! If you find any issues or 
have suggestions for improvement, please open an issue or submit a pull request.
