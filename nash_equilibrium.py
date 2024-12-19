import numpy as np

class NashEquilibrium:
    def __init__(self, matrix, row_labels=None, col_labels=None):
        self.payout_matrix=matrix
        self.original_row_labels = row_labels if row_labels else list(range(len(self.payout_matrix)))
        self.original_col_labels = col_labels if col_labels else list(range(len(self.payout_matrix[0])))
        self.row_labels = self.original_row_labels.copy()
        self.col_labels = self.original_col_labels.copy()


    def print_matrix(self):
        print("\nPayoff Matrix:")
        cell_width = 10
        header_separator = "+" + "-".join(["-" * cell_width] * len(self.col_labels)) + "+"
        print(header_separator)
        for row in self.payout_matrix:
            row_str = "|".join([f" {cell[0]:>5},{cell[1]:>5} " for cell in row])
            print(f"|{row_str}|")
            print(header_separator)



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
            print("\nPure Strategies: None")
        else:
            pure_str = ", ".join(f"({eq[0]},{eq[1]})" for eq in equilibria)
            print(f"\nPure Strategies: {pure_str}")



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

    def remove_dominated_p2(self):
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
    

    def remove_dominated_moves(self):
        while self.remove_dominated_p1() | self.remove_dominated_p2():
            pass


    def mixed_strategy(self):
        self.remove_dominated_moves()
        p1_probabilities = {}
        p2_probabilities = {}

        col_length = len(self.payout_matrix[0])
        row_length = len(self.payout_matrix)

        if col_length == 1 and row_length == 1:
            p1_probabilities[self.row_labels[0]] = 1.0
            p2_probabilities[self.col_labels[0]] = 1.0
            return p1_probabilities, p2_probabilities
        
        p1_outcomes = [[1] * row_length]
        for c in range(1, col_length):
            p1_outcomes.append([self.payout_matrix[r][c][1] - self.payout_matrix[r][0][1] for r in range(row_length)])
        p1_solutions = [1] + [0] * (row_length - 1)
        p1_outcomes = np.linalg.solve(np.array(p1_outcomes), np.array(p1_solutions))
        for r in range(len(self.row_labels)):
            p1_probabilities[self.row_labels[r]] = p1_outcomes[r]

        p2_outcomes = [[1] * col_length]
        for r in range(1, row_length):
            p2_outcomes.append([self.payout_matrix[r][c][0] - self.payout_matrix[0][c][0] for c in range(col_length)])
        p2_solutions = [1] + [0] * (col_length - 1)
        p2_outcomes = np.linalg.solve(np.array(p2_outcomes), np.array(p2_solutions))
        for c in range(len(self.col_labels)):
            p2_probabilities[self.col_labels[c]] = p2_outcomes[c]

        for label in self.original_row_labels:
            if label not in self.row_labels:
                p1_probabilities[label] = 0.0
        for label in self.original_col_labels:
            if label not in self.col_labels:
                p2_probabilities[label] = 0.0

        return p1_probabilities, p2_probabilities

    def print_mix_strategies(self):
        equilibrium = self.mixed_strategy()
        p1_str = ", ".join(f"{equilibrium[0].get(k, 0.0):.1f}" for k in self.original_row_labels)
        p2_str = ", ".join(f"{equilibrium[1].get(k, 0.0):.1f}" for k in self.original_col_labels)
    
        print(f"\nMix Strategies: P1 ({p1_str}), P2 ({p2_str})")


