#importações
import pyxel
from components import player
from levels import block, item, mob

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

    #Função da interface
    def draw(self):
        pyxel.cls(0)
        pyxel.mouse(visible= True)

        #Nome do game na tela
        pyxel.text(self.window_x/2 -13, 30, "Magic!", pyxel.frame_count % 16)

        #Desenhando blocos/itens/player
        block.DrawBlock(0, 84, 0, 160, 7)
        item.Mushroom.DrawItem()
        item.Coin.DrawItem()
        item.staff.DrawItem()
        mob.Goblin.DrawMobs()
        player.Player1.DrawPlayer()

#verificação da execução direta do módulo
if __name__ == "__main__":
    Game()
