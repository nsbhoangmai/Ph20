# -*- coding: utf-8 -*-
"""
Created on Thu May  3 01:30:24 2018

@author: nsbho
"""

def load_num(filename):
    """
    Load variables x0, v0, t, h from a plain-text file and return these 
	 as a list.
    """
    with open(filename) as vari:
        A0 = vari.read().split()
        A1 = []
        for i in A0:
            i1 = float(i)
            A1.append(i1)
        return A1


# def save_image(filename, image):
    """
    Save a list of [word, count, percentage] lists to a file, in the form
    "word count percentage", one tuple per line.
    """
    # with open(filename, 'wb') as f:
        # f.write(image)