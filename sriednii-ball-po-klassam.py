def main():
    grades = [[] for i in range(3)]
    with open("input.txt", "r", encoding='utf8') as lines:
        for line in lines:
            lastName, name, grade, score = line.strip().split(" ", maxsplit=4)
            grade, score = int(grade) - 9, int(score)
            grades[grade].append(score)
        for scores in grades:
            print(sum(scores) / len(scores), end=" ")


if __name__ == "__main__":
    main()
