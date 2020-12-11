def scrapping(input):
    new_text = ""
    flag = 0
    for i in range(len(input)):

        if flag == 0:
            if input[i] == "<" and i != len(input) - 1 and input[i + 1] == "s":
                flag = 2
            else:
                new_text += input[i]

        if flag == 2 or flag == 1:
            if input[i] == '>':
                flag -= 1

    return new_text


text = ""
while True:
    try:
        x = input()
        if x:
            text += x
        else:
            break
    except EOFError as e:
        break
            
print(scrapping(text))
