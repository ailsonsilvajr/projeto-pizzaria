from barcode import EAN13
from barcode.writer import ImageWriter 

codigo_de_barra = EAN13("123123123123")
codigo_de_barra.save("codigo_barra")
