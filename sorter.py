class Sorter:
    def swap_elements(self, list: list[int], first: int, second: int) -> None:
        (list[first], list[second]) = (list[second], list[first])

    def selection_sort(self, list: list[int]) -> list[int]:
        for current_idx in range(len(list)):
            min_idx = current_idx

            for i in range(current_idx + 1, len(list)):
                if list[i] < list[min_idx]:
                    min_idx = i

            self.swap_elements(list, current_idx, min_idx)

        return list

    def insertion_sort(self, list: list[int]) -> list[int]:
        for i in range(1, len(list)):
            j = i

            while j and list[j - 1] > list[j]:
                self.swap_elements(list, j, j - 1)
                j = j - 1

        return list
