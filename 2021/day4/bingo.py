
class Bingo:

    def __init__(self,content):
        self.rows = {
            0:0,
            1:0,
            2:0,
            3:0,
            4:0,
             }
        self.cols = {
            0:0,
            1:0,
            2:0,
            3:0,
            4:0,
             }
        self.content = []
        for i in content:
            self.content += list(map(lambda x: int(x) ,i.split()))

        

    def check_rows(self,value):
        if value in self.content:
            index_value = self.content.index(value)
            self.rows[index_value//5] += 1
            for row in self.rows.keys():
                if self.rows[row] == 5:
                    return row
            
        
        return -1
    
    def check_cols(self,value):
        if value in self.content:
            index_value = self.content.index(value)
            self.cols[index_value%5] += 1
            for col in self.cols.keys():
                if self.cols[col] == 5:
                    return col
        return -1

    def get_row(self, row):
        return self.content[row*5:(row*5)+5]
    
    def get_col(self, col):
        return [self.content[i+col] for i in range(0,len(self.content),5) ]

        
    def print_board(self):
        for i in range(0,len(self.content),5):
            print(self.content[i:i+5])
    
    def get_sum(self,content):
        val = 0
        for i in self.content:
            if i not in content:
                val += i
        
        return val * content[-1]

def solve1(content):
    boards = []
    for i in range(0,len(content),6):
        a = Bingo(content[i+1:i+6])
        boards.append(a)

    used = []
    found = None
    
    for number in random_numbers:
        used.append(number)
        for board in boards:
            row_val = board.check_rows(number)
            col_val = board.check_cols(number)
            if row_val > -1:
                found = board
                break
            if col_val > -1: 
                found = board
                break
        if found:
            break
    
    
    
    print(f"solution 1: {found.get_sum(used)}")

def solve2(content):
    boards = []
    for i in range(0,len(content),6):
        a = Bingo(content[i+1:i+6])
        boards.append(a)

    used = []
    
    found = []
    done = False
    for number in random_numbers:
        used.append(number)
        for board in boards:
            row_val = board.check_rows(number)
            col_val = board.check_cols(number)
            if (row_val > -1 or col_val > -1) and len(boards) > 1:
                if board not in found:
                    found.append(board)
            elif (row_val > -1 or col_val > -1) and len(boards)==1:
                print(f"solution 2 : {board.get_sum(used)}")
                done = True
                break
                
                
        if done:
            break
        if len(found) > 0:
            for b in found:
                boards.remove(b)
        found = [] 

if __name__=="__main__":

    with open("input.txt", "r") as fp:

        random_numbers = list(map(lambda x: int(x) ,fp.readline().split(",")))

        content = fp.readlines()

    solve1(content)
    solve2(content)
    

    
    
        

    
        


    
        
        