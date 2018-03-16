def count_(dic):
    a,b,indexx=0,0,0
    for ss in dic:
        if ss=='{':
            a+=1
        elif ss=='}':
            b+=1
        if a==b:
            return indexx
            
        indexx+=1
