
def get_input():
    with open("./input.txt") as f:
        return f.readlines()



def solve():
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


if __name__ == "__main__":
    solve()
