"""
Project: Inventory and Production Optimization Case Study
File: model_definition.py
Purpose: Define the Pyomo optimization model
Author: Abdoulaye Diop

Confidentiality and Anonymization Note:
All company and product references in this model are fictional.
They are used solely to demonstrate optimization techniques.
"""

import pyomo.environ as pyo


def build_model(data):
    model = pyo.ConcreteModel()

    months = data["months"]
    products = data["products"]

    # -----------------------------
    # DECISION VARIABLES
    # -----------------------------

    model.P = pyo.Var(months, products, within=pyo.NonNegativeReals)
    model.I = pyo.Var(months, products, within=pyo.NonNegativeReals)
    model.B = pyo.Var(months, products, within=pyo.NonNegativeReals)

    # -----------------------------
    # OBJECTIVE FUNCTION
    # -----------------------------

    def objective_rule(m):
        return (
            sum(data["production_cost"][p][t] * m.P[t, p] for t in months for p in products)
            + sum(data["holding_cost_rate"] * data["production_cost"][p][t] * m.I[t, p] for t in months for p in products)
            + sum(data["production_cost"][p][t] * m.B[t, p] for t in months for p in products)
        )

    model.objective = pyo.Objective(rule=objective_rule, sense=pyo.minimize)

    # -----------------------------
    # CONSTRAINTS
    # -----------------------------

    def capacity_rule(m, t):
        return sum(m.P[t, p] for p in products) <= data["total_capacity"]

    model.capacity = pyo.Constraint(months, rule=capacity_rule)

    def inventory_balance_rule(m, t, p):
        if t == 1:
            return (
                m.I[t, p]
                == data["initial_inventory"][p]
                + m.P[t, p]
                - data["demand"][p][t]
                + m.B[t, p]
            )
        return (
            m.I[t, p]
            == m.I[t - 1, p]
            + m.P[t, p]
            - data["demand"][p][t]
            + m.B[t - 1, p]
            - m.B[t, p]
        )

    model.inventory_balance = pyo.Constraint(months, products, rule=inventory_balance_rule)

    def max_inventory_rule(m, t):
        return sum(m.I[t, p] for p in products) <= data["max_inventory"]

    model.max_inventory = pyo.Constraint(months, rule=max_inventory_rule)

    def min_inventory_rule(m, t):
        return sum(m.I[t, p] for p in products) >= data["min_inventory"]

    model.min_inventory = pyo.Constraint(months, rule=min_inventory_rule)

    def demand_feasibility_rule(m, t, p):
        if t == 1:
            return m.P[t, p] + data["initial_inventory"][p] + m.B[t, p] >= data["demand"][p][t]
        return m.P[t, p] + m.I[t - 1, p] + m.B[t, p] >= data["demand"][p][t]

    model.demand_feasibility = pyo.Constraint(months, products, rule=demand_feasibility_rule)

    return model
