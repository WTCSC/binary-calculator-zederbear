[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17650013)
# Binary Calculator
btd converts a binary number to decimal while dtb converts a decimal number to binary.

## Functions

### btd binary to decimal
goes through the digits of b and adds the value (1 or 0) times 2 to the power of (the length of b minus the index minus 1)For example: If you pass the string "101", the first digit, 1, is multiplied by 2^(3-0-1 = 2) which is 1 to the power of 4. So 4 is added. Then the second digit is 0 so nothing is added. The third digit is 1 so, 2^(3-2-1=0) so 1 is added making it output 5.

### dtb decimal to binary
Does a for loop for 8 digits because the overflow is 256 so its an 8 bit binary number. It checks if the decimal number minus (2 to the power of (8 minus the index minus 1)) is less than zero, and if it is it adds a zero to the string, otherwise it adds a 1. 

### binary\_calculator
Checks if the set of bin2 is equal to a set of just zero and returns "NaN" if true.
checks if bin1 and bin2 have only 0s and 1s and returns "Error" if false by checking a set of the digits of bin1 and bin2 against a set of "0" and "1".
Calls btd on bin1 and bin2 does eval by doing dec1 + operator + dec2
checks if that answer is greater than 256 or less than 0 and returns "Overflow" if true.
returns the result of dtb(dec\_ans)

<!--

The following requirements must be met to receive full credit on this assignment. The calculator must handle binary arithmetic operations accurately while following proper error handling procedures and output formatting guidelines.

- Your solution must have a well-written and thorough README file.
- The solution must be implemented as a function called `binary_calculator()` with three parameters:
    - `bin1` - A string parameter representing the first binary number to be used in the calculation. Must contain only 0s and 1s.
    - `bin2` - A string parameter representing the second binary number to be used in the calculation. Must contain only 0s and 1s.
    - `operator` - A string containing one of the following arithmetic operators: `'+'`, `'-'`, `'*'`, or `'/'`
- Do not use Python's built-in `bin()` function.
- Implement your own binary-to-decimal and decimal-to-binary conversion logic.
- All binary inputs and outputs should be strings.
- Handle division by zero by returning `"NaN"`
- Handle decimal numbers by rounding down to the nearest whole number (flooring).
- Return `"Error"` for invalid binary inputs (containing characters other than `0` and `1`)
- Return `"Overflow"` for any operations that overflow (i.e. negative numbers, numbers greater than 8-bits).
- Outputs must be returned as 8-bit numbers (padded with leading zeros if necessary). For example, the decimal number `5` should be returned as `"00000101"` .

Your solution will be tested against various test cases including edge cases, invalid inputs, and all four arithmetic operations.

 -->
