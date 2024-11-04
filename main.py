from LinkedList.SingleLinkedList import SingleLinkedList
from ProblemStatement.Array.ArrayProblems import ArrayProblems

def solve_array_problems():
    arr = ArrayProblems()
    answer = arr.TwoSums([3,2,4], 6)
    print(f"answer is {answer}")


def link_list_implementations():
    linkedNode = SingleLinkedList()
    linkedNode.push(23)
    linkedNode.push(24)
    linkedNode.push(25)

def main():
    print("\n DATA STRUCTURE CLASS")
    solve_array_problems()


if __name__ == '__main__':
    main()
