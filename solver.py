def definir_problema():
    
    problema= [

        [7, 0, 8, 0, 9, 0, 5, 0, 0 ],
        [0, 0, 0, 7, 3, 0, 0, 1, 9 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [2, 0, 0, 0, 0, 0, 6, 0, 0 ],
        [0, 0, 6, 9, 0, 4, 8, 0, 0 ],
        [0, 0, 5, 0, 0, 0, 0, 0, 1 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [4, 8, 0, 0, 5, 7, 0, 0, 0 ],
        [0, 0, 9, 0, 6, 0, 1, 0, 3 ],
    ]

    for linha in problema:
        for i,numero in enumerate(linha):
            if numero!=0:
                linha[i]=str((numero))

    return problema

def checar_possiveis_comeco(linha):
    numeros_possiveis={1,2,3,4,5,6,7,8,9}
    
    for j,numero in enumerate(linha):
        if numero!=0 and int(numero) in numeros_possiveis:
            numeros_possiveis.remove(int(numero))
    return numeros_possiveis

def checar_coluna(problema,posicao,numeros_possiveis):
    for linha in problema:
        if int(linha[posicao]) in numeros_possiveis:
            numeros_possiveis.remove(int(linha[posicao]))
    return numeros_possiveis

def checar_linha_quadrado(problema,y,yy,x,xx,numeros_possiveis):
    for linha in problema[x:xx+1]:
                for numero in linha[y:yy+1]:
                    if int(numero) in numeros_possiveis:
                        numeros_possiveis.remove(int(numero))
    return numeros_possiveis
def checar_coluna_quadrado(problema,pos_linha,y,yy,numeros_possiveis):
    if 0<=pos_linha<=2:
        return checar_linha_quadrado(problema,y,yy,0,2,numeros_possiveis)
    
    if 3<=pos_linha<=5:
        return checar_linha_quadrado(problema,y,yy,3,5,numeros_possiveis)

    if 6<=pos_linha<=8:
        return checar_linha_quadrado(problema,y,yy,6,8,numeros_possiveis)

def checar_quadrado(problema,pos_linha,pos_coluna,numeros_possiveis):
    if 0<=pos_coluna<=2:
        return checar_coluna_quadrado(problema,pos_linha,0,2,numeros_possiveis)
    
    if 3<=pos_coluna<=5:
        return checar_coluna_quadrado(problema,pos_linha,3,5,numeros_possiveis)

    if 6<=pos_coluna<=8:
        return checar_coluna_quadrado(problema,pos_linha,6,8,numeros_possiveis)
        



def resolver(problema):
    vdd=True
    possibilidades={}
    while vdd:
        vdd=False
        for i,linha in enumerate(problema):
            for j, numero in enumerate(linha):
                if numero==0:
                    numeros_possiveis=checar_possiveis_comeco(linha)
                    numeros_possiveis=checar_coluna(problema,j,numeros_possiveis)
                    numeros_possiveis=checar_quadrado(problema,i,j,numeros_possiveis)
                    possibilidades[str(i)+str(j)]=numeros_possiveis
                    if len(list(numeros_possiveis))==1:
                        vdd=True
                        problema[i][j]=str(list(numeros_possiveis)[0])
        
                    


def main():
    problema=definir_problema()
    resolvido=resolver(problema)
    for linha in problema:
        for i, numero in enumerate(linha):
            linha[i]=int(numero)
        print(linha)
main()