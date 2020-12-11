def maxSubstring(s):
    character = []
    unique = []
    for i in range(len(s)):
        character.append(s[i])
    max_list = max(character)
    for i in range(len(character)):
        if character[i] == max_list:
            max_substring = max_list
            for j in range(i + 1, len(character)):
                max_substring += character[j]
            unique.append(max_substring)

    return max(unique)

print(maxSubstring("abcdefzadsfjkhgjkb"))