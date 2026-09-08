class Solution:
    def countCommas(self, n: int) -> int:
        l = len(str(n))
        i = 1
        count = 0
        while i * 3 < l:
            count += n-pow(10,i*3)+1
            i += 1
        return count