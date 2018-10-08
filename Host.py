# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:43:03 2018

@author: Yorhagy
"""

import socket
import requests

#%%
def InformacionSitio(host) :
    url = 'http://' + host 
    ip = socket.gethostbyname(host)
    response = requests.get(url)
    
    if 'server' in response.headers: 
        server = response.headers['server']
    else:
        server = 'unknown'
    if 'Content-Encoding' in response.headers:
        contentEncoding = response.headers['content-encoding']
    else:
        contentEncoding = 'unknown'
    if 'Content-Type' in response.headers:
        contentType = response.headers['content-type'] 
    else:
        contentType = 'unknown'

    info = {'Host' : host,"ip" : ip,'Server' : server, 
        "Content-Encoding" : contentEncoding,'Content-Type' : contentType}
    
    # Guardar datos
    file = open('informacion.txt', 'a')
    file.write('Host: %s\n' % (info['Host']) )
    file.write('IP: %s\n' % (info['ip']))
    file.write('Server: %s\n' % (info['Server']))
    file.write('Content-Encoding: %s\n' % (info['Content-Encoding']))
    file.write('Content-Type: %s\n\n' % (info['Content-Type']))
    file.close()
    
#%% 
InformacionSitio('youtube.com')