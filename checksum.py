def checksum(input):

        card = list(input.strip())
        check = card.pop()
        card.reverse()

        numbers = []

        for index, num in enumerate(card):
            if index % 2 == 0:
                double_num = int(num) * 2
                if double_num > 9:
                    double_num = double_num - 9
                numbers.append(double_num)
            else:
                numbers.append(int(num))

        total = int(check) + sum(numbers)

        if total % 10 == 0:
            return "Yes"
        else:
            return "No"


N = int(input())
for i in range(N):
    print(checksum(input()))


