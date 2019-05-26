############################################################
##### ALUNOS: LEONARDO MARCO, MARIA CLARA, MARIANE LUIZA####
############################################################

# import libraries
import cv2
import face_recognition

imagem = cv2.imread('imagem/tom.jpg')
imagem2 = cv2.imread('imagem/red.jpg')

face_encoding = face_recognition.face_encodings(imagem)[0]
face_encoding2 = face_recognition.face_encodings(imagem2)[0]

faces_conhecidas = [
    face_encoding,
    face_encoding2
]

video = cv2.VideoCapture("video/video.mp4")

face_locations = []

fps = video.get(cv2.CAP_PROP_FPS)
count = 0

while True:
    ret, frame = video.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []


    for face_encoding in face_encodings:
        # Compara a imagem de busca com todos os rostos existentes na imagem atual.
        match = face_recognition.compare_faces(faces_conhecidas, face_encoding, tolerance=0.50)
        
        count += 1
        time = count/fps
        minutes = int(time/60)
        seconds = time%60

        name = None
        if match[0]:
            name = "Tom"
            print('Tom aparece em:' + str(minutes) + ':' + str(seconds) + ' segundos')
        elif match[1]:
            name = "Red"
            print('Red aparece em:' + str(minutes) + ':' + str(seconds) + ' segundos')

            
        
        face_names.append(name)
    
    #Aplica a label nas faces encontradas
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        #Desenha um retangulo  em torno da face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 127, 255), 2)

        #Inclui o nome da face identificada
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 127, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)


    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()