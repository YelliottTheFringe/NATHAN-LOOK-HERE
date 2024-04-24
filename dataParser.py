import sys as s
def c (data):
    s.stdout.write(str(data))
    s.stdout.flush()
def parseOutDouble(coords):
    outString=''
    for i in range(0,2):
        for v in range(0,2):
            outString+=str(coords[i][v])
            outString+='-'
    return(outString.encode())
def parseInDouble(data):
    coords=[]
    num_holder=''
    for i in data.decode():
        if i=="-":
            coords.append(num_holder)
            num_holder=''
        else:
            num_holder+=i
    coords.append(num_holder)
    coordA=(int(coords[0]),int(coords[1]))
    coordD=(int(coords[2]),int(coords[3]))
    return coordA,coordD
def parseOutSingle(data):
        outString=''
        for v in range(0,2):
            outString+=str(data[v])
            outString+='-'
        return(outString.encode())
def parseInSingle(data):
    coords=[]
    num_holder=''
    for i in data.decode():
        if i=="-":
            coords.append(num_holder)
            num_holder=''
        else:
            num_holder+=i
    coords.append(num_holder)
    coordA=(int(coords[0]),int(coords[1]))
    return coordA