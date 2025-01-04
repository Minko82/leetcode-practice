# 🧮 1071. Greatest Common Divisor of Strings

<img width="738" alt="Screenshot 2025-01-04 at 1 28 03 PM" src="https://github.com/user-attachments/assets/514d0eb2-9b12-4e08-8241-c3a9c297c852" />


##  📝 Problem Statement:
Given two strings `str1` and `str2`, return the largest string `X` such that:
- `X` is a divisor of both `str1` and `str2`.


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

1. **Find the Shorter String**:

   Because the GCD cannot be longer than the shorter string.

3. **Try Possible Divisors**:

    Starting from the full shorter string, test every possible substring (from longest to shortest) as a potential divisor.

5. **Check if the Divisor Works**:
   
   For each potential divisor:
   - Calculate how many times the divisor would need to repeat to form `str1` and `str2`.
   - Check if repeating the divisor the required number of times equals `str1` and `str2`.

6. **Return the First Match**:
   
   As soon as we find a divisor that works for both strings, we return it. If no such divisor exists, we return an empty string (`""`).
   
 <br>
 
   #### Example: (✿◠‿◠)

      Input: `"ABABAB"` and `"ABAB"`

      - Start with `"ABAB"`, the shorter string.
      - Check if repeating `"ABAB"` (1 time for `str2`, 1.5 times for `str1`) equals the original strings. It doesn't work.
      - Next, try `"AB"`.
      - Repeating `"AB"` (3 times for `str1`, 2 times for `str2`) matches both strings.
      - Return `"AB"`.

<br>

---

## ✨ Notes:

### - String Slicing (`[:n]`)

   The syntax `[:n]` is a **slice operation** in Python used to extract a portion of a string (or list, tuple, etc.). Here's how it works:
      
      
   #### **How `[:n]` Works:**
   When you write `[:n]`:
         
   - start is not specified, so Python starts at the beginning of the string (index 0).
   - end is n, so Python stops at index n (but doesn’t include it).
            
      Thus, `[:n]` extracts the first n characters of the string.
     
       <br>
       
   #### Example: (✿◠‿◠)
   Let’s say my_string = "HELLO":
      
         my_string[:3]
         # Starts at index 0, stops at index 3 (excludes index 3)
         # Result: "HEL"
      
         my_string[:1]
         # Starts at index 0, stops at index 1
         # Result: "H"
