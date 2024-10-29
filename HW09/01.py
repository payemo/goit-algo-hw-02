from pulp import LpMaximize, LpProblem, LpVariable

def main():
    model = LpProblem(name='maximize_drink_production', sense=LpMaximize)

    limonad = LpVariable(name='Limonad', lowBound=0, cat='Integer')
    fruit_juice = LpVariable(name='Fruit_Juice', lowBound=0, cat='Integer')

    model += limonad + fruit_juice, "Total_Production"

    # Define resource constraints
    model += 2 * limonad + 1 * fruit_juice <= 100, "Water_Constraint"

    model += 1 * limonad <= 50, "Sugar_Constraint"

    model += 1 * limonad <= 30, "Lemon_Juice_Constraint"

    model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

    model.solve()

    print(f"Optimal production of 'Lemonade': {limonad.varValue} units")
    print(f"Optimal production of 'Fruit juice': {fruit_juice.varValue} units")
    print(f"Maximum total production: {limonad.varValue + fruit_juice.varValue} units")

if __name__ == '__main__':
    main()