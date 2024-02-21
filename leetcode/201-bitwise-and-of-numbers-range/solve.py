class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0:
            return 0
        leftBin = "{0:b}".format(left)
        rightBin = "{0:b}".format(right)
        leftBin = leftBin.rjust(len(rightBin), '0')
        leftFirst = leftBin.find('1')
        rightFirst = rightBin.find('1')
        ansBin = ''
        if leftFirst != rightFirst:
            return 0
        leftBin = leftBin[leftFirst:]
        rightBin = rightBin[rightFirst:]
        mismatched = False
        for i, char in enumerate(rightBin):
            if mismatched:
                ansBin += '0'
            elif char == leftBin[i]:
                ansBin += char
            else:
                ansBin += '0'
                mismatched = True
        return int(ansBin, 2)

        