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
    
    def print_prue_strategies(self):
        equilibria = self.find_pure_strategy_nash_equilibria()
        if not equilibria:
            print("No pure strategy Nash equilibria found.")
        else:
            for eq in equilibria:
                print(f"Pure strategy Nash equilibrium: Player 1 plays {eq[0]}, Player 2 plays {eq[1]}")

