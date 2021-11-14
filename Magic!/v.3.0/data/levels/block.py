#Importações
import pyxel

#Função colocar blocos
def DrawBlock(x, y, posx, posy, quant):
    x = -32
    
    #Loop para colocar os blocos mais de uma vez
    for _ in range(quant):
        x +=16

        #mostrar o bloco na tela
        pyxel.blt(x +16, y, 1, posx, posy, 16, 16)