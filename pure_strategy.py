def find_pure_strategy_nash_equilibria(payoff_matrix_player1, payoff_matrix_player2):
    nash_equilibria = []
    
    num_strategies_player1 = len(payoff_matrix_player1)
    num_strategies_player2 = len(payoff_matrix_player2[0])
    
    best_responses_player1 = [None] * num_strategies_player2
    for j in range(num_strategies_player2):
        best_responses_player1[j] = max(range(num_strategies_player1), key=lambda i: payoff_matrix_player1[i][j])
    
    best_responses_player2 = [None] * num_strategies_player1
    for i in range(num_strategies_player1):
        best_responses_player2[i] = max(range(num_strategies_player2), key=lambda j: payoff_matrix_player2[i][j])

    for i in range(num_strategies_player1):
        for j in range(num_strategies_player2):
            if best_responses_player1[j] == i and best_responses_player2[i] == j:
                nash_equilibria.append((i, j))
                
    return nash_equilibria