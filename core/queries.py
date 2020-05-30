predesigned_queries = [

    # 1
    
    '''SELECT empleado.nombre, familiar.nombre, relacion, empleado.departamento_nom_dep
    FROM familiar, empleado, departamento 
    WHERE familiar.relacion = 'Hermana' AND empleado.id = familiar.empleado_id AND departamento.numero = 1''',

    '''SELECT empleado.nombre, empleado.apellidos, departamento.nom_dep, familiar.nombre, familiar.telefono
    FROM empleado LEFT JOIN familiar ON empleado.id = familiar.empleado_id LEFT JOIN departamento ON empleado.departamento_nom_dep = departamento.nom_dep
    WHERE empleado.id = 18''',

    '''SELECT becario.nombre, becario.nif, empresa_ext.nombre_emp, universidad.nombre_uni
    FROM becario, universidad, empresa_ext
    WHERE universidad_nombre_emp = nombre_emp AND universidad_nombre_emp = empresa_ext_nombre_emp''',

    '''SELECT empleado.nombre, empleado.apellidos, departamento.nom_dep, familiar.nombre, familiar.telefono
    FROM familiar, empleado, departamento
    WHERE empleado.id = familiar.empleado_id AND empleado.departamento_nom_dep = departamento.nom_dep AND departamento.numero = 1''',

    '''SELECT producto.nom_prod, empleado.nombre, empleado.apellidos
    FROM producto, proyecto, departamento, empleado
    WHERE producto.id_producto = '1' and producto.proyecto_nom_proy = proyecto.nom_proy
    and proyecto.departamento_nom_dep = departamento.nom_dep and empleado.departamento_nom_dep = departamento.nom_dep''' ,
    
    # 2
    
    '''SELECT departamento_nom_dep, MAX(salario) AS SALARIO_MAXIMO
    FROM empleado
    GROUP BY departamento_nom_dep
    HAVING MAX(salario) <= (SELECT MAX (salario)
                            FROM empleado
                            WHERE departamento_nom_dep = 'Diseño');''',

    '''SELECT proyecto_nom_proy, MIN(coste) AS COSTE_MINIMO
    FROM producto
    GROUP BY proyecto_nom_proy
    HAVING MIN(coste) < (SELECT MIN (coste)
                         FROM producto
                         WHERE proyecto_nom_proy = 'Protesis');''',

    '''SELECT departamento_nom_dep, COUNT(departamento_nom_dep)
    FROM empleado
    GROUP BY departamento_nom_dep
    HAVING COUNT(departamento_nom_dep) > (SELECT COUNT(departamento_nom_dep)
                                          FROM empleado
                                          WHERE departamento_nom_dep = 'Diseño');''',
    
    # 3
    
    '''SELECT empleado_id, empleado_nif
    FROM disenador_ind 
    WHERE empleado_nif IN(SELECT nif FROM empleado WHERE ciudad = 'Málaga')''',

    '''SELECT nombre, apellidos, nif, departamento_nom_dep
    FROM empleado 
    WHERE nif IN(SELECT empleado_nif FROM departamento)''',

    '''SELECT *
    FROM proyecto
    WHERE nom_proy = ANY(SELECT proyecto_nom_proy FROM producto WHERE coste>2000)''',

    # 4
    
    '''SELECT empleado.id, empleado.nif, empleado.departamento_nom_dep
    FROM empleado
    WHERE NOT EXISTS (SELECT 1
                      FROM departamento
                      WHERE departamento.empleado_nif = empleado.nif)''' ,
    
    '''SELECT *
    FROM empresa_ext
    WHERE NOT EXISTS (SELECT 1
                      FROM universidad
                      WHERE universidad.empresa_ext_nombre_emp = empresa_ext.nombre_emp)''',

    '''SELECT *
    FROM proyecto
    WHERE NOT EXISTS (SELECT 1 FROM producto
                      WHERE producto.proyecto_nom_proy = proyecto.nom_proy)''',

    # 5
    
    ''' SELECT nif, nombre, apellidos, sexo, departamento_nom_dep, salario
    FROM empleado
    WHERE departamento_nom_dep = 'Investigación' AND salario>ALL(SELECT salario
                                                               FROM empleado
                                                               WHERE departamento_nom_dep = 'Desarrollo')''',

    '''SELECT producto.nom_prod, producto.coste
    FROM producto
    WHERE producto.proyecto_nom_proy = 'Equipamiento' and coste > ALL(SELECT producto.coste
                                                                      FROM producto
                                                                      WHERE producto.proyecto_nom_proy = 'Protesis')''',

    '''SELECT *
    FROM empresa_ext
    WHERE coste/2<ALL(SELECT salario
                      FROM empleado)''',

    # 6
    '''SELECT id_evento, fecha_final - fecha_inicio AS DURACIÓN_DÍAS
    FROM evento 
    ORDER BY DURACIÓN_DÍAS''',

    '''SELECT DEPARTAMENTO_NOM_DEP, AVG(SALARIO) AS MEDIA
    FROM EMPLEADO
    GROUP BY DEPARTAMENTO_NOM_DEP
    ORDER BY MEDIA DESC''',

    '''SELECT  ID, NOMBRE, APELLIDOS, NIF, TRUNC((SYSDATE - fecha_nacimiento)/365) AS EDAD
    FROM EMPLEADO
    ORDER BY EDAD'''
]

descriptions = [

    # 1

    '''Show employee name and his relative info, relation, and department''',

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

    '''Show all employes that aren't from Design department''',
    
    '''Show all external enterprises that aren't universities''',

    '''Show all products that aren't in prosthesis''',

    # 5

    '''Show employees that aren't directors of departments''',
    
    '''Show external enterprises that aren't universities''',

    '''Show projects that haven't any products''',

    # 6

    '''Show the events ordered by their duration''',

    '''Show average wage by departament in descending order''',

    '''Show employees ordered by their age''',

]