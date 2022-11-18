class Methods:
    def __init__(self):
        pass
    def degree(self, n, aList):
        degreeCount = 0
        for i in range(0, n, 1):
            if aList[i] == 1: 
                degreeCount += 1
            else: 
                while (aList[i] % 5 == 0): 
                    aList[i] = aList[i] // 5
                    if aList[i] == 1: 
                        degreeCount += 1
        return degreeCount

    def is_prime(self, n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


