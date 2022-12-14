import os
import cv2

#onde pga o arquivo
path = "C:\\Users\\yasmi\\Desktop\\BYJUS\\Python\\c105\\Aluno\\PRO_1-1_C105_AtividadeDaProfessora4-main\\Images"

#onde vai salvar
images = []

#pega cada arquivo da pasta
for file in os.listdir(path):
    #separa o nome e a extensão, só pega arquivos de imagens
    name, ext = os.path.splitext(file)
    #só vai pegar a imagem se ela for esses formatos
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        #remonta o arquivo
        file_name = path+"/"+file
        # ve se o resultado tá correto
        #print(file_name)

        #cada arquivo está sendo add a lista   
        images.append(file_name)

#quantas imagens estão sendo adicionadas     
#print(len(images))
count = len(images)

# precisamos do tamanho 
frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
#print(size)

#criar um vídeo
out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

#Para o PÔR DO SOL
#for i in range(0,count-1):

#Para o NASCER DO SOL
# vai colocando cada frame pro video
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)
    
out.release() # liberando o vídeo gerado
print("Concluído")


