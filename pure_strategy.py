class NashEquilibrium:
    def __init__(self, matrix):
        self.payout_matrix=matrix
        self.row_labels=list(range(len(self.payout_matrix)))
        self.col_labels=list(range(len(self.payout_matrix[0])))

    def find_pure_strategy_nash_equilibria(self):
        nash_equilibria = []
        
        payoff_matrix_player1 = [[cell[0] for cell in row] for row in self.payout_matrix]
        payoff_matrix_player2 = [[cell[1] for cell in row] for row in self.payout_matrix]
        
        num_strategies_player1 = len(payoff_matrix_player1)
        num_strategies_player2 = len(payoff_matrix_player2[0])
        
        best_responses_player1 = [None] * num_strategies_player2
        for j in range(num_strategies_player2):
            best_responses_player1[j] = max(range(num_strategies_player1), 
                                            key=lambda i: payoff_matrix_player1[i][j])
        
        best_responses_player2 = [None] * num_strategies_player1
        for i in range(num_strategies_player1):
            best_responses_player2[i] = max(range(num_strategies_player2), 
                                            key=lambda j: payoff_matrix_player2[i][j])
        
        for i in range(num_strategies_player1):
            for j in range(num_strategies_player2):
                if best_responses_player1[j] == i and best_responses_player2[i] == j:
                    nash_equilibria.append((self.row_labels[i], self.col_labels[j]))
                    
        return nash_equilibria
    
    def print_pure_strategies(self):
        equilibria = self.find_pure_strategy_nash_equilibria()
        if not equilibria:
            print("No pure strategy Nash equilibria found.")
        else:
            for eq in equilibria:
                print(f"Pure strategy Nash equilibrium: Player 1 plays {eq[0]}, Player 2 plays {eq[1]}")



    def remove_dominated_p1(self):
        row_num=len(self.payout_matrix)
        col_num=len(self.payout_matrix[0])
        max_values=[]
        for c in range(col_num):
            max_payout=max([self.payout_matrix[r][c][0] for r in range(row_num)])
            rows_to_keep=set()
            for r in range(row_num):
                if self.payout_matrix[r][c][0] == max_payout:
                    rows_to_keep.add(r)
                max_values.append(rows_to_keep)

        rows_to_keep=[]
        while max_values:
            maximum_intersection= max_values[0].copy()
            for c in range(1, len(max_values)):
                if len(maximum_intersection & max_values[c]) !=0:
                    maximum_intersection = maximum_intersection & max_values[c]
            
            max_index= maximum_intersection.pop()
            rows_to_keep.append(max_index)
            max_values=[row for row in max_values if max_index not in row]
        
        new_matrix= [self.payout_matrix[i] for i in sorted(rows_to_keep)]
        self.payout_matrix= new_matrix
        self.row_labels=[self.row_labels[i] for i in sorted(rows_to_keep)]
        return row_num !=len(rows_to_keep)

    def remove_dominant_p2(self):
        row_num=len(self.payout_matrix)
        col_num=len(self.payout_matrix[0])
        max_values=[]
        for r in range(row_num):
            max_payout=max([self.payout_matrix[r][c][1] for c in range(col_num)])
            cols_to_keep=set()
            for c in range(col_num):
                if self.payout_matrix[r][c][1]==max_payout:
                    cols_to_keep.add(c)
            max_values.append(cols_to_keep)

        cols_to_keep=[]
        while max_values:
            maximum_intersaction = max_values[0].copy()
            for c in range(1, len(max_values)):
                if len(maximum_intersaction & max_values[c])!=0:
                    maximum_intersaction = maximum_intersaction & max_values[c]
                
            max_index=maximum_intersaction.pop()
            cols_to_keep.append(max_index)
            max_values= [col for col in max_values if max_index not in col]
            
        new_matrix=[[] for _ in range(row_num)]
        for c in sorted(cols_to_keep):
            for r in range (row_num):
                new_matrix[r].append(self.payout_matrix[r][c])
        self.payout_matrix = new_matrix
        self.col_labels = [self.col_labels[i] for i in sorted(cols_to_keep)]
        return col_num != len(cols_to_keep)
    
    
