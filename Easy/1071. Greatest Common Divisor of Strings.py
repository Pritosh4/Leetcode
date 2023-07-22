class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        l1, l2 = len(str1), len(str2)

        def check(i):
            substr = str1[:i]
            l = len(substr)
            if l1 % l != 0 or l2 % l != 0:
                return False
            s1 = l1 // l
            s2 = l2 // l
            return substr * s1 == str1 and substr * s2 == str2 

        for i in range(min(l1, l2), 0, -1):
            if check(i):
                return str1[:i]
        return ''
        '''
        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b % a, a)

        if str1 + str2 != str2 + str1:
            return ''
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]
          
