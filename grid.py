STUDENT_NAME = "Deirick Rosas"

class Cell:
    """The cells to go on the grid"""
    
    def __init__(self, cell_type):
        """Intialize the cell that will be a single spot on the grid
        
        Args:
            cell_type (str): the type of cell on the grid. It can be base, tower, or path
        """
        
        self.cell_type = cell_type
        
class Grid:
    """The grid to be filled with cell objects"""
    
    def __init__(self, size):
        """Initialize the grid to build the row and be filled cell objects
        
        Args:
            size (int): the length of row   
        """
        
        self.size = size
        self.row = []
        
    def add_row (self):
        """Method to create cell and fill a row by looping self.size and appending
        to self.row"""
        
        for index in range(self.size):
            if index == self.size -1:
                self.row.append(Cell("B"))
            else:
                self.row.append(Cell("P"))
                
    def place_tower(self, index):
        """Place a tower in a cell at a given index"""
        
        if self.row[index].cell_type == "P": #check if cell is a path
            self.row[index].cell_type = "T" #place a tower
                
    def display(self):
        """Prints the grid row"""
        
        for cell in self.row: #loop through cells in the row
            print (cell.cell_type, end=" ") #prints cell type and keep it one line
        print()
        
if __name__ == "__main__":
    g = Grid(10)
    g.add_row()
    g.place_tower(4)
    g.display()