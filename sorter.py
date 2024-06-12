class Sorter:
  def swap_elements(self, list: list, first: int, second: int) -> None:
    (list[first], list[second]) = (list[second], list[first])

  def selection_sort(self, list: list) -> list:
    for current_idx in range(len(list)):
      min_idx = current_idx

      for i in range(current_idx + 1, len(list)):
        if list[i] < list[min_idx]:
          min_idx = i

      self.swap_elements(list, current_idx, min_idx)
      
    return list