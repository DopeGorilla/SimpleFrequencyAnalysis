#!/usr/bin/python

import os, sys, matplotlib.pyplot as plt, string, numpy as np
from decimal import *

def Usage():
    print "Usage: "+sys.argv[0]+" <File or Text>"
    exit()

def relativeFrequency():
    y=[.08167,.01492,.02782,.04253,.12702,.02228,.02015,.06094,.06966,.00153,.00722,.04025,.02406,.06749,.07507,.01929,.00095,.05987,.06327,.09056,.02758,.00978,.02360,.00150,.01974,.0074]
    return y

def freq(ciphertext):
    letters = [['A', 0], ['B', 0], ['C', 0], ['D', 0], ['E', 0], ['F', 0], ['G', 0], ['H', 0], ['I', 0], ['J', 0], ['K', 0], ['L', 0], ['M', 0], ['N', 0], ['O', 0], ['P', 0], ['Q', 0], ['R', 0], ['S', 0], ['T', 0], ['U', 0], ['V', 0], ['W', 0], ['X', 0], ['Y', 0], ['Z', 0]]
    length=len(ciphertext)-1
    for i in letters:
       i[1]=Decimal(ciphertext.count(i[0]))/Decimal(length)
    return letters

def frequencyAnalysis(cipher):
    result=freq(cipher)
    ind = range(1,27)
    width=.35
    fig, ax=plt.subplots()
    rects1= ax.bar(ind,getIndex(result,1),width,color='r')
    std=relativeFrequency()
    ind2 =[]
    for i in range(0,len(ind)):
        ind2.append(ind[i]+width)
    rects2=ax.bar(ind2,std,width,color='g')
    ax.set_title('Letter Frequencies')
    ind3=[]
    for i in range(0,len(ind)):
        ind3.append(ind[i]+width/2)
    ax.set_xticks(ind3)
    labels=[]
    for b in string.uppercase:
        labels.append(b)
    ax.set_xticklabels(labels)
    ax.legend([rects1[0],rects2[0]],['Ciphertext','English'])
    plt.show()

def Vigenere(cipher):
    keylength=None
    while keylength is None:
        try:
            keylength=int(raw_input("How long is the Key?"))
        except ValueError:
            print "Type in an integer value."
    
    width=.35
    ciphers=['']*keylength
    cipherfreq=[0]*keylength
    ind=np.arange(1,26*(keylength*width+2*width),keylength*width+2*width)
    print ind
    print len(ind)

    for i in range(0,len(cipher)-1):
        ciphers[i%keylength]=ciphers[i%keylength]+cipher[i]
    colors=['#F44366','#9C27B0','#3F51B5','#2196F3','#00BCD4','#009688','#4CAF50','#8BC34A','#CDDC39','#FFEB3B','#795548']
    colorindex=0
    rects=[]
    fig,ax =plt.subplots()
    for i in range(0,keylength):
        cipherfreq[i]=freq(ciphers[i])
        indtemp=[]
        for x in range(0,len(ind)):
            indtemp.append(ind[x]+width*i)
        print "For "+str(i)+" ",indtemp
        rects.append(ax.bar(indtemp,getIndex(cipherfreq[i],1),width,color=colors[colorindex]))
        del indtemp
        colorindex+=1
    ind2=[]
    ind3=[]
    for i in range(0,len(ind)):
        ind2.append(ind[i]+width*keylength)
        ind3.append(ind[i]+(width*keylength)/2)
    rects.append(ax.bar(ind2,relativeFrequency(),width,color='b'))

    ax.set_xticks(ind3)
    labels=[]
    for b in string.uppercase:
        labels.append(b)
    ax.set_xticklabels(labels)
    legendrect=[]
    legend=[]
    for b in rects:
        legendrect.append(b[0])
    for c in range(0,len(rects)-1):
        legend.append('Index '+str(c))
    legend.append('English')

    ax.legend(legendrect,legend)
    plt.show()



def getIndex(lists,index):
    ret=[]
    for p in lists:
        ret.append(p[index])
    return ret

def main():
    if len(sys.argv) != 2:
        Usage()
    cipher=''
    if os.path.exists(sys.argv[1]):
        f = open(sys.argv[1], 'r')
        cipher=f.read()
    else:
        cipher=sys.argv[1]
    ans=True
    while ans:
        print ("""        1. Frequency Analysis
        2. Vigenere Frequency Analysis
        3. Exit""")
        ans=raw_input()
        if ans =="1":
            frequencyAnalysis(cipher.upper())
        elif ans=="2":
            Vigenere(cipher)
        elif ans =="3":
            exit()
        else:
            print ("Invalid Choice")


if __name__=="__main__":
    main()
        
