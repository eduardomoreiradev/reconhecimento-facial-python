import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    eduardo1 = reconhece_face("./img/eduardo1.png")
    if(eduardo1[0]):
        rostos_conhecidos.append(eduardo1[1][0])
        nomes_dos_rostos.append("Eduardo")

    henrique1 = reconhece_face("./img/henrique1.png")
    
    
    if(henrique1[0]):
        rostos_conhecidos.append(henrique1[1][0])
        nomes_dos_rostos.append("Henrique")
        


        bruno1 = reconhece_face("./img/bruno1.png")
    if(bruno1[0]):
        rostos_conhecidos.append(bruno1[1][0])
        nomes_dos_rostos.append("Bruno Okazava")
    
        rodrigo1 = reconhece_face("./img/rodrigo1.png")
    if(rodrigo1[0]):
        rostos_conhecidos.append(rodrigo1[1][0])
        nomes_dos_rostos.append("Rodrigo")


    return rostos_conhecidos, nomes_dos_rostos