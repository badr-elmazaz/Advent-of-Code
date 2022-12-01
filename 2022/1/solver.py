


def get_input():
    with open("./input.txt") as f:
        return f.readlines()




def solve():
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
    solve()
