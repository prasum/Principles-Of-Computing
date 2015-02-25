"""
Merge function for 2048 game.
"""

    

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    line2=[]
    line3=[]
    line4=[]
    pair=0
    shift=0
    line1=[0]*len(line)
    if(len(line)==1):
        for iota in line:
            line1[0]=iota
        return line1
    
    for iota in xrange(len(line)):
        line4.append(line[iota])
        
    for iota in xrange(len(line)):
        line3.append(line[iota])
        
        
    
    for xinn in xrange(len(line3)):
        for iota in xrange(len(line3)-1):
            if(line3[iota]==0):
                if((line3[iota+1])>0):
                    temp=line3[iota];
                    line3[iota]=line3[iota+1];
                    line3[iota+1]=temp
                    shift=1
        xinn=xinn+1
                
                
    if(shift==1):
        for iota in xrange(len(line3)):
            line2.append(line3[iota])
    else:
         for iota in xrange(len(line4)):
            line2.append(line4[iota])
            
    
        
                
            
    
                
    for olay in range(len(line2)-1):
     
            
        if(line2[olay]==line2[olay+1]):
            line1[olay]=2*line2[olay];
            line2[olay+1]=0
            line1[olay+1]=line2[olay+1]
            pair=1;
            olay=olay+2
        else:
            line1[olay]=line2[olay]
            line1[olay+1]=line2[olay+1]
            
        
            
    
            
            
    
                
        
    
    if(pair==0):
        for lonn in xrange(len(line3)):
            line1[lonn]=line3[lonn]
        return line1
        
    
        
    for xinn in xrange(len(line1)):
        for iota in xrange(len(line1)-1):
            if(line1[iota]==0):
                if((line1[iota+1])>0):
                    temp=line1[iota];
                    line1[iota]=line1[iota+1];
                    line1[iota+1]=temp
        
        xinn=xinn+1
        
    return line1





                