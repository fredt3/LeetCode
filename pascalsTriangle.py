class Solution:
    def generate(self, numRows):
        triangle = []
        if(numRows == 0):
            return triangle
        row = [1]
        triangle.append(row)

        for i in range(1, numRows):
            newRow = [1]
            for j in range(1, i):
                newRow.append(triangle[i-1][j-1]+triangle[i-1][j])
            newRow.append(1)
            triangle.append(newRow)

        return triangle


print(Solution().generate(5))
