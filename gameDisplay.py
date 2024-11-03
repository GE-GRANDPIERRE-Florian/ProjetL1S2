from fltk import ligne, point, cercle, PhotoImage
import fltk as fl

def trackLoader(track):
    """Function that load track, a txt file as a matrice of list

    INPUT:
    track (string): txt file containing "*" or "#" or "." or ">"

    OUTPUT:
    lines (list): matrice of list containing "*" or "#" or "." or ">"
    """
    lines = []
    with open(track, 'r') as track:
        for line in track:
            track_chain = list(line.strip())
            lines.append(track_chain)
    return lines

def gridDisplay(w, h, trackChain, wid, hei):
    """Function that display a grid with a size proportionnal of the map and the choosen size by the user
    
    INPUT:
    w (int): original width choosen by the user
    h (int): original height choosen by the user
    trackChain (list): matrice of list containing "*" or "#" or "." or ">"
    wid (int): recalculated width proportionnal to the width choosen by the user
    hei (int): recalculated height proportionnal to the height choosen by the user

    OUTPUT:
    (display)
    """
    for i in range(len(trackChain)-1):
        ligne(0, (i + 1) * hei, h, (i + 1) * hei)
    for j in range(len(trackChain[0])-1):
        ligne((j + 1) * wid, 0, (j + 1) * wid, w)

def trackDisplay(trackChain, wid, hei):
    """Draw the obstacles, starting line,
    finish line .

    Args:
        trackChain (list): the map
        wid (int): width of the board
        hei (int): height of the board
    """
    for line in range(len(trackChain)-1):
        for car in range(len(trackChain[line])):
            if trackChain[line][car] == ".":
                point(wid * (1 + car), hei * (1 + line),
                      couleur="white", epaisseur=hei / 1.4)    
    for line in range(len(trackChain) - 1):
        for car in range(len(trackChain[line])):
            if trackChain[line][car] == "#":
                point(wid * (1 + car), hei * (1 + line), couleur="green",
                  epaisseur= int(hei/1.2))
            elif trackChain[line][car] == ">":
                point(wid * (1 + car), hei * (1 + line), couleur="blue",
                  epaisseur=wid / 1.2)
            elif trackChain[line][car] == "*":
                point(wid * (1 + car), hei * (1 + line), couleur="grey",
                  epaisseur=hei / 1.2)

def trajectoryDisplay(trajectory, wid, hei, speed):
    """Function that display the user's car trajectory
    
    INPUT:
    trajectory (list): list of tuple containing car's positions 
    wid (int): recalculated width proportionnal to the width choosen by the user
    hei (int): recalculated height proportionnal to the height choosen by the user

    OUTPUT:
    (display)
    """
    color ="black"
    somme = int(speed[0] + speed[1])
    if 2 <= somme <=3:
        color="yellow"
    elif 4 <= somme <=6:
        color='orange'
    elif 7 <= somme:
        color='red'
    for i in range(len(trajectory) - 1):
        cercle(wid * (1 + trajectory[i][0]),
              hei * (1 + trajectory[i][1]),
              wid / 2, remplissage="red")
        ligne(wid * (1 + trajectory[i][0]),
              hei * (1 + trajectory[i][1]),
              wid * (1 + trajectory[i + 1][0]),
              hei * (1 + trajectory[i + 1][1]),
              epaisseur=3, couleur=color)

def neighborsDisplay(options, wid, hei):
    """Function that display the 8 neighbors of a point on the map
    
    INPUT:
    options (list): list containing tuple of neighbors' coordinates
    wid (int): recalculated width proportionnal to the width choosen by the user
    hei (int): recalculated height proportionnal to the height choosen by the user

    OUTPUT:
    (display)
    """
    for i in range(len(options)):
        cercle(wid * (1 + options[i][0]),
              hei * (1 + options[i][1]), 
              wid / 2.5, remplissage="white")

def futur_point_display(fle, neighs, wid, hei):
    """Draw the possibles futur points.

    Args:
        fle (list): the map
        neighs (list): neighbors of the futur calculated point
        wid (int): width of the window
        hei (int): height of the window
    """
    for pnts in neighs:
        righ = pnts[0]
        left = pnts[1]
        if righ <= len(fle[0]) and left <= len(fle):
            cercle(wid * (righ + 1),
                   hei * (left + 1),
                   wid / 2.5, remplissage="white")

def nearest_color(rgb):
    """Function that calculate the nearest color of a rgb tuple between green,
    white, gray and blue and return a string associated to this color
    
    INPUT:
    rgb (tuple): rgb tuple 

    OUTPUT:
    closest (string): closest color 
    """
    colors = {
        '#': (0, 255, 0),  # green
        '.': (255, 255, 255),  # white
        '*': (128, 128, 128),  # gray
        '>': (0, 0, 255)  # blue
    }

    dist = lambda c1, c2: sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5
    closest = min(colors, key=lambda k: dist(rgb, colors[k]))
    
    return closest

imgtrack = "media/map_test.png"

def imgTrack(track):
    """ return a list of the different type of point of a line,
    (obstacles, starting line, finish line)"""
    fl.cree_fenetre(500,500)
    pisteimg = PhotoImage(file = track)
    img = []
    wid= pisteimg.width()
    hei = pisteimg.height()
    for i in range(hei):
        line = []
        for j in range(wid):
            line.append(nearest_color(pisteimg.get(i,j)))
        img.append(line)
    fl.ferme_fenetre()
    return img
    """for line in img:
        print(line)

    print(nearest_color(pisteimg.get(1,1)))
imgTrack()"""