


def get_input():
    with open("./input.txt") as f:
        return f.readlines()




def solve2():
    calories = get_input()
    top=3
    total_calories = []
    sum=0
    for i in range(len(calories)):
        if(i==len(calories)-1 or calories[i]=="\n"):
            if (i==len(calories)):
                sum+=int(calories[i].replace("\n", ""))
            total_calories.append(sum)
            sum=0
        else:
            sum+=int(calories[i].replace("\n", ""))
    total_calories.sort(reverse=True)
    answer = 0
    for i in range(top):
        answer+=total_calories[i]
    print(answer)


def solve1():
    calories = get_input()
    elf_max = 1
    current_elf = 1
    sum = 0
    maximum = 0
    for i in range(len(calories)):
        if (i==len(calories)-1 or calories[i]=="\n"):
            if(i==len(calories)-1):
                sum+=int(calories[i].replace("\n", ""))
            if sum > maximum:
                maximum = sum
                elf_max = current_elf
            # reset counter
            sum=0
            # go ahead with elf
            current_elf+=1
        else:
            sum+=int(calories[i].replace("\n", ""))
    print("The ", elf_max, " elf is carrying the most calories, total of ", maximum, " calories")


if __name__ == "__main__":
    solve1()
    solve2()
