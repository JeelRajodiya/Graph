from classe import Graph
def generate_graph(*args,**kwargs):
    if type(args[0]) is tuple:
        x=[]
        y=[]
        for i in args:
            _x,_y=i
            x.append(_x)
            y.append(_y)
    else:
        x=args[0]
        y=args[1]
    my_graph=Graph(x,y)
    graph_lines=my_graph.generate_graph()
    if kwargs.get('mode') is None:

        for i in graph_lines:
            print(i)
    else:
        return graph_lines
#smile=[(1, 4),(1, 6),(2, 4),(2, 6),(3, 4),(3, 6),(1, 5),(3, 5),(6, 4),(6, 6),(7, 4),(7, 6),(8, 4),(8, 6),(6, 5),(8, 5),(2,2),(3,1),(4,1),(5,1),(6,1),(7,2)]
#print(generate_graph(*smile))
        