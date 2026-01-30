"""
Project: Inventory and Production Optimization Case Study
File: solver_run.py
Purpose: Solve the optimization model
Author: Abdou

Note:
This script assumes an open source solver such as GLPK
is available in the system environment.
"""

import pyomo.environ as pyo
from data import input_data
from src.model_definition import build_model

# -----------------------------
# LOAD DATA
# -----------------------------

data = {
    "months": input_data.months,
    "products": input_data.products,
    "production_cost": input_data.production_cost,
    "demand": input_data.demand,
    "total_capacity": input_data.total_capacity,
    "max_inventory": input_data.max_inventory,
    "min_inventory": input_data.min_inventory,
    "holding_cost_rate": input_data.holding_cost_rate,
    "initial_inventory": input_data.initial_inventory,
    "initial_backorder": input_data.initial_backorder
}

# -----------------------------
# BUILD AND SOLVE MODEL
# -----------------------------

model = build_model(data)
solver = pyo.SolverFactory("glpk")
results = solver.solve(model)

# -----------------------------
# OUTPUT RESULTS
# -----------------------------

if results.solver.termination_condition == pyo.TerminationCondition.optimal:
    print("Optimal solution found\n")
    print(f"Total cost: ${pyo.value(model.objective):,.2f}\n")

    for t in data["months"]:
        print(f"Month {t}")
        for p in data["products"]:
            print(
                f"{p} | "
                f"Production: {pyo.value(model.P[t, p]):.0f}, "
                f"Inventory: {pyo.value(model.I[t, p]):.0f}, "
                f"Backorders: {pyo.value(model.B[t, p]):.0f}"
            )
        print()
else:
    print("No optimal solution found or model infeasible")
