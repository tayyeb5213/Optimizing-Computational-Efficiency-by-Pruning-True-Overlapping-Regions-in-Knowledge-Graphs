'''
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import FOAF, RDF

g = Graph()
g.bind("foaf", FOAF)

bob = URIRef("http://example.org/people/Bob")
linda = BNode()  # a GUID is generated

name = Literal("Bob")
age = Literal(24)

g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.name, name))
g.add((bob, FOAF.age, age))
g.add((bob, FOAF.knows, linda))
g.add((linda, RDF.type, FOAF.Person))
g.add((linda, FOAF.name, Literal("Linda")))

print(g.serialize())
'''

'''
import matplotlib.pyplot as plt

x_axis = [500, 1000, 2000, 4000, 8000,16000]

y_axis = [69,68,67,64,63,61]
y_ax = [78,76,74,73,70,69]

y_a = [57,55,53,51,49,45]

y_b = [64,63,62,61,59,58]

y_c = [72,72,70,68,67,54]

y_d = [57,59,60,58,57,56]


plt.plot(x_axis, y_axis, color='lightgrey')
plt.plot(x_axis, y_axis, 'o-', color='lightgrey', label='No mask')

plt.plot(x_axis, y_ax, color='red')
plt.plot(x_axis, y_ax, 'o-', color='red', label='value1')

plt.plot(x_axis, y_a, color='green')
plt.plot(x_axis, y_a, 'o-', color='green', label='value2')

plt.plot(x_axis, y_b, color='blue')
plt.plot(x_axis, y_b, 'o-', color='blue', label='No mask')

plt.plot(x_axis, y_c, color='black')
plt.plot(x_axis, y_c, 'o-', color='black', label='value4')

plt.plot(x_axis, y_d, color='orange')
plt.plot(x_axis, y_d, 'o-', color='orange', label='value4')


plt.xlim(1, 18000)
plt.ylim(1, 100)
plt.title('Reduction of triples for specifc Property')
plt.xlabel('Number of Triples')
plt.ylabel('% age Reduction')
plt.legend()
plt.show()
'''


import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)

plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')

plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')

plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
             label='uplims=True, lolims=True')

upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
             label='subsets of uplims and lolims')

plt.legend(loc='lower right')