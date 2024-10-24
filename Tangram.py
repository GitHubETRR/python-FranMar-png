import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((960, 640))
clock = pygame.time.Clock()
pygame.display.set_caption("VIVA EL TANGRAM")
mover_piezas = 0

player_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)

#piezas
triangulo_grande_pos = [[185,120],[385,120],[285,20]]
triangulo_medio_pos = [[442,120],[542,120],[542,20]] 
triangulo_chico_pos = [(599,120),(699,120),(649,70)]
poligono_pos = [(806,120),(756,70),(856,70),(906,120)]
cuadrado_pos = pygame.Rect(57, 45, 70.71, 70.71) # 57,45 es posicion X,Y
agarrado = 0

#figura
figura = [(570.7,200),(500,270.7),(570.7,270.7),(570.7,341.4),(521.4,463.8),(620.7,563.8),(550,634.5),(620.7,634.5),(620.7,563.8),(720.7,563.8),(650,634.5),(720.7,634.5),(720.7,563.8),(820.7,563.8),(720.7,463.8),(591.4,463.8),(641.4,341.4),(641.4,270.7)]
# marcos
tangram_marco = pygame.Rect(480, 160, 480, 480)
marco = pygame.Rect(0, 0, 960, 640)

# esconder cursor
pygame.mouse.set_visible(False)

# colores
BLANCO = (255, 255, 255)
CELESTE = (0, 255, 255)

running = True
dt = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
    # muestra objetos en pantalla
    pygame.draw.rect(screen, BLANCO, marco, 5)
    pygame.draw.rect(screen, BLANCO, tangram_marco, 5)
    
    player = pygame.draw.circle(screen, CELESTE, player_pos, 10)
    
    #piezas
    triangulo_grande = pygame.draw.polygon(screen, CELESTE, triangulo_grande_pos)
    triangulo_medio = pygame.draw.polygon(screen, CELESTE, triangulo_medio_pos)
    triangulo_chico = pygame.draw.polygon(screen, CELESTE, triangulo_chico_pos)
    poligono = pygame.draw.polygon(screen, CELESTE, poligono_pos)
    cuadrado = pygame.draw.rect(screen, CELESTE, cuadrado_pos)
    
    figura_pantalla = pygame.draw.polygon(screen, CELESTE, figura)
    
    # teclas
    keys = pygame.key.get_pressed() #keys = tecla presionada
    
    if keys[pygame.K_UP]:
        player_pos.y -= 2 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 2 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 2 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 2 * dt
        
    if keys[pygame.K_c]:
        dt = 0.3
    else:
        dt = 1
        
    # Detectar colision
    if player.colliderect(tangram_marco):
        if player_pos.x < tangram_marco.left:
            player_pos.x = tangram_marco.left - 10
        elif player_pos.x > tangram_marco.right:
            player_pos.x = tangram_marco.right + 10
        if player_pos.y < tangram_marco.top:
            player_pos.y = tangram_marco.top - 10
        elif player_pos.y > tangram_marco.bottom:
            player_pos.y = tangram_marco.bottom + 10

    # Colision con los bordes de la pantalla
    if player_pos.x < 0:
        player_pos.x = 0
    elif player_pos.x > screen.get_width():
        player_pos.x = screen.get_width()
    if player_pos.y < 0:
        player_pos.y = 0
    elif player_pos.y > screen.get_height():
        player_pos.y = screen.get_height()
        
    # Mover piezas
    if agarrado == 0:
        if keys [pygame.K_z]:
            if player.colliderect(triangulo_medio):agarrado = 1          
            elif player.colliderect(triangulo_grande):agarrado = 2
            elif player.colliderect(triangulo_chico):agarrado = 3 
            elif player.colliderect(cuadrado): agarrado = 4
            elif player.colliderect(poligono): agarrado = 5
            else: agarrado = 0 
        else: agarrado = 0
    
    if agarrado == 1: 
        triangulo_medio_pos[0] = [player_pos.x-100, player_pos.y]
        triangulo_medio_pos[1] = [player_pos.x, player_pos.y]
        triangulo_medio_pos[2] = [player_pos.x, player_pos.y-100]
        if not keys [pygame.K_z]: agarrado = 0
        
    if agarrado == 2: 
        triangulo_grande_pos[0] = [player_pos.x-100, player_pos.y+100]
        triangulo_grande_pos[1] = [player_pos.x+100, player_pos.y+100]
        triangulo_grande_pos[2] = [player_pos.x, player_pos.y]
        if not keys [pygame.K_z]: agarrado = 0
        
    if agarrado == 3: 
        triangulo_chico_pos[0] = (player_pos.x-50, player_pos.y+50 )
        triangulo_chico_pos[1] = (player_pos.x+50, player_pos.y+50)
        triangulo_chico_pos[2] = (player_pos.x, player_pos.y)
        if not keys [pygame.K_z]: agarrado = 0
        
    if agarrado == 4: 
        cuadrado_pos = pygame.Rect(player_pos.x, player_pos.y, 70.71, 70.71)
        if not keys [pygame.K_z]: agarrado = 0
     
    if agarrado == 5: 
        poligono_pos[0] = (player_pos.x-25, player_pos.y+25)
        poligono_pos[1] = (player_pos.x-75, player_pos.y-25)
        poligono_pos[2] = (player_pos.x+25, player_pos.y-25)
        poligono_pos[3] = (player_pos.x+75, player_pos.y+25)
        if not keys [pygame.K_z]: agarrado = 0
        
    # pone todo en pantalla
    pygame.display.flip()
    
    # velocidad (mayor numero mas rapido)
    clock.tick(120) / 1000

pygame.quit()