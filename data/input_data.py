"""
Project: Inventory and Production Optimization Case Study
File: input_data.py
Purpose: Centralized definition of model parameters and input data
         Store all input data and model parameters
Author: Abdoulaye Diop

Confidentiality and Anonymization Note:
The company name, product names, and numerical values in this file
have been modified and anonymized for demonstration purposes only.
This project does not use real or proprietary business data.
"""

# -----------------------------
# SETS
# -----------------------------

months = range(1, 13)
products = ["Smartphone", "Laptop", "Tablet"]

# -----------------------------
# COST DATA
# -----------------------------

production_cost = {
    "Smartphone": {1: 150, 2: 160, 3: 170, 4: 180, 5: 190, 6: 200, 7: 210, 8: 220, 9: 230, 10: 240, 11: 250, 12: 260},
    "Laptop": {1: 500, 2: 520, 3: 530, 4: 540, 5: 550, 6: 560, 7: 570, 8: 580, 9: 590, 10: 600, 11: 610, 12: 620},
    "Tablet": {1: 300, 2: 310, 3: 320, 4: 330, 5: 340, 6: 350, 7: 360, 8: 370, 9: 380, 10: 390, 11: 400, 12: 410}
}

# -----------------------------
# DEMAND DATA
# -----------------------------

demand = {
    "Smartphone": {1: 1000, 2: 1100, 3: 1200, 4: 1300, 5: 1400, 6: 1500, 7: 1600, 8: 1700, 9: 1800, 10: 1900, 11: 2000, 12: 2100},
    "Laptop": {1: 500, 2: 550, 3: 600, 4: 650, 5: 700, 6: 750, 7: 800, 8: 850, 9: 900, 10: 950, 11: 1000, 12: 1050},
    "Tablet": {1: 800, 2: 850, 3: 900, 4: 950, 5: 1000, 6: 1050, 7: 1100, 8: 1150, 9: 1200, 10: 1250, 11: 1300, 12: 1350}
}

# -----------------------------
# SYSTEM CONSTRAINTS
# -----------------------------

total_capacity = 10000
max_inventory = 15000
min_inventory = 1000
holding_cost_rate = 0.02

# -----------------------------
# INITIAL CONDITIONS
# -----------------------------

initial_inventory = {p: 0 for p in products}
initial_backorder = {p: 0 for p in products}
