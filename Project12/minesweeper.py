'''A program to take a given 'minesweeper' grid and return the completed version. 
Using 2D lists as rows and columns to check if each value is a '-' counts the mines in a ring around it'''

grid = [["-","-","-","#","#"],       #input grid
["-","#","-","-","-"],
["-","-","#","-","-"],
["-","#","#","-","-"],
["-","-","-","-","-"]]

def is_mine(grid):       #function is_mine with one input of a grid
    rows = len(grid)             #in this case row would be 5 as there are 5 items in grid
    cols = len(grid[0])          #each item is the same len so using the len of the first item for col
    for i, row in enumerate(grid):
        for j, col in enumerate(row):           #nested loop for each item. enumerate to get the index/ position
            if col == "-":
                counter = 0                    #placeholder
                if i>0 and j>0 and grid[i-1][j-1] == "#":
                    counter +=1
                if i>0 and grid[i-1][j] == "#":
                    counter +=1          
                if i>0 and j<cols-1 and grid[i-1][j+1] == "#":     #if loops for each item around and exception of outliers
                    counter +=1
                if j>0 and grid[i][j-1] == "#":
                    counter +=1           
                if j<cols-1 and grid[i][j+1] == "#":
                    counter +=1                
                if i<rows-1 and j>0 and grid[i+1][j-1] == "#":
                    counter +=1
                if i<rows-1 and grid[i+1][j] == "#":
                    counter +=1
                if i<rows-1 and j<cols-1 and grid[i+1][j+1] == "#":
                    counter +=1   

                grid[i][j]=str(counter)           
    return grid
test = is_mine(grid)    #calling the function
for row in test:
    [print(row)]   

