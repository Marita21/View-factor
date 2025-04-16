from viewfactor import viewfactor


if __name__=='__main__':
    FACTOR12,FACTOR21,AREA1,AREA2=viewfactor([[0,0,0],[1,0,0],[0,1,0]],[[0,0,1],[2,0,1],[0,2,1]],6);
    print(FACTOR12,FACTOR21,AREA1,AREA2) #

    print(viewfactor([[0,0,0],[1,0,0],[1,1,0],[0,1,0]],[[0,0,1],[2,0,1],[0,2,1]],6))
   
    print(viewfactor([[0,0,0],[1,0,0],[0,1,0]],[[0,0,1],[2,0,1],[0,2,1]],6))
