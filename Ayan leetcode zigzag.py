def Convert(s, rownum):
    if rownum == 1:
        print(s)
    else:
        Array = [[""] *len(s) for i in range(rownum)]
        OgCount = 0
        Total = len(s)
        ColPlacer = -1
        a = 0

        while OgCount != Total:
            ColPlacer = ColPlacer + 1

            for loop in range(rownum):
                if OgCount != Total:
                    Place = s[a: a+1]
                    a = a + 1
                    OgCount = OgCount + 1
                    Array[loop][ColPlacer] = Place

            for index in range(rownum-2, 2-2, -1):
                if OgCount != Total:
                    ColPlacer = ColPlacer + 1
                    Place = s[a: a+1]
                    a = a + 1
                    OgCount = OgCount + 1
                    Array[index][ColPlacer] = Place

        Concatenate = ""

        for row in range(rownum):
            for col in range(Total):
                Concatenate = Concatenate + Array[row][col]
        print(Concatenate)
        
Convert("PAYPALISHIRING",4)
Convert("Ayansheeraz",5)
