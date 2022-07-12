#Coded by Aman Dhiraj

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #map of 3x3 matrix
        A, B, C, D, E, F, G, H, I = [],[],[],[],[],[],[],[],[]
        subMatrixMap = {1:A, 2:B, 3:C , 4:D, 5:E, 6:F , 7:G, 8:H, 9:I}
    
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] != '.':
                    A.append(board[i][j])
        
        for i in range(0, 3):
            for j in range(3, 6):
                if board[i][j] != '.':
                    B.append(board[i][j])
                
        for i in range(0, 3):
            for j in range(6, 9):
                if board[i][j] != '.':
                    C.append(board[i][j])
                
        #second
        for i in range(3, 6):
            for j in range(0, 3):
                if board[i][j] != '.':
                    D.append(board[i][j])
        
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j] != '.':
                    E.append(board[i][j])
                
        for i in range(3, 6):
            for j in range(6, 9):
                if board[i][j] != '.':
                    F.append(board[i][j])
        #third
        for i in range(6, 9):
            for j in range(0, 3):
                if board[i][j] != '.':
                    G.append(board[i][j])
        
        for i in range(6, 9):
            for j in range(3, 6):
                if board[i][j] != '.':
                    H.append(board[i][j])
                
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j] != '.':
                    I.append(board[i][j])

        #row check 9x9
        vaildRow = {'1':0, '2':0, '3':0 , '4':0, '5':0, '6':0 , '7':0, '8':0, '9':0}
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] in vaildRow:
                    vaildRow[board[i][j]] += 1
                if j == 8:
                    for k in vaildRow:
                        if vaildRow[k] > 1:
                            return False
                    vaildRow = {'1':0, '2':0, '3':0 , '4':0, '5':0, '6':0 , '7':0, '8':0, '9':0}
        #col check 9x9
        vaildCol = {'1':0, '2':0, '3':0 , '4':0, '5':0, '6':0 , '7':0, '8':0, '9':0}
        for i in range(0,9):
            for j in range(0, 9):
                if board[j][i] in vaildCol:
                    vaildCol[board[j][i]] += 1
                if j == 8:
                    for k in vaildCol:
                        if vaildCol[k] > 1:
                            return False
                    vaildCol = {'1':0, '2':0, '3':0 , '4':0, '5':0, '6':0 , '7':0, '8':0, '9':0}
        #check freq 3x3
        for i in subMatrixMap:
            x = Counter(subMatrixMap[i])
            for j in x:
                if x[j] > 1:
                    return False
        return True
            
                    
        