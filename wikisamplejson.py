# -*- coding: cp1252 -*-

import webbrowser
import math
import json
from pprint import *
import nltk 
import re
import wikitools
from wikitools import wiki
from wikitools import api
sentence="""Sony tiene nuevo tel�fono en su gama de entrada, se llama Sony Xperia E1, y curiosamente se ha decidido presentar fuera del CES, donde el Sony Xperia Z1 Compact iba a ser el protagonista. En el cat�logo de los japoneses tenemos tel�fonos de todos los tama�os, el nuevo llega para situarse en el primer escal�n, con una pantalla de cuatro pulgadas.
Si ya nos hab�an sorprendido con un dispositivo de �ltima tecnolog�a en tama�o relativamente peque�o como el Compact, ahora han decidido que tambi�n es posible un terminal con especificaciones moderadas, pero buen aspecto externo.
El Sony Xperia E1 cuenta con un dise�o similar al de su hermano m�s lujoso, y nos prometen que en la mano va a lucir muy parecido. Han aprovechado para enfocarlo m�s hacia el aspecto multimedia, con botones dedicados y un altavoz potente.
Esperamos las primeras tomas de contacto e im�genes reales para comprobar el tipo de materiales y construcci�n utilizados, por lo que vemos pinta bastante bien. Pasando a las especificaciones, son sencillas, como as� nos prueba su coraz�n Qualcomm de cuatro n�cleos, o la pantalla con resoluci�n WVGA (800�480 p�xeles). En la web oficial aseguran que es un MSM8210 de doble n�cleo, si nos vamos a la web de Qualcomm, eso corresponde con un Snapdragon 200, que �nicamente existe en configuraci�n de cuatro n�cleos.

Otras especificaciones que nos hablan de sus posibilidades reales son la justa memoria RAM � 512MB -, o los 4GB de memoria interna. Afortunadamente con KitKat, que es la versi�n Android con la que aparece en el mercado (est� por confirmar), hay espacio para tel�fonos menos capaces.
El otro aspecto llamativo del tel�fono es el potente altavoz trasero, tanto que registra 100dB � un terror para algunos -. Sony lo acompa�a de las tecnolog�as ClearAudio+ y xLoud para asegurar que el sonido adem�s se propaga con calidad. No se me olvida, la bater�a es de 1.700mAh.
El tel�fono presenta adem�s un bot�n dedicado Walkman, con �l podemos acceder directamente a la aplicaci�n multimedia, y tambi�n reconocer� nuestros gestos -agitar el m�vil � para ir cambiando de canci�n. Se regala un pase de 30 d�as al servicio de m�sica Sony Entertainment Network2.
Walkman

Entre los detalles que no nos gustan tanto � hab�a que recortar -, tenemos poca memoria interna, y la c�mara es muy sencilla � 3 megap�xeles -, ya que no cuenta con enfoque autom�tico ni est� acompa�ada por flash. Tampoco hay c�mara frontal.
Sony lo va a lanzar inicialmente en mercados emergentes � China, Oriente Medio, �frica y Asia-Pac�fico � , por lo que nos lo veremos por aqu�, o en Estados Unidos. Tampoco hay informaci�n concreta sobre precio o fechas de lanzamiento.
Para terminar de conocerlo, su conectividad se queda en 3G/HSPA+, contar� con versi�n Dual SIM, y estar� disponible en tres colores: blanco, negro y p�rpura. Por cierto, ha sido presentado a la par que una nueva phablet, Sony Xperia T2 Ultra.
Actualizaci�n: el blog especializado XperiaBlog se atreve a dar precios para Europa. Nos cuentan que el Xperia E1 costar� 129 euros en B�lgica, 139 euros en Alemania, y 149 euros en Holanda."""
text = nltk.word_tokenize(sentence)
tagged=nltk.pos_tag(text)
namedentities = nltk.chunk.ne_chunk(tagged,binary=True)
entities=re.findall(r'NE\s(.*?)/',str(namedentities))
arr= []
arr1 =set(entities)
for i in arr1:
    t = entities.count(i)
    arr.append([i,t])


    
print arr
w = 0
b = []
for i in range(len(arr)):
    w= w + arr[i][1]    
for i in range(len(arr)):
    temp = arr[i][1]*10/w
    if temp>1:
        b.append(math.floor(temp))
    else:   
        b.append(1)
print b

site = wiki.Wiki("http://commons.wikimedia.org/w/api.php")

for i in range(len(arr)):
    params = {'action':'query', 'titles': arr[i][0], 'prop' : 'images', 'redirects' : '1' }
    request = api.APIRequest(site, params)
    result = request.query()
    pprint(result)
    key = result['query']['pages'].keys()
    key2 = result['query']['pages'][key[0]].keys()
    if  key[0]== '-1' :
        continue
    if key2[0] == 'images':
        for z in range(3):
            a = result['query']['pages'][key[0]]['images'][z]['title']
            url = "http://commons.wikimedia.org/wiki/"+ a
            webbrowser.open(url,new=1)

    
