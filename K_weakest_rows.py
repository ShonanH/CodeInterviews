class Solution:
    def kWeakestRows(mat):
        counter1 = 0
        counter0 = 0
        new_arr = []
        for i in range (len(mat)):
            #print(mat[i])
            for j in range (len(mat[i])):
                print(mat[i])
                if mat[i][j] == 1:
                    counter1 += 1
                elif mat[i][j] == 0:
                    counter0 += 1
        #print(counter1)
    kWeakestRows([[1,1,0,0,0],
                 [1,1,1,1,0],
                 [1,0,0,0,0],
                 [1,1,0,0,0],
                 [1,1,1,1,1]])