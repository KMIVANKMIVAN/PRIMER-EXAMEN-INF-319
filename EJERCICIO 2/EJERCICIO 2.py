# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:48:33 2021

@author: van
"""

from pyswip import Prolog

prolog=Prolog()
prolog.assertz("padrede('Juan', 'María')") #% Juan es padre de María
prolog.assertz("padrede('Pablo', 'Juan')") #% Pablo es padre de Juan
prolog.assertz("padrede('Pablo', 'Marcela')") #% Pablo es padre de Marcela
prolog.assertz("padrede('Carlos', 'Débora')") #% Carlos es padre de Débora

list(prolog.query("padrede(Juan,X)"))==[{'X':'María'},{'X':'Juan'}]

for elemento in prolog.query("padrede(X,Y)"):
    print(elemento["X"],"es el padre de ", elemento["Y"])