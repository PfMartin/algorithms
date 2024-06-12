from sorter import Sorter


def main():
    l = [7, 3, 4, 6, 5, 8, 10, 1]

    sorter = Sorter()
    # print(sorter.selection_sort(l))
    print(sorter.insertion_sort(l))


main()
