class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_list = []
        for i in operations:
            if i == "+":
                new_list.append(new_list[-1] + new_list[-2])
            elif i == "C":
                new_list.pop()
            elif i == "D":
                new_list.append(new_list[-1] * 2)
            else:
                new_list.append(int(i))
        return sum(new_list)
