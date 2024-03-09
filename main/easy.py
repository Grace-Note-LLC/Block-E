import easyocr
reader = easyocr.Reader(['ch_sim','en'])
result = reader.readtext('images/diffA.jpg')
print(result)