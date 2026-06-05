class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for number in range(max(101,num1), num2 + 1):
            lst = []
            while number > 0:
                lst.append(number % 10)
                number //= 10
            digits = len(lst)
            for i in range(1, digits - 1):
                if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
                    print(lst)
                    res += 1
                elif lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
                    print(lst)
                    res += 1
        return res
            
        