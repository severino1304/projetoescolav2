import pygame
import globals
import utils
import engine

class Level:
    def __init__(self, platforms=None, entities=None, winFunc=None, loseFunc=None, powerupSpawnPoints=None, lava=None):
        self.platforms = platforms
        self.entities = entities
        self.winFunc = winFunc # guardar variável
        self.loseFunc = loseFunc # guardar variável
        self.powerupSpawnPoints = powerupSpawnPoints
        self.lava = lava
    def isWon(self):
        if self.winFunc is None:
            return False
        return self.winFunc(self)
    def isLost (self):
        if self.loseFunc is None:
            return False
        return self.loseFunc(self)


# perder caso não existam jogadores vivos
def lostLevel(level):
    # o nível não está perdido caso qualquer jogador possua pelo menos 1 vida
    for entity in level.entities:
        if entity.type == "player":
            if entity.battle is not None:
                if entity.battle.vidas > 0:
                    return False
    # nível perdido
    return True

# vence caso não sobrem moedas
def wonLevel(level):
    # o nível não foi terminado caso sobrem moedas
    for entity in level.entities:
        if entity.type == "collectable":
            return False
    return True

def loadLevel(levelNumber):
    if levelNumber == 1:
        # carregar nível 1
        globals.world = Level(
            platforms = [
                    # meio
                    pygame.Rect(100,300,400,50),
                    # esquerda
                    pygame.Rect(100,250,50,50),
                    # direita
                    pygame.Rect(450,250,50,50),
                    pygame.Rect(0,200,100,50),
                    {
                        "rect" : pygame.Rect(200, 150, 100, 20),  # móvel
                        "type": "moving",
                        "speed": 2,
                        "axis": "x",
                        "distance": 150,
                        "direction": 1,
                        "original_pos": (200, 150),
                    },
            ],
            entities = [
                    utils.makeCoin(105,225), #
                    utils.makeCoin(200,275), # Lista de entidades com 2 moedas
                    utils.makeEnemy(150,291),
                    utils.makePowerup("vida", 400,260),
                    utils.makeButton(300,400,44,32)
            ],
            winFunc = wonLevel,
            loseFunc = lostLevel,
            powerupSpawnPoints = [(400,260),(300, 100)]
        )
    if levelNumber == 2:
        # carregar nível 2
        globals.world = Level(
            platforms = [
                    # meio
                    pygame.Rect(100,300,400,50),
            ],
            entities = [
                    utils.makeCoin(105,225), #
            ],
            winFunc = wonLevel,
            loseFunc = lostLevel
        )

    if levelNumber == 3:
    # carregar nível 3
        globals.world = Level(
            platforms = [
                    # meio
                    pygame.Rect(100,300,400,50),
            ],
            entities = [
                    utils.makeCoin(105,225), #
            ],
            winFunc = wonLevel,
            loseFunc = lostLevel,
            powerupSpawnPoints = None,
            lava = engine.Lava(alturaInicial=830, speed=1)
        )

    # adicionar jogadores
    for player in globals.players:
        globals.world.entities.append(player)
   
    # reíniciar os jogadores
    for entity in globals.world.entities:
        entity.reset(entity)

def update_level(players):
    # Atualizar entidades (botões, moedas, etc.)
    for entity in globals.world.entities:
        if entity.type == "button":
            # Verificar colisão com jogadores
            for player in players:
                if (entity.position.x < player.position.x < entity.position.x + entity.position.width and
                    entity.position.y < player.position.y + player.position.height < entity.position.y + entity.position.height):
                    entity.activated = True
                    if entity.trigger:
                        entity.trigger["active"] = True  # Ativa plataformas ligadas ao botão
                    break
            else:
                entity.activated = False

    # Atualizar plataformas móveis
    for platform in globals.world.platforms:
        if isinstance(platform, dict) and platform["type"] == "moving":
            # Atualizar posição no eixo X
            if platform["axis"] == "x":
                platform["rect"].x += platform["speed"] * platform["direction"]
                if abs(platform["rect"].x - platform["original_pos"][0]) >= platform["distance"]:
                    platform["direction"] *= -1  # Inverte a direção
            # Atualizar posição no eixo Y
            elif platform["axis"] == "y":
                platform["rect"].y += platform["speed"] * platform["direction"]
                if abs(platform["rect"].y - platform["original_pos"][1]) >= platform["distance"]:
                    platform["direction"] *= -1
