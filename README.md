# Graph
a simple python to create graph in console

# run the demo file.


###################################################################################################
																								  #	
 	ways of passing arguments																	  #	
 	1. by list																					  #		
 	   x=[1,2,3,4,5]																			  #			
 	   y=[1,2,3,3,3]																			  #		
 	   generate_graph(x,y)																		  #	
 																								  #
 	2. by tuples  [ (x1,y1) , (x2,y2) , (x3,y3) .... , (x10,y10)]								  #
      data=[(1,1),(2,2),(3,3),(4,3),(5,3)]            #this will generate graph as same as above #
      generate_graph(*data)  																	  #
  																								  #
																								  #
###################################################################################################


# Example
x=[1,2,3,4,5,6,7]
y=[1,2,3,4,3,2,1]
generate_graph(x,y)

>>>
5|                 
4|        *        
3|      *   *      
2|    *       *    
1|  *           *  
0|_________________
  0 1 2 3 4 5 6 7 
 
