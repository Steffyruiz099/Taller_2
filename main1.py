from imageShape import *

width = int(input('ingrese el ancho de la imagen'))         # se pide el ancho de la imagen
height = int(input('ingrese el alto de la imagen'))         # se pide el alto de la imagen
im = imageShape(width,height)                               # se crea un objeto en la clase
im.generateShape()                                          # se llama el método generateShape
im.showShape()                                              # se llama el método showShape
im.getShape()                                               # se llama el método getShape
im.whatShape()                                              # se llama el método whatShape