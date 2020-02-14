# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:31:14 2019

@author: andre
"""

import owlready2

from owlready2 import get_ontology

help (owlready2)

from owlready2 import onto_path

onto_path.append("C:/Users/andre/Dropbox/André Rosa/FACULDADE/Doutorado/TESE/GERAÇÃO DE LINGUAGEM COM O PYTHON/NLG_BRAZILIAN_PORTUGUESE_SPYDER/ONTOLOGY")

#TESTE_BASE = get_ontology("file:///Users/andre/Dropbox/André Rosa/FACULDADE/Doutorado/TESE/GERAÇÃO DE LINGUAGEM COM O PYTHON/NLG_BRAZILIAN_PORTUGUESE_SPYDER/ONTOLOGY/TESTE_IMPORT_PY.owl").load()
#
#
#TESTE_BASE.classes()
#list(TESTE_BASE.classes())




GUM =  get_ontology ("file:///Users/andre/Dropbox/André Rosa/FACULDADE/Doutorado/ONTOLOGIAS/GUM-3-space.owl").load ()
GUM.classes()
list(GUM.classes())
len(GUM.classes())
GUM.individuals()
x = ('1','2','3')

type (x)
len(x)
list(GUM.object_properties())


individuals = list(GUM.individuals())

type (individuals)


y=individuals[4]
type(x)
type(y)

help(slice)
help(type)




base_conhecimento = get_ontology("file:///Users/andre/Dropbox/André Rosa/FACULDADE/Doutorado/TESE/TESTE_IMPORT_PY.owl").load()

help(get_ontology)

base_conhecimento.classes()
list(base_conhecimento.classes())
onto=  get_ontology ("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl").load ()
onto.classes()
onto.individuals()
list(onto.classes())
list(onto.individuals())




