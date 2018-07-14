#
#
# for now let's assume t hat the prob_detection is constant

def bayes_probability(a,b,false_detection = None):
    if false_detection is None:
        false_detection = .999999999999999999999
    else:
        num = (a*false_detection)
        denom = ((false_detection*a)+(b*(1-a)))
        return num/denom


class Grid():
    def __init__(self, m, n, x, y, prob_detection, false_detection):
        self.m = m
        self.n = n
        self.Grid = []
        self.object_location = [x,y]
        self.prob_detection = prob_detection
        self.false_detection = false_detection
        self.steps = 0
        self.max_search_list = []
        self.max = ()

    def grid(self):
        j = 0
        while j < self.m:
            row = []
            i = 0
            while i < self.n:
                row.append('')
                i = i + 1
            self.Grid.append(row)
            j = j + 1

    def print_grid(self):
        for row in self.Grid:
            print(row)

    def update_item(self, m, n,update):
        self.Grid[m][n] = update


    def search_grid(self):
        #
        # This is a basic search where we search through each grid
        #
        for row in self.Grid:
            for column in row:
                if self.object_location != [row, column]:
                    self.steps = self.steps + 1
                    self.p(row, column)

    def max_search_grid(self):
        if len(self.max_search_list) > 0:
            for coordinate in self.max_search_list:
                self.p(coordinate[0], coordinate[1])


    def z(self, m, n):
        if [m,n] == [self.object_location[0], self.object_location[1]]:
            z = 1
        else:
            z = 0
        return z

    def p(self, m, n):
        z = self.z(m,n)
        pi = bayes_probability(z,self.prob_detection,self.false_detection)
        pi_new = ((1-pi)*self.Grid[m][n])/(1-pi*self.Grid[m][n])
        if pi_new > self.max[0]:
            self.max = (pi_new,m,n)
            self.max_search_list.insert((pi_new, m, n))
            self.max_Search_list.remove((self.Grid[m][n],m,n))
        else:
            for i in range(len(0, self.max_search_list)):
                if pi_new > self.max_search_list[i][0]:
                    self.max_search_list = self.max_search_list[:i]+[(pi_new,m,n)]+self.max_search_list[i:]
                    self.max_search_list.remove((self.Grid[m][n],m,n))
        self.update_item(m,n,pi_new)
