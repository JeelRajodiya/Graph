class Graph:
    def __init__(self,x,y,flag='*'):
        self.x=x
        self.y=y
        self.flag=flag
        self.maximum_on_x=(max(x)+1)*2
        self.maximum_on_y=max(y)+1
    def get_line(self,n_th):
        line=''
        number_of_y=self.y.count(n_th)
        
        if number_of_y==0:
            return str(n_th)+'|'+(' '*self.maximum_on_x)+' '
        elif number_of_y==1:
            for i in self.y:
                if i==n_th:
                    x=self.x[self.y.index(n_th)]*2
                    #     9    10     16
                    # *********5**************** 26
                    spaces_after=self.maximum_on_x-x
                    spaces_before=self.maximum_on_x-spaces_after
                    if spaces_before<0:
                        spaces_before=0
                    #print(spaces_before,self.maximum_on_x,spaces_after)
                    return str(n_th)+'|'+(' '*spaces_before)+self.flag+(' '*spaces_after)
        else:
            x=[]
            index=0
            for i in self.y:
                if i==n_th:
                    try:
                        x.append((self.x[index])*2)
                    except:
                        print(index)
                index+=1
            line=f'{n_th}|'
            for i in range(self.maximum_on_x+1):
                if i in x:
                    line+=self.flag
                else:
                    line+=' '
            return line
    def generate_graph(self):
        from functions import reversed_range
        graph_lines=[]
        for i in reversed_range(self.maximum_on_y):
            graph_lines.append(self.get_line(i))
        max_length=max(map(len,graph_lines))    
       
        for n,i in enumerate(graph_lines):
            graph_lines[n]=i.rjust(max_length)
        graph_lines[-1]=graph_lines[-1].replace(' ','_')
        temp1=0
        
        if graph_lines[-1][0]=='_':
            for i in graph_lines[-1]:
                if i=='0':
                    break
                temp1+=1
            print(temp1)
            graph_lines[-1]=(' '*temp1)+graph_lines[-1][temp1:]
        last_line=''
        tempx=0
        a=0
        for i in range(self.maximum_on_x):
            if tempx%2==0:
                last_line+=str(a)[-1]
                a+=1
            else:
                last_line+=' '
            tempx+=1
        del tempx
        last_line=last_line.rjust(max_length-1)
        graph_lines.append(last_line)

        
        return graph_lines
    

    

