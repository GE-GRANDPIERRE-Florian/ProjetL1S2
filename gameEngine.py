import math
from fltk import (cercle)


def find_neighbors(tab, point):

    """Find the neighbors , if they exist , of a point with his coordinate

    Returns:
        list: list of tuples with coordinate
    """

    neighbors = []
    rows = len(tab)
    col = len(tab[0])

    if point[1] > (rows-1) or point[0] > (col-1):
        return "Inexistant Point"

    for i in range(point[0]-1, point[0]+2):
        for j in range(point[1]-1, point[1]+2):
            if 0 <= i < col and 0 <= j < rows:
                neighbors.append((i, j))

    return neighbors


##### flo
def speed(traj):
    """Calculate the speed of the movement.

    Args:
        traj (list): contain the coordinate of the past points

    Returns:
        list: a speed vector
    """
    return [traj[-1][0] - traj[-2][0], traj[-1][1] - traj[-2][1]]

# Example :
#traj = [ (1,1), (1,2), (2,4), (3,5), (5,5) ]

def next(speed, traj, track_chain):
    """ Calculate the next possible choice of points"""
    point = (traj[-1][0] + speed[0], traj[-1][1] + speed[1])
    return point, find_neighbors(track_chain, point)


def clic_neighbors(lst, wid, hei, x, y, r, traj):
    """ Check if the clicked point is in the neighbors list"""
    for pnt in lst:
        abs = (pnt[0]+ 1) * (wid)
        ord = (pnt[1]+ 1) * (hei)
        distance = math.sqrt((abs - x)**2 + (ord - y)**2)
        # Test taille zone clic
        #cercle(abs , ord , r, couleur = 'red')
        if distance <= r:
            return pnt
    return traj[-1]


def lose(tab, point):
    """Check if the player win

    Args:
        tab (lst): map
        point (tuple): point coordinate

    Returns:
        bol: response of the question
    """
    if tab[point[1]][point[0]] == '#':
        return False
    else:
        return True

def win(tab, point):
    """Check if the player win

    Args:
        tab (lst): map
        point (tuple): point coordinate

    Returns:
        bol: response of the question
    """
    if tab[point[1]][point[0]] == '*':
        return False
    else:
        return True

def point_placement(fle):
    """ Calculate the starting point of the race"""
    for line in range(len(fle)):
        for elt in range(len(fle[line])):
            if fle[line][elt] == ">":
                return (elt, line)
