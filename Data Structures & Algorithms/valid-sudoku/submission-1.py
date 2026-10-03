class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0]*9
        cols = [0]*9
        boxes = [0]*9

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue

                val = int(board[r][c])-1
                box_num = ((r//3)*3) + (c//3)

                ## (1 << val) is a mask for that specific val

                if (1 << val) & rows[r]: ## non zero is true
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & boxes[box_num]:
                    return False
                
                ## use bitwise-OR to mark the digit presence(think of numbers in 8 bit binary)
                rows[r] = (1 << val) | rows[r]
                cols[c] =  (1 << val) | cols[c]
                ## r_b = {(0,1,2):[0,1,2], (3,4,5):[3,4,5], (6,7,8):[6,7,8]}
                ## c_b = {(0,1,2):[0,3,6], (3,4,5):[1,4,7], (6,7,8):[2,5,8]}
                ## boxes_coordinates = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)]] => how do they give the box number? : ((r//3)*3) + (c//3)
                boxes[box_num] =  (1 << val) | boxes[box_num]
        return True