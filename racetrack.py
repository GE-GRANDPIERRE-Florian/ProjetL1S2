from fltk import (cree_fenetre, donne_ev, type_ev, touche, mise_a_jour,
                  ferme_fenetre, abscisse, ordonnee , efface, rectangle, texte, attend_ev, efface_tout)
import os

from gameDisplay import (trackLoader, trackDisplay, gridDisplay, trajectoryDisplay,
                         neighborsDisplay, futur_point_display)
from gameEngine import (clic_neighbors, find_neighbors, speed, next, lose, win,
                        point_placement)


def game(w, h, track):
    # Game configuration
    file = trackLoader(track)
    if len(file[0]) > len(file):
        height = h / int(len(file))
    else:
        height = h / (len(file[0]))
    width = w / (len(file[1]))
    cree_fenetre(w, h)

    # Draw the grid and track
    trackDisplay(file, width, height)
    gridDisplay(h, w, file, width, height)

    # Start Initialization
    point = point_placement(file)
    trajectory = [point]
    neighbors = find_neighbors(file , point)
    #trajectoryDisplay(trajectory, width, height)
    futur_point_display(file, neighbors, width, height)

    playtime = True
    while playtime:
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == 'Quitte':
            playtime = False
            exit()

        elif tev == 'ClicGauche':
            # Detect the clicked point
            abss, ordo = abscisse(ev), ordonnee(ev)
            point = clic_neighbors(neighbors, width, height, abss, ordo, height/2, trajectory)

            # Calculate next point
            if point in trajectory and len(trajectory)>1:
                spd = speed(trajectory)
            else:
                trajectory.append(point)
                spd = speed(trajectory)
            next_point, neighbors= next(spd, trajectory, file)

            # Draw the new state of the grid and track
            efface_tout()
            trackDisplay(file, width, height)
            gridDisplay(h, w, file, width, height)
            trajectoryDisplay(trajectory, width, height, spd)

            # Check if the point is not of graph before drawing it
            if next_point[1] <= len(file)-1 and next_point[0] <= len(file[0])-1:
                futur_point_display(file, neighbors, width, height)

        # Comeback with 'space'
        if tev == 'Touche':
            nom_touche = touche(ev)
            if nom_touche == 'space':
                if len(trajectory) > 1:
                    point = trajectory[-1]
                    sup = trajectory.pop()
                    spd = speed(trajectory)
                    next_point, neighbors= next(spd, trajectory, file)

                    # Draw the new state of the grid and track
                    efface_tout()
                    trackDisplay(file, width, height)
                    gridDisplay(h, w, file, width, height)
                    trajectoryDisplay(trajectory, width, height, spd)

                    # Check if the point is not of graph before drawing it
                    if next_point[1] <= len(file)-1 and next_point[0] <= len(file[0])-1:
                        futur_point_display(file, neighbors, width, height)
                else:
                    exit()
        
                 

        # Test if the player lose or win
        playtime = lose(file, point)
        if playtime is False:
            efface_tout()
            texte(w//2, h//2,
                  "Lose",
                  ancrage='center',
                  couleur="red",
                  taille=w//10)
            attend_ev()
            exit()
        playtime = win(file, point)
        if playtime is False:
            efface_tout()
            texte(w//2, h//2,
                  "Win",
                  ancrage='center',
                  couleur="blue",
                  taille=w//10)
            attend_ev()
            exit()

        # Update
        mise_a_jour()

    ferme_fenetre()




def menu():
    cree_fenetre(800, 600)
    wid, hei = 800, 600
    maps = os.listdir('pistes')
    currmap = 0
    ###########   PLAY
    playbtn = [300, 90, 500, 130]
    rectangle(playbtn[0], playbtn[1], playbtn[2], playbtn[3]) #play button
    texte(400, 110, "PLAY", ancrage='center', tag='play') #play
    ###########   QUIT
    quitbtn = [300, 530, 500, 570]
    rectangle(quitbtn[0], quitbtn[1], quitbtn[2], quitbtn[3]) #quit button
    texte(400, 550, "LEAVE", ancrage='center', tag='quit') #quit
    ###########   SOLVE
    solve = [300, 140, 500, 180]
    rectangle(solve[0], solve[1], solve[2], solve[3]) #solve button
    texte(400, 160, "SOLVE", ancrage='center', tag='play') #solve 
    ###########   WINDOW SIZE
    # WIDTH
    lesswid = [50, 280, 160, 305]
    rectangle(lesswid[0], lesswid[1], lesswid[2], lesswid[3]) #-width button
    texte((lesswid[0] + lesswid[2]) / 2, (lesswid[1] + lesswid[3]) / 2, '-10', ancrage='center', taille=15)
    morewid = [170, 280, 280, 305]
    rectangle(morewid[0], morewid[1], morewid[2], morewid[3]) #+width button
    texte((morewid[0] + morewid[2]) / 2, (morewid[1] + morewid[3]) / 2, '+10', ancrage='center', taille=15)
    texte(165, 260, "Width : " + str(wid), ancrage='center', tag='wid') 
    # HEIGHT
    lesshei = [50, 350, 160, 375]
    rectangle(lesshei[0], lesshei[1], lesshei[2], lesshei[3]) #-height button
    texte((lesshei[0] + lesshei[2]) / 2, (lesshei[1] + lesshei[3]) / 2, '-10', ancrage='center', taille=15)
    morehei = [170, 350, 280, 375]
    rectangle(morehei[0], morehei[1], morehei[2], morehei[3]) #+height button
    texte((morehei[0] + morehei[2]) / 2, (morehei[1] + morehei[3]) / 2, '+10', ancrage='center', taille=15)
    texte(165, 330, "Height : " + str(hei), ancrage='center', tag='hei') 
    ##########   MAP CHOICE
    #previous
    prevmap = [520, 315, 630, 340]
    rectangle(prevmap[0], prevmap[1], prevmap[2], prevmap[3]) #-previous button
    texte((prevmap[0] + prevmap[2]) / 2, (prevmap[1] + prevmap[3]) / 2, 'PREVIOUS', ancrage='center', taille=15)
    #next
    nextmap = [640, 315, 750, 340]
    rectangle(nextmap[0], nextmap[1], nextmap[2], nextmap[3]) #+next button
    texte((nextmap[0] + nextmap[2]) / 2, (nextmap[1] + nextmap[3]) / 2, 'NEXT', ancrage='center', taille=15)
    texte(635, 290, maps[currmap][:-4], ancrage='center', tag='map') 
    play = True
    while play:
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == 'Quitte':
            playtime = False
            exit()
        elif tev == 'ClicGauche':
            absc, ordo = abscisse(ev), ordonnee(ev)
            if (playbtn[0] <= absc <= playbtn[2]) and (playbtn[1] <= ordo <= playbtn[3]):
                ferme_fenetre()
                mps = "pistes/" + maps[currmap]
                game(wid, hei, mps)
            elif (quitbtn[0] <= absc <= quitbtn[2]) and (quitbtn[1] <= ordo <= quitbtn[3]):
                playtime = False
                exit()
            elif (lesswid[0] <= absc <= lesswid[2]) and (lesswid[1] <= ordo <= lesswid[3]):
                wid = abs(wid - 10)
                efface("wid")
                texte(165, 260, "Width : " + str(wid), ancrage='center', tag='wid') #width
            elif (morewid[0] <= absc <= morewid[2]) and (morewid[1] <= ordo <= morewid[3]):
                wid = abs(wid + 10)
                efface("wid")
                texte(165, 260, "Width : " + str(wid), ancrage='center', tag='wid') #width
            elif (lesshei[0] <= absc <= lesshei[2]) and (lesshei[1] <= ordo <= lesshei[3]):
                hei = abs(hei - 10)
                efface("hei")
                texte(165, 330, "Height : " + str(hei), ancrage='center', tag='hei') #height
            elif (morehei[0] <= absc <= morehei[2]) and (morehei[1] <= ordo <= morehei[3]):
                hei = abs(hei + 10)
                efface("hei")
                texte(165, 330, "Height : " + str(hei), ancrage='center', tag='hei') #height
            elif (prevmap[0] <= absc <= prevmap[2]) and (prevmap[1] <= ordo <= prevmap[3]):
                currmap = (currmap - 1) % 5 
                efface('map')
                texte(635, 290, maps[currmap][:-4], ancrage='center', tag='map') #current map
            elif (nextmap[0] <= absc <= nextmap[2]) and (nextmap[1] <= ordo <= nextmap[3]):
                currmap = (currmap + 1) % 5
                efface('map')
                texte(635, 290, maps[currmap][:-4], ancrage='center', tag='map') #current map
 

        mise_a_jour()
    ferme_fenetre()

#game("pistes/map_test.txt")

menu()