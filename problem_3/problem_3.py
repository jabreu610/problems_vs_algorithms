class MaxHeap:
    def __init__(self, init = []):
        self.d = []
        for element in init:
            self.push(element)

    def is_empty(self):
        return len(self.d) == 0

    def get_children_index(self, index):
        return 2 * index + 1, 2 * index + 2

    def get_parent_index(self, index):
        return (index - 1) // 2

    def heapify_up(self):
        if len(self.d) < 2:
            return

        curr = len(self.d) - 1
        parent = self.get_parent_index(curr)

        while self.d[curr] > self.d[parent] and curr > 0:
            self.d[curr], self.d[parent] = self.d[parent], self.d[curr]
            curr = parent
            parent = self.get_parent_index(curr)

    def heapify_down(self):
        if len(self.d) < 2:
            return
        curr = 0
        left, right = self.get_children_index(curr)
        last_index = len(self.d) - 1
        while curr < last_index and (left <= last_index or right <= last_index):
            curr_val = self.d[curr]
            left_val = self.d[left] if left <= last_index else float('-inf')
            right_val = self.d[right] if right <= last_index else float('-inf')
            swap_required = curr_val < left_val or curr_val < right_val
            if not swap_required:
                break
            if left_val > right_val:
                self.d[curr], self.d[left] = self.d[left], self.d[curr]
                curr = left
            else:
                self.d[curr], self.d[right] = self.d[right], self.d[curr]
                curr = right
            left, right = self.get_children_index(curr)

    def push(self, element):
        self.d.append(element)
        self.heapify_up()

    def pop(self):
        if len(self.d) == 0:
            raise IndexError("heap is empty")
        if len(self.d) == 1:
            return self.d.pop()
        self.d[0], self.d[-1] = self.d[-1], self.d[0]
        result = self.d.pop()
        self.heapify_down()
        return result

def rearrange_digits(input_list):
    """Rearrange Array Elements so as to form two number such that their sum is maximum."""
    input_length = len(input_list)
    heap = MaxHeap(input_list)
    if input_length < 2:
        ans = []
        while not heap.is_empty():
            ans.append(heap.pop())
        return ans

    is_even = input_length % 2 == 0
        
    ans_a = ''
    ans_b = ''

    if not is_even:
        ans_a += f"{heap.pop()}"

    current_index = 0
    while not heap.is_empty():
        element_str = f"{heap.pop()}"
        if current_index % 2 == 0:
            ans_a += element_str
        else:
            ans_b += element_str
        current_index += 1

    return [int(ans_a), int(ans_b)]
    


if __name__ == "__main__":
    print(rearrange_digits([1, 2, 3, 4, 5]) == [542, 31])
    # True
    print(rearrange_digits([4, 6, 2, 5, 9, 8]) == [964, 852])
    # True
    print(rearrange_digits([]) == [])
    # True
    print(rearrange_digits([1]) == [1])
    # True
    print(rearrange_digits([1, 2]) == [2, 1])
    # True
