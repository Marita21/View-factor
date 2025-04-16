def functionviewfactorarea(pt1,pt2,normale,t):

    #Global variables: pt1 to pt2 are the points that define the segment to integrate, normale is the unit normal vector.
    #global pt1;
    #global pt2;
    #global normale;

    #Parametric equations of the segment that join pt1 to pt2
    x=pt1[0]+(pt2[0]-pt1[0])*t#TO CHECK: removed a forced float
    y=pt1[1]+(pt2[1]-pt1[1])*t
    z=pt1[2]+(pt2[2]-pt1[1])*t

    #Function to integrate to calculate the area of a figure
    partieaire=normale[1]*z*(pt2[0]-pt1[0])+normale[2]*x*(pt2[1]-pt1[1])+normale[0]*y*(pt2[2]-pt1[2])
    return partieaire
