import pygame
import sys

#Inicializamos el módulo
pygame.init()

#Creamos nuestra Screen (Seria ocmo un canvas negro donde podemos poner cosas sobre él)
WIDTH, HEIGTH = 800, 800
SCREEN = pygame.display.set_mode((800, 800)) #Variable en mayus porque va a ser una constante

#Titulo del programa
pygame.display.set_caption("VIVA LA LIBERTAD CARAJO!")


#Otro black canvas, pero pasandole una imagen
ICON = pygame.image.load("ima1.jpeg")
pygame.display.set_icon(ICON)

#Definimos la imagen de back aca pero la cargamos y actualizamos el display mas abajo
BACKGROUND = pygame.image.load("ima2.png")

#Creamos un reloj
CLOCK = pygame.time.Clock()

#Seteamos una fuente
FONT = pygame.font.SysFont("segoeuiblack", 64) #Solo nos deja usar las fuentes default de pygame. 2do parametro seteamos la Size
#print(pygame.font.get_fonts()) ACA podemos ver las fuentes default que tiene pygame
text = FONT.render("Fuerza del Cielo", True, "white") #Lo hacemos que sea un objeto de texto, que funciona como surface(capa) en pygame. Para el color = str name / RGB / HEX

text_rect = text.get_rect(center=(WIDTH/2, 150)) #Es como un rectangulo que va alrededor de una surface, sirve para detectar colisiones por ej, pero ahora lo creamos para manejar la ubi del texto
                                                 #Definimos su posicion en valores x, y.  


pygame_image = pygame.transform.scale(pygame.image.load("ima3.png"), (400, 300)) #Esta funcion nos permite escalar la imagen. Parametros x y
pygame_image_rect = text.get_rect(center=(WIDTH/2, 300))


###----------------------------------------------INICIO-------------------------------------------------------------------------------------------------------------------------------------------------------####

#main game loop. Es lo que queremos para un juego, no se detendrá hasta que se lo indiquemos
while True:
    #Hacemos que el game corra, en vez de desaparecer al instante y seteamos el QUIT
    for event in pygame.event.get(): #retorna todos los posibles eventos en pygame como por ej mouse click, keyboard, etc y entonces si tocamos la X de cierre, se stopea.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(BACKGROUND, (0, 0))#Blit nos permite poner una surface (capa) arriba de otra capa, ya teniamos el black canvas como surface principal
    SCREEN.blit(text, text_rect)
    SCREEN.blit(pygame_image, pygame_image_rect)

    
    pygame.display.update()

    CLOCK.tick(60) #Seteamos los fps a 60, y lo podremos ver si hay cosas en movimiento