#!/usr/bin/python

import httplib
site=raw_input("Entrez l adresse du site :")
#httpServ= httplib.HTTPConnection("google.fr", 80 )
httpServ= httplib.HTTPConnection(site, 80 )
httpServ.connect()
httpServ.request('GET',("GET / HTTP/1.1 \n\n"))
response = httpServ.getresponse()
print "\n\n Voici la page \n\n",response.read()


