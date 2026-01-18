from tkinter import *
from PIL import Image, ImageTk

# Liste pour la création du background les lettres correspondent aux murs et les '.' au espaces
tableau = ["fbbbbbbbbbbbbbbbbbe",
           "a.................a",
           "a.fbe.a.bbb.a.fbe.a",
           "a.a.a.a.....a.a.a.a",
           "a.cbd.a.a.a.a.cbd.a",
           "a.....a.a.a.a.....a",
           "a.fbbbd.a.a.cbbbe.a",
           "a.a.............a.a",
           "a.a.bbbbb.bbbbb.a.a",
           "a.................a",
           "a.bbbbb.fbe.bbbbb.a",
           "a.......a.a.......a",
           "a.fbe.a.cbd.a.fbe.a",
           "a.a.a.a.....a.a.a.a",
           "a.cbd.a.fbe.a.cbd.a",
           "a.....a.a.a.a.....a",
           "a.bbbbd.cbd.cbbbb.a",
           "a.................a",
           "cbbbbbbbbbbbbbbbbbd"]  

TAILLE_CASE = 32

# position de la tête
speed = 1
i, j = 5,5
direction = ""

def dessiner_carte():
    # Boucle qui parcourt la liste afin de créer la carte
    for j in range(len(tableau)):
        for i in range(len(tableau[j])):
            if tableau[j][i] == "a":
                canvas.create_image(32*i, j*32, anchor=NW, image=a)
            elif tableau[j][i] == "b":
                canvas.create_image(32*i, j*32, anchor=NW, image=b)
            elif tableau[j][i] == "c":
                canvas.create_image(32*i, j*32, anchor=NW, image=c)
            elif tableau[j][i] == "d":
                canvas.create_image(32*i, j*32, anchor=NW, image=d)
            elif tableau[j][i] == "e":
                canvas.create_image(32*i, j*32, anchor=NW, image=e)
            elif tableau[j][i] == "f":
                canvas.create_image(32*i, j*32, anchor=NW, image=f)
            elif tableau[j][i] == ".":
                pass

def interface():
    global fenetre, canvas, a, b, c, d, e, f
    
    fenetre = Tk()
    fenetre.title("Nibbler")
    canvas = Canvas(
                    fenetre,
                    width=608,
                    height=608,
                    bg="black"
                    )
    canvas.pack()
    
    ## Chargement des images
    imagea = Image.open("mur_a.png")
    a = ImageTk.PhotoImage(imagea)
    
    imageb = Image.open("mur_b.png")
    b = ImageTk.PhotoImage(imageb)
    
    imagec = Image.open("mur_c.png")
    c = ImageTk.PhotoImage(imagec)

    imaged = Image.open("mur_d.png")
    d = ImageTk.PhotoImage(imaged)
    
    imagee = Image.open("mur_e.png")
    e = ImageTk.PhotoImage(imagee)
    
    imagef = Image.open("mur_f.png")
    f = ImageTk.PhotoImage(imagef)

    fenetre.bind("<Key>", deplacer)
    dessiner_carte()
    dessiner()
    
    fenetre.after(500, maj) 

def dessiner():
    canvas.delete("snake")
    x = j * TAILLE_CASE
    y = i * TAILLE_CASE
    canvas.create_rectangle(x,y, x+TAILLE_CASE, y+TAILLE_CASE, fill="red", tags="snake")

def deplacer(event):
    #print(event)
    global direction, fenetre
    if event.keysym == "Right":
        direction = "Right"
    elif event.keysym == "Left":
        direction = "Left"
    elif event.keysym == "Up":
        direction = "Up"
    elif event.keysym == "Down":
        direction = "Down"
    else:
        direction = ""

def collision(x,y):
    # Gestion du hors carte
    if x<0 or y<0:
        return True
    if y >= len(tableau) or x >= len(tableau[0]):
        return True
    # Gestion des murs
    return tableau[y][x] != "."

def maj():
    global j,i

    j1,i1 = j,i # Position n+1

    if direction == "Right":
        j1 += speed
    elif direction == "Left":
        j1 -= speed
    elif direction == "Up":
        i1 -= speed
    elif direction == "Down":
        i1 += speed
    dessiner()
    fenetre.after(200, maj)

    if collision(j1,i1) == False:
        j,i = j1,i1

global fenetre

interface()


fenetre.mainloop() 