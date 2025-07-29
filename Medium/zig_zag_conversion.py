class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        strs = [''] * numRows
        current_row = 0
        going_down = False

        for letter in s:
            strs[current_row] += letter

            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            if going_down:
                current_row += 1
            else:
                current_row -= 1
        
        return ''.join(strs)

obj = Solution()
s = "PAYPALISHIRING"
print(obj.convert(s, 3))
