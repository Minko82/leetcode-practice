# 🧮 Greatest Common Divisor of Strings

##  📝 Problem Statement:
Given two strings `str1` and `str2`, return the largest string `X` such that:
- `X` is a divisor of both `str1` and `str2`.
- That is, `str1 = X * n` and `str2 = X * m` for some positive integers `n` and `m`.

<br>

---



## 🔍 Example Outputs

| **Input**                     | **Output** | **Explanation**                                                                 |
|-------------------------------|------------|---------------------------------------------------------------------------------|
| `str1 = "ABABAB"`, `str2 = "ABAC"` | `""`       | No common divisor string exists between the two inputs.                        |
| `str1 = "ABCABC"`, `str2 = "ABC"`  | `"ABC"`    | `"ABC"` is the greatest string that divides both inputs.                       |
| `str1 = "LEET"` , `str2 = "CODE"`  | `""`       | No common divisor string exists as the two inputs share no repeating patterns. |

<br>

---

## 🧠 Solution Explanation

The goal of the solution is to find the **greatest common divisor (GCD)** of two strings, meaning the largest string that can evenly divide both strings.

### How it Works:

1. **Find the Shorter String**:
   We start by identifying the shorter string between the two inputs since the GCD cannot be longer than the shorter string.

2. **Try Possible Divisors**:
   Starting from the full shorter string, we test every possible substring (from longest to shortest) as a potential divisor.

3. **Check if the Divisor Works**:
   
   For each potential divisor:
   - Calculate how many times the divisor would need to repeat to form `str1` and `str2`.
   - Check if repeating the divisor the required number of times equals `str1` and `str2`.

5. **Return the First Match**:
   As soon as we find a divisor that works for both strings, we return it. If no such divisor exists, we return an empty string (`""`).

### Example:

Input: `"ABABAB"` and `"ABAB"`

- Start with `"ABAB"`, the shorter string.
- Check if repeating `"ABAB"` (1 time for `str2`, 1.5 times for `str1`) equals the original strings. It doesn't work.
- Next, try `"AB"`.
- Repeating `"AB"` (3 times for `str1`, 2 times for `str2`) matches both strings.
- Return `"AB"`.

Input: `"ABABAB"` and `"ABAC"`

- Start with `"ABAC"`, the shorter string.
- Check all substrings of `"ABAC"`. None can divide both strings evenly.
- Return `""`.


---


