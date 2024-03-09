import splitter as sp
import simple
import imageTaker as iT
import gridOverlay as grid
import threading
import wordFinder as wf


def helpME():
    iT.take()
    sp.tile("./blockImage/big.jpg")
    letters = simple.OCR()
    print(letters)
    # letters = [['', 'DS', '', 'OO', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', 'A', '', 'E', 'PN', 'WW', '', 'SN'], ['', '', 'E', 'G', 'A', 'U', '', '', 'ON'], ['', '', 'C', 'YY', 'TO', 'S', 'P', '', ''], ['', '', 'R', 'O', 'MM', 'C', 'NX', '', ''], ['', 'SY', 'S', '', 'VV', 'P', 'H', '', 'A'], ['', '', '', '', '', '', '', '', 'G']]
    grid.main(letters)
    # print("he")
    # print("ho")

    return letters


def main():
    letters = helpME()
    # iT.take()
    sp.tile("./blockImage/big2.jpg")
    letters2 = simple.OCR()
    print(letters2)
    grid.main(letters2)

    common_letters = []
    for i in range(len(letters)):
        common_row = []
        for j in range(len(letters[i])):
            if letters[i][j] == letters2[i][j]:
                if(len(letters[i][j]) > 0):
                    common_row.append(letters[i][j][0:1])
                else:
                    common_row.append(letters[i][j])
            else:
                if(len(letters[i][j]) > 0):
                    common_row.append(letters[i][j][0:0])
                
                elif (len(letters2[i][j]) > 0):
                    common_row.append(letters2[i][j][0:0])
                else:
                    common_row.append(letters[i][j])
                
        common_letters.append(common_row)
   
    # print("\n")
    # print(common_letters)
    # common_letters = [['', '', '', '', '', '', '', '', ''], ['A', '', 'H', 'A', 'P', 'P', 'Y', '', ''], ['', '', 'A', 'E', 'E', 'N', 'W', '', 'N'], ['', 'J', 'Y', 'G', 'L', 'U', 'F', '', 'A'], ['', 'O', '', 'Y', 'T', 'S', 'P', '', ''], ['', 'Y', 'I', 'O', 'M', 'C', 'A', '', 'D'], ['', '', 'S', 'S', 'K', 'P', 'H', '', 'A'], ['', '', '', '', '', 'C', 'F', 'J', 'G']]
    grid.main(common_letters)

    coords = wf.findHappyWords(common_letters)

    # print(coords)


    

if __name__ == "__main__":
    main()

