def mergeAlternately(word1: str, word2: str) -> str:
    minLen = min(len(word1), len(word2))
    result = ""

    for i in range(minLen):
        result += word1[i] + word2[i]
        i += 1

    # Print the rest of the string
    result += word1[minLen:] + word2[minLen:]

    return result

print(mergeAlternately("ABABAB", "ABAC"))