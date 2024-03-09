import copy
happy_words = [
    "Joy".upper(),
    "Yes".upper(),
    "Win".upper(),
    "Fun".upper(),
    "Ace".upper(),
    "Top".upper(),
    "Pro".upper(),
    "Awe".upper(),
    "Gem".upper(),
    "Can".upper(),
    "Sun".upper(),
    "happy".upper(),
]

def findHappyWords(lette):
    coords = []
    coo_let = []
    temp_coord = []
    letters = copy.deepcopy(lette)
    # print(lette)
            
    for word in happy_words:
        wor = ""
        letep = copy.deepcopy(letters)
        for i in range(len(letep)):
            for j in range(len(letep[i])):
                # if len(word) > 0:
                    for lett in word:
                        if ((letep[i][j].upper() == lett) and ((letep[i][j].upper() not in wor))):
                            # print("hi")
                            wor += letep[i][j].upper()
                            temp_coord.append([i, j])

                            letep[i][j] = ""
                        elif((letep[i][j].upper() == lett) and (letep[i][j].upper() in wor) and (letep[i][j].upper() == "P".upper())):
                            if(len(word) > len(wor)):
                                wor += letep[i][j].upper()
                                temp_coord.append([i, j])
                                # print(letep[i][j])

                                letep[i][j] = ""
                                # print(wor)
        
        # print(temp_coord)
    
        if(len(word) == len(wor)):
            print(word)
            for coo in temp_coord:
                coords.append(coo)
                ey = coo[0]
                jay = coo[1]
                # print("ey: " + str(ey))
                # print("jay: " + str(jay))
                
                # print(letters[ey][jay])
                coo_let.append(letters[ey][jay])
                letters[ey][jay] = ""
            temp_coord = []
        else:
            temp_coord = []

    
    
    
                        # if len(word) > 1:
                        #     if j + len(word) <= len(letters[i]):
                        #         if letters[i][j + 1].upper().startswith(word[1]):
                        #             if len(word) > 2:
                        #                 if j + len(word) <= len(letters[i]):
                        #                     if letters[i][j + 2].upper().startswith(word[2]):
                        #                         coords.append((i, j))
                        #                         print(word)
                        #             else:
                        #                 coords.append((i, j))
                        #                 print(word)
                                
    print(coords)
    print(coo_let)
    # print(lette)
    return coords
