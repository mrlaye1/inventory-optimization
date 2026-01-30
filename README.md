# Inventory and Production Optimization Case Study

## Applied Operations Research and Decision Optimization using Python and Pyomo
### Date: May 12th, 2024

---

## Overview

This project presents a multi product, multi period inventory and production optimization model.  
The objective is to determine optimal monthly production, inventory holding, and backorder decisions that minimize total operational cost while satisfying demand and capacity constraints.

The project is designed as a clean, modular, and reproducible analytics case study suitable for academic evaluation, professional portfolios, and technical interviews.

---

## Business Problem

A manufacturing company produces multiple products over a planning horizon of twelve months.

The company faces the following challenges.

> 1. Demand varies by product and month  
> 2. Production capacity is limited each month  
> 3. Inventory storage has upper and lower bounds  
> 4. Holding inventory creates cost  
> 5. Failing to meet demand creates backorders  

The company must decide how much to produce and store each month in order to minimize total cost while maintaining feasible operations.

---

## Objectives

The optimization model aims to.

> 1. Minimize total production cost  
> 2. Minimize inventory holding cost  
> 3. Minimize backorder related cost  
> 4. Respect monthly production capacity  
> 5. Ensure demand feasibility over time  
> 6. Maintain inventory within allowed bounds  

---

## Data Description

The model uses deterministic input data defined in Python.

### Products

> Smartphone  
> Laptop  
> Tablet  

### Planning Horizon

> Twelve monthly periods

### Key Parameters

> 1. Monthly demand by product  
> 2. Monthly production cost by product  
> 3. Total monthly production capacity  
> 4. Minimum and maximum total inventory  
> 5. Inventory holding cost rate  

All data is stored in a dedicated data module to ensure traceability and transparency.

---

## Methodology

### Optimization Approach

The problem is formulated as a linear programming model using Pyomo.

### Decision Variables

> 1. Production quantity per product and month  
> 2. Inventory level per product and month  
> 3. Backorder quantity per product and month  

### Objective Function

The objective minimizes the sum of.

> 1. Production cost  
> 2. Inventory holding cost  
> 3. Backorder related cost  

### Constraints

> 1. Monthly production capacity constraint  
> 2. Inventory balance across months  
> 3. Maximum inventory constraint  
> 4. Minimum inventory constraint  
> 5. Demand feasibility constraint  

---

## Project Structure

The project follows a professional analytics repository layout.

Project root  
README.md  

data  
input_data.py  

src  
model_definition.py  
solver_run.py  

Each file has a single responsibility.

> 1. input_data.py contains all parameters and assumptions  
> 2. model_definition.py defines the optimization model  
> 3. solver_run.py builds and solves the model  

---

## Execution Instructions

Follow these steps to run the project.

> 1. Open the project folder in PyCharm  
> 2. Create and select a Python virtual environment  
> 3. Install the Pyomo package  
> 4. Install and verify the GLPK solver  
> 5. Mark the data and src folders as Sources Root  
> 6. Open solver_run.py  
> 7. Run the script  

If the setup is correct, the console will display.

> 1. Confirmation that an optimal solution was found  
> 2. The total optimized cost  
> 3. Monthly production, inventory, and backorder values  

---

## Reproducibility

The project is fully reproducible.

> 1. No absolute file paths are used  
> 2. No package installation commands are embedded in scripts  
> 3. All logic is deterministic  
> 4. The solver is external and clearly documented  

---

## Tools and Libraries

> Python  
> Pyomo  
> GLPK  

---

## Key Insights

This model demonstrates how constrained optimization can support operational decision making by.

> 1. Balancing production and inventory tradeoffs  
> 2. Quantifying the cost of unmet demand  
> 3. Managing capacity limitations over time  
> 4. Providing transparent and auditable decisions  

---

## Limitations

> 1. Demand is assumed to be known with certainty  
> 2. Costs are deterministic and linear  
> 3. No service level constraints are enforced  
> 4. No stochastic or scenario based extensions are included  

These limitations are intentional to maintain model clarity.

---

## Author

**ABDOULAYE DIOP**  

Supply Chain Analytics  

Inventory and Production Optimization Case Study
