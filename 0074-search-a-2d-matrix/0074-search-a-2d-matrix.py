class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # [[1,3]]
        # 1
        # 3
        # 1 3
        flag = False
        for row in matrix:
            l, r = 0, len(row) - 1
            print(row[l], row[r])
            while l <= r:
                m = l + ((r - l) // 2)
                print(row[m])
                if row[m] > target:
                    r = m - 1
                elif row[m] < target:
                    l = m + 1
                else:
                    flag = True
                    break
                

        return flag
        
