import numpy as np
import scipy.integrate as integrate
from functionviewfactorarea import functionviewfactorarea
from functionintegral import functionintegral

def viewfactor(figure1,figure2,niveau):
    #How many vertices on each figures?
    nbpoint1,nbcoord1=np.array(figure1).shape
    nbpoint2,nbcoord2=np.array(figure2).shape

    #We add the first point as the last point to close the outline of the figure
    figure1.append(figure1[0])
    figure2.append(figure2[0])


    #make it a numpy array
    figure1=np.array(figure1)
    figure2=np.array(figure2)

    #Unit normal vector of figure 1
    cote1=figure1[1]-figure1[0]
    cote2=figure1[2]-figure1[0]
    normale1=np.cross(cote1,cote2)/(np.linalg.norm(np.cross(cote1,cote2)))

    #Unit normal vector of figure 2
    cote1=figure2[1]-figure2[0]
    cote2=figure2[2]-figure2[0]
    normale2=np.cross(cote1,cote2)/(np.linalg.norm(np.cross(cote1,cote2)))






    ##Preliminar calculation of area to determine which precision to use in calculation to respect the number of significant digits
    aire1temp=0;
    normale=normale1;
    for i in range(0,nbpoint1):
        pt1=figure1[i]
        pt2=figure1[i+1]

        #Integration to calculate the area of figure 1
        #aire1temp=aire1temp+integral('functionviewfactorarea',0,1);%,0.1);# this part is
         #%aire1temp=aire1temp+quadl('functionviewfactorarea',0,1,0.1);    #commented out in the original code...

    aire1temp=abs(aire1temp)
    #prec=10**(-niveau)/(nbpoint1*nbpoint2/(2*np.pi*aire1temp)+nbpoint1/aire1temp)

    ##The calculation of area of figure 1 with the right precision.
    aire1=0
    normale=normale1
    for i in range(0,nbpoint1):
        pt1=figure1[i]
        pt2=figure1[i+1]
        #Integration to calculate the area of figure 1
        aire1=aire1+integrate.quad(lambda t:functionviewfactorarea(pt1,pt2,normale,t),0,1)[0]

    aire1=abs(aire1)

    ##The calculation of area of figure 1 with the right precision.
    aire2=0;
    normale=normale2;
    for i in range(0,nbpoint2):
        pt1=figure2[i]
        pt2=figure2[i+1]
        #Integration to calculate the area of figure 2
        aire2=aire2+integrate.quad(lambda t:functionviewfactorarea(pt1,pt2,normale,t),0,1)[0]

    aire2=abs(aire2)

    #prec=3;

    #Double integral that we need to calculate the view factor
    sommeintegrale=0;
    for i in range(0,nbpoint1):
        for j in range(0,nbpoint2):
            pt1=figure1[i]
            pt2=figure1[i+1]
            pt3=figure2[j]
            pt4=figure2[j+1]
            sommeintegrale=sommeintegrale+integrate.dblquad(lambda s,t:functionintegral(pt1,pt2,pt3,pt4,normale1,normale2,s,t),0,1, lambda x: 0, lambda x: 1)[0]



    #Calculation of the view factors
    facteur12=abs(sommeintegrale)/(2*np.pi*aire1);
    facteur21=abs(sommeintegrale)/(2*np.pi*aire2);

    return facteur12,facteur21,aire1,aire2
