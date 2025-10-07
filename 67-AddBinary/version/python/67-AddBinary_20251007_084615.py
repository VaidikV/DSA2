# Last updated: 10/7/2025, 8:46:15 AM
# simple binary addition which uses bin function already provided by python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        res = a + b
        return bin(res)[2:]