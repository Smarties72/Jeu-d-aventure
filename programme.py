"""
Programme réalisé par Aulair, Florentin, 1g7
"""
import pygame

#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((640, 360))
pygame.display.set_caption("office.jpg")
font = pygame.font.Font('freesansbold.ttf', 20)
image1=pygame.image.load("office.jpg")
image2=pygame.image.load("couloir.jpg")
image3=pygame.image.load("salle de jeux.jpg")
image4=pygame.image.load("hall principal.jpg")
image5=pygame.image.load("porte.jpg")
image6=pygame.image.load("toillette.jpg")
image7=pygame.image.load("DiningArea.jpg")
image8=pygame.image.load("scène de concert.jpg")
image9=pygame.image.load("clé.jpg")
image10=pygame.image.load("fin.jpg")
text1 = font.render("Vous vous trouvez dans la salle des caméras", True, (0, 200, 0))
text2 = font.render("Vous vous trouvez dans le couloir", True, (0, 255, 0))
text3 = font.render("Vous vous trouvez dans la salle de jeux", True, (255, 0, 255))
text4 = font.render("Vous vous trouvez dans le hall principal",True,(255,0,255))
text5 = font.render("Vous vous trouvez dans la loge",True,(255,0,255))
text6 = font.render("Vous vous trouvez devans les toillettes",True,(255,0,255))
text7 = font.render("Vous vous trouvez dans la salle de fête",True,(255,0,255))
text8 = font.render("Vous vous trouvez devans la scène principal",True,(255,0,255))
text9 = font.render("Vous avez trouvez la clef mais à quoi sert t'elle ?",True,(255,0,255))
text10 = font.render("Gagner vous avez trouver la boite mais avez vous trouver la clef ?",True,(255,0,255))


dansQuellePierceEstLePersonnage=1


def decrireLaPiece(piece):
    if piece==1:
        fenetre.blit(image1,(0,0))  #afficher l'image à la prochaine actualisation
        fenetre.blit(text1,(0,300)) #afficher le texte à la prochaine actualisation
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(0,300))
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(0,300))
    elif piece==4:
        fenetre.blit(image4,(0,0))
        fenetre.blit(text4,(0,300))

    elif piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(0,300))
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(0,300))
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(0,300))
    elif piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(0,300))
    elif piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(0,300))

    elif piece==10:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text10,(0,300))




def decision(direction,piece):
    print("Vous désirez allez au",direction)
    memorisePiece=piece
    #N : le personnage désire aller au nord    
    if direction=='n':
        if piece==6:
            piece=7
        elif piece==8:
            piece=9
        elif piece==3:
            piece=4
    #S : le personnage désire aller au sud
    elif direction=='s':
        if piece==9:
            piece=8
        elif piece==7:
            piece=6
        elif piece==4:
            piece=3
    #E : le personnage désire aller à l'est
    elif direction=='o':
       if piece==8:
        piece=7
       elif piece==10:
        piece=8
       elif piece==3:
        piece=2
       elif piece==5:
        piece=6
       elif piece==4:
        piece=5
       elif piece==2:
        piece=1
       elif piece==4:
            piece=5
    
    #O : le personnage désire aller à l'ouest
    elif direction=='e':
        if piece==7:
            piece=8
        elif piece==8:
            piece=10
        elif piece==5:
            piece=4
        elif piece==1:
            piece=2
        elif piece==2:
            piece=3
        elif piece==6:
            piece=5

       
    if memorisePiece==piece:
        print("Déplacement impossible")
    else:
        print("C'est possible")
    return piece



loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #lecture du clavier
            dansQuellePierceEstLePersonnage=decision(event.unicode,dansQuellePierceEstLePersonnage)
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
    decrireLaPiece(dansQuellePierceEstLePersonnage)
    # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()

