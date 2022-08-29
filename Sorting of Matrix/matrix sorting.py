#funtion of matrix input from nested lists
def inputmatrix (matrix):
    for i in range(len(matrix)):
        j=0
        for j in range(len((matrix)[j])):
            unsortedmatrix.append(matrix[i][j])
    return unsortedmatrix

#funtion of sorting
def srt (unsortedmatrix):
    for k in range (len(unsortedmatrix)):
        for l in range (k+1, len(unsortedmatrix)):
            if unsortedmatrix[k] > unsortedmatrix[l]:
                pseudo = unsortedmatrix[l]
                unsortedmatrix[l] = unsortedmatrix[k]
                unsortedmatrix[k] = pseudo
    return unsortedmatrix

"_______________________________________MAIN PROGRAM_______________________________________"

#main program
matrix=[[9,8,5],[7,1,2],[4,3,6]]
Sortedmatrix=[]
unsortedmatrix=[]
inputmatrix(matrix)
print(f"Unsortedmatrix: {unsortedmatrix}")
srt(unsortedmatrix)
print(f"Sortedmatrix:   {unsortedmatrix}")
    
