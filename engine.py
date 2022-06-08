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

    daiane1 = reconhece_face("./img/daiane1.png")
    if(daiane1[0]):
        rostos_conhecidos.append(daiane1[1][0])
        nomes_dos_rostos.append("Daiane")
    
    return rostos_conhecidos, nomes_dos_rostos