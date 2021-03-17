
import math
done=None
rows=0
cols=0
def strokesRequired(picture):
    global done,rows,cols
    rows=len(picture)
    cols=len(picture[0])
    done =[[False]*cols for i in range(rows)]
    def do_all(i,j,curr,picture):
        global done
        if (i<rows and i>=0 and j-1<cols and j-1>=0) :
            if  picture[i][j-1]==curr and done[i][j-1]==False:
                done[i][j-1]=True
                do_all(i,j-1,curr,picture)
        if (i<rows and i>=0 and j+1<cols and j+1>=0):
            if picture[i][j+1]==curr and done[i][j+1]==False:
                done[i][j+1]=True
                do_all(i,j+1,curr,picture)
        if (i+1<rows and i+1>=0 and j<cols and j>=0) :
            if picture[i+1][j]==curr and done[i+1][j]==False:
                done[i+1][j]=True
                do_all(i+1,j,curr,picture)
        if (i-1<rows and i-1>=0 and j<cols and j>=0) :
            if picture[i-1][j]==curr and done[i-1][j]==False:
                done[i-1][j]=True
                do_all(i-1,j,curr,picture)
    ans=0
    for i in range(rows):
        for j in range(cols):
            if done[i][j]:
                continue
            done[i][j]=True
            ans+=1
            do_all(i,j,picture[i][j],picture)
    return ans
    
