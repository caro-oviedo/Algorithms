class Matrix:
    rows = 0
    columns = 0

    matrix = []
    matrixRow = []

    dataCount = 0
    matrixList = []
    tempProduct = 0

    def __init__(self, rows, columns, data = []):
        if data == []:
            data = [None] * (rows * columns)
        self.matrix = []
        self.rows = rows
        self.columns = columns 

        for i in range(rows):
            self.matrixRow = []
            for j in range(columns):
                self.matrixRow.append(data[self.dataCount])
                self.dataCount += 1
            self.matrix.append(self.matrixRow)

    def __getItem__(self, index):
        return self.matrix[index]



listAux = list(range(6))
print(listAux)

myMatrix = Matrix(2,3,listAux)
print(myMatrix.matrix)
print(myMatrix.matrix[1])
print(myMatrix.matrix[1][2])
print(myMatrix.__getItem__(1))
