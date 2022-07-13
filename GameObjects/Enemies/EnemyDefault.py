#coding=utf-8

from GameObjects.Enemies._Enemy import EnemyBase
from Core.Game import Game
from Core.Vector import Vector2

class EnemyDefault(EnemyBase):
    # Construtor. Use APENAS para declarar variáveis
    # Comportamentos iniciais devem ser adicionados no _start
    def __init__(self):
        super().__init__()
        self.lives = 1
        self.score_base = 100
        self._fire_delay = .5
    
        self._reload()
    
    # Executa no momento em que o inimigo é instanciado/criado
    def _awake(self):
        super()._awake()
        
    # Executa no momento em que o inimigo é habilitado em cena
    def _start(self):
        super()._start()
        # Função do inimigo usado para definir uma posição de spawn.
        # O posicionamento é aleatório e você pode adicionar um fixo, caso queira
        self.configure_spawn()
        
        # Função dos inimigos usado para encarar o player
        self._faceToPlayer()
        # Função dos inimigos usado para andar na direção do player
        self._followPlayer()
    
    # Executa a todo frame
    def _update(self):
        super()._update()
        
    
    # Executa após todo _update
    def _afterUpdated(self):
        super()._afterUpdated()
    
    def _fire(self):
        from GameObjects.GunFire import GunFire
        
        # Irei bolar um tiro no formato \|/
        # Primeiro, crio os 3 tiros
        shoot = GunFire()
        shoot2 = GunFire()
        shoot3 = GunFire()
        
        
        # É NECESSÁRIO adicioná-los como filha ANTES de alterar as propriedades
        self.addChild(shoot)
        self.addChild(shoot2)
        self.addChild(shoot3)
        
        
        # Fazemos a bala "olhar" para o Player
        angleOffset = 180 # Apenas porque a imagem da bala está invertida
        shoot.transform.vectorRotate(self.vector_direction, angleOffset)
        shoot2.transform.vectorRotate(self.vector_direction, angleOffset)
        shoot3.transform.vectorRotate(self.vector_direction, angleOffset)
        
        
        # Colocamos elas para nascerem em frente a nave
        shoot.setLocalPosition(
            # Pegamos a posição central do inimigo e somamos com "a direção que olha com metade de seu próprio tamanho"
			self.getObjectCenter() + (self.vector_direction * (self.width / 2.3))	
		)
        shoot2.setLocalPosition(self.getObjectCenter() + (self.vector_direction * (self.width / 2.3)))
        shoot3.setLocalPosition(self.getObjectCenter() + (self.vector_direction * (self.width / 2.3)))
        
        
        # Configuro agora a movimentação dos tiros
        # Tiro que anda em linha reta. O cálculo da rota dos tiros é feito completamente por cálculo vetorial :)
        shoot2.kinetics.setVelocity(
            # Pego o vetor direção que a nave está olhando e multiplico pela
            # velocidade que quero adicionar ao tiro
            (self.vector_direction) * shoot.moveSpeedBase * .8
        )
        # Tiro que vai mais a direta
        shoot.kinetics.setVelocity((self.vector_direction + Vector2(.15, 0)) * shoot.moveSpeedBase * .8)
        # Tiro que vai mais a esquerda
        shoot3.kinetics.setVelocity((self.vector_direction + Vector2(-.15, 0)) * shoot.moveSpeedBase * .8)
        
        
        # Após todas as configurações, colocamos a bala para colidir com o Player
        shoot.addCollisionWithPlayer()
        shoot2.addCollisionWithPlayer()
        shoot3.addCollisionWithPlayer()