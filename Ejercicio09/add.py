archivo = open("test.txt", "a", encoding= "UTF-8")
for i in range (1048576):
    archivo.write("a")
archivo.close()