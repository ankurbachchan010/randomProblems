def palindrome(int1, count):
    rev = "".join(reversed(int1))
    sum1 = int(int1) + int(rev)
    revsum = int(str(sum1)[::-1])
    if count < 100:
        if sum1 == revsum:
            print(sum1)
        else:
            count += 1
            palindrome(str(sum1), count)
    else:
        print("Palindrome not exist ")


count = 0
palindrome(str(195), count)
