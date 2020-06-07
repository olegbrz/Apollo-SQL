# Descriptions for queries from queries.sql file
descriptions = [

    # 1

    '''Show employee name, relative info, relation, and department of employee with ID 1''',

    '''Show relative info and department name of employe with ID 18''',

    '''Show scholars and their universities info''',

    '''Show info of employee from department number 1 and his relative''',

    '''Show product with code 1 and employees working on it''',


    # 2

    '''Show maximum wage of employees that's less than the maximum wage of employees from Design department''',

    '''Show ptojects where cost is less than the minimum cost of prosthesis project''',

    '''Show departments that have more employees than Design department''',

    # 3

    '''Show Industrial Designers from Málaga''',

    '''Show department directors''',

    '''Show projects whose cost is more than 2000''',

    # 4

    '''Show all employes that aren't directos of departments''',

    '''Show all external enterprises that aren't universities''',

    '''Show all products that aren't in prosthesis''',

    # 5

    '''Show employees from Invetigation department whose wage is more that any of employees from Dev department''',

    '''Show products from equipment that cost more than any of prosthetics products''',

    '''Show external enterprises which half of the cost is less than the salary of any of the employees''',

    # 6

    '''Show the events ordered by their duration''',

    '''Show average wage by departament in descending order''',

    '''Show employees ordered by their age''',

]

# Relation: [destination, origin(s), type]
# Types of relationships:
# 1 -> 1:1, 2 -> 1:N, 3 -> N:M
relations = [
    ['EMPLEADO', 'DEPARTAMENTO', 2],
    ['DEPARTAMENTO', 'EMPLEADO', 2],
    ['PRODUCTO', 'PROYECTO', 2],
    ['PROYECTO', 'DEPARTAMENTO', 2],
    ['EVENTO', 'EMPRESA_EXT', 2],
    ['UNIVERSIDAD', 'EMPRESA_EXT', 2],
    ['BECARIO', 'UNIVERSIDAD', 2],
    ['AFILIADO_A', ['DEPARTAMENTO', 'EMPRESA_EXT'], 3],
    ['PROVEE_A', ['PROYECTO', 'EMPRESA_EXT'], 3],
]