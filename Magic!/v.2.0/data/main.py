#importações
import pyxel
from components import  player
from levels import block, button, item, mob

class Game:
    def __init__(self) -> None:
        #configurando a tela
        self.window_x, self.window_y = 100,100
        pyxel.init(self.window_x, self.window_y, caption="Magic!", fullscreen= True)
        
        #importando recursos
        #iniciando musica
        #atualiza funçôes enquanto o código estiver sendo rodando
        pyxel.load('components/resources/magic.pyxres')
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    #Função de verificação 
    def update(self):
        #Movimentação do player
        player.Player1.Move()
        player.Player1.Collision()
        
        #verificando açoes com os itens
        item.Mushroom.Collision()
        item.Coin.Collision()
        item.staff.Collision()
        mob.Goblin.Move()

        #verificando interação com os botões
        #se pressionar o botão play:
        if button.ButtonPlay.PressButton():
            button.ButtonPlay.button= True
            button.ButtonPlay.pos_y= -16
            button.ButtonPlay.img_x = 16

        else:
            button.ButtonPlay.pos_y= 43
            button.ButtonPlay.img_x = 0

        #se o player morrer
        if player.Player1.life <= 0:
            #move o botão para o centro da tela
            button.ButtonHome.pos_y=47
            button.ButtonHome.img_x = 16
   

            #se pressionar o botão home:
            if button.ButtonHome.PressButton():
                #voltar ao menu inicial
                button.ButtonPlay.button= False
                button.ButtonHome.pos_y= -16

                #resentando Tudo
                #resetando player
                player.Player1.life =3
                player.Player1.pos_x, player.Player1.pos_y = 10,68
                player.Player1.img_x, player.Player1.img_y =  0,0
                player.Player1.power = False
                player.Player1.staff = False
                player.Player1.scores = 0

                #resetando itens
                item.staff.item= False
                item.staff.pos_x, item.staff.pos_y= 75,68
                item.staff.img_x,item.staff.img_y = 96,0
                item.Coin.pos_y =-16
                item.Mushroom.pos_y=-16 

                #resetando mobs
                mob.Goblin.pos_x ,mob.Goblin.pos_y = 320, 68
                mob.Goblin.img_x = 0
                mob.Goblin.img_y = 112
                mob.Goblin.spear_x = -16

            else:
                button.ButtonHome.img_x = 0
            
        #se pressionar o botão de Som
        if button.ButtonMusic.PressButton():
            button.ButtonMusic.img_x = 48
            
            #Troca de sprites
            if button.ButtonMusic.img_y == 0:
                #sprite botao precionado + parar musica
                button.ButtonMusic.img_y = 16
                pyxel.stop(0)
                pyxel.stop(1)
            else:
                #sprite/Musica padrão
                button.ButtonMusic.img_y = 0
                pyxel.playm(0, loop= True)
                pyxel.playm(1, loop= True)
        
        #Sprite padrão
        else:
            button.ButtonMusic.img_x  = 32

    #Função da interface
    def draw(self):
        pyxel.cls(0)
        pyxel.mouse(visible= True)

        #se o botão play for apertado:
        if button.ButtonPlay.button:
            item.Mushroom.DrawItem()
            item.Coin.DrawItem()
            item.staff.DrawItem()
            mob.Goblin.DrawMobs()
            player.Player1.DrawPlayer()
            button.ButtonHome.DrawButton()

        else:
            #Nome do game na tela
            pyxel.text(self.window_x/2 -13, 30, "Magic!", pyxel.frame_count % 16)
            #enquanto não clicar no botão play,ele ficará na tela
            button.ButtonPlay.DrawButton()

        #Desenhando blocos/itens/player
        block.DrawBlock(0, 84, 0, 160, 7)
        button.ButtonMusic.DrawButton()
#verificação da execução direta do módulo
if __name__ == "__main__":
    Game()