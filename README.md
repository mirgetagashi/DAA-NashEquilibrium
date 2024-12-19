# Nash Equilibrium

This project implements an algorithm to find Nash Equilibria in both pure and mixed strategies for two-player games. It is designed for educational purposes, showcasing game theory concepts and Python programming.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

---

## Overview
A **Nash Equilibrium** is a set of strategies where no player can benefit by changing their strategy while the other players keep their strategies unchanged. This project computes Nash Equilibria for two-player normal-form games, supporting:
- **Pure strategies**: Deterministic choices by players.
- **Mixed strategies**: Probabilistic combinations of strategies.


---

## Features
- Compute Nash Equilibria for both pure and mixed strategies.
- Handle games represented in matrix form.
- Support symmetric and asymmetric games.
- Use linear programming to find Nash Equilibrium.
- Customizable for various game sizes.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mirgetagashi/DAA-NashEquilibrium.git
   ```

2. Install Required Libraries:
   ```bash
   pip install numpy
   ```

---

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. Input the payoff matrices.

3. The output will display:
   - Nash Equilibria in pure strategies (if they exist).
   - Nash Equilibria in mixed strategies.

---
## Example

### Game Description

- **Player 1 Strategies**: U, C, D
- **Player 2 Strategies**: L, M, R

**Payoff Matrices**:

  |       | **L** | **M** |**R**|
  |-------|-------|-------|-------|
  | **U** |   10,3  |   2,4  |   6,5  |
  | **C** |   5,3   |   6,6   |   2,2   |
  | **D** |   7,2   |   5,5   |   3,6   |

 Each cell contains two numbers:
- The first number represents Player 1’s payoff.
- The second number represents Player 2’s payoff.
  
**Expected Output**:
- **Pure Strategies**: (U,R) , (C,M)
- **Mix Strategies**: P1 (0.8, 0.2, 0), P2 (0, 0.5, 0.5)

---





