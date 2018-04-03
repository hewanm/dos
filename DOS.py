import urllib

url = "http://192.168.34.3/"
for i in range (0,425111685422):
    url=url + str(i)
    print(url)
    try:
        urllib2.open(url)
        print ("DOS attack")
    except:
        pass
        
    
