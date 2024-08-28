def pertenece (seq,n):
    for i in seq:
        if i == n:
            return True
        else: 
            pass


def masLarga (s1,s2):
    if len(s1)>len(s2):
        return s1
    else:
        return s2

def mezclar(s1,s2):
    seq = 0
    i = 0
    s = ""
    if len(s1)>len(s2):
        print(len(s1))
        seq = s1
        seqCorta = s2
    else:
        print(len(s2))
        seq = s2
        seqCorta = s1
    for i in range(0,len(seqCorta)):
        print(s)
        s = s + s1[i]
        s = s + s2[i]
    for j in range(len(seqCorta),len(seq)):
        s = s + seq[j]

    return s
def traductorGeringoso(seq):
    s = ""
    vocales = ["a","e","i","o","u"]
    dic = {}
    for j in range (0,len(seq)):
        for i in range(0, len(seq[j])):
            s = s+ seq[j][i]
            if seq[j][i] in vocales:
                s = s + "p" + seq[j][i]
        dic[seq[j]] = s
        s = ""
    return dic
print(traductorGeringoso(['banana', 'manzana', 'mandarina']))