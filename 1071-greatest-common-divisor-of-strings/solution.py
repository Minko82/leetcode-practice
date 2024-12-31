def gcdOfStrings(str1: str, str2: str) -> str:
    shorter_string = min(str1, str2)

    divisor = ''

    for i in range(len(shorter_string)):
        divisor = shorter_string[:len(shorter_string)-i]
        str1_factor =  len(str1) // len(divisor)
        str2_factor =  len(str2) // len(divisor)

        if (divisor * str1_factor) == str1 and (divisor * str2_factor) == str2:
            return divisor
        
    return ""

print(gcdOfStrings("ABABAB", "ABAC"))