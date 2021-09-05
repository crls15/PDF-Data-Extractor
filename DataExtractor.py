import slate3k as slate
import pathlib

idList=["SUBDISTRITO","CLAVE CATASTRAL","ZONIFICACIÓN","UBICACIÓN","SUPERFICIE EN CARTOGRAFÍA","SUPERFICIE LEGAL","SUPERFICIE EDIFICADA","SUPERFICIE DE DESPLANTE","COS","CUS","SUPERFICIE MÁXIMA PERMITIDA POR COS","SUPERFICIE MÁXIMA PERMITIDA POR CUS"]
generalList=[]

def synCor(Obj):
    for i in range(len(Obj)):
        if "m²" in Obj[i]:
            m=Obj[i].split(" ")
            Obj[i]=m[0]
    return Obj 


def isInidList(id):
    if id in idList:
        return True
    else:
        return False

def get_info(path):
    with open(path,'rb') as f:
        pageText = slate.PDF(f)
    texto=str(pageText)
    listaDataG=texto.split("\\n")
    rowList=[]
    
    cont=0
    cantID=len(idList)
    idCont=0
    
    while cont<=len(listaDataG):
        if cont == 0:
            cont=cont+2
            rowList.append(listaDataG[cont])
        elif isInidList(listaDataG[cont]):
            rowList.append(listaDataG[cont+2])
            cont=cont+1
            idCont=idCont+1       
        elif idCont>=cantID:
            break
        else:
            cont=cont+1

    rowList=synCor(rowList)
    row=",".join(rowList)
    return row+"\n"
       

def loopFromDir(path):
    listFiles =list( pathlib.Path(path).glob('*.pdf'))
    for fileName in listFiles:
       
       mapKeys =get_info(fileName)
       generalList.append(mapKeys)
 
    return generalList

def writeData(path):
    if _name_ == '_main_':
        Data= loopFromDir(path)

    f = open("DataSantaTere.txt","w")

    f.writelines(Data)
    f.close()



path = '/home/carlosfl/Desktop/Programacion/Proyecto de Probabilidad/PDFs Santa Tere/' #Incerte direccion de la carpeta de los PDFs
writeData(path)