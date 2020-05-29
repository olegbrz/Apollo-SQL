queries = [
    # 1
    '''SELECT empleado.nombre, familiar.nombre, relacion, empleado.departamento_nom_dep
    FROM familiar, empleado, departamento 
    WHERE familiar.relacion = 'Hermana' AND empleado.id = familiar.empleado_id AND departamento.numero = 1''',

    '''SELECT empleado.nombre, empleado.apellidos, departamento.nom_dep, familiar.nombre, familiar.telefono
    FROM familiar, empleado, departamento
    WHERE empleado.id = familiar.empleado_id AND empleado.id = '1' AND departamento.numero = 1''',

    '''SELECT becario.nombre, becario.nif, empresa_ext.nombre_emp, universidad.nombre_uni
    FROM becario, universidad, empresa_ext
    WHERE universidad_nombre_emp=nombre_emp AND universidad_nombre_emp=empresa_ext_nombre_emp''',

    '''SELECT empleado.nombre, empleado.apellidos, departamento.nom_dep, familiar.nombre, familiar.telefono
    FROM familiar, empleado, departamento
    WHERE empleado.id = familiar.empleado_id AND empleado.departamento_nom_dep = departamento.nom_dep AND departamento.numero = 1''',

    '''SELECT producto.nom_prod, empleado.nombre, empleado.apellidos
    FROM producto, proyecto, departamento, empleado
    WHERE producto.id_producto = '1' and producto.proyecto_nom_proy = proyecto.nom_proy
    and proyecto.departamento_nom_dep = departamento.nom_dep and empleado.departamento_nom_dep = departamento.nom_dep''' ,
    
    # 2
    '''SELECT count(familiar.relacion), relacion
    FROM familiar
    GROUP BY relacion''',

    '''SELECT count(departamento_nom_dep), departamento_nom_dep
    FROM empleado
    GROUP BY departamento_nom_dep''',

    '''SELECT count(id), ciudad
    FROM empleado
    GROUP BY(ciudad)
    HAVING count(ciudad) > 2''',

    # 3
    '''SELECT empleado_id, empleado_nif
    FROM disenador_ind 
    WHERE empleado_nif IN(SELECT nif FROM empleado WHERE ciudad='Málaga')''',

    '''SELECT nombre, apellidos, nif, departamento_nom_dep
    FROM empleado 
    WHERE nif IN(SELECT empleado_nif FROM departamento)''',

    '''SELECT *
    FROM proyecto
    WHERE nom_proy=ANY(SELECT proyecto_nom_proy FROM producto WHERE coste>2000)''',

    # 4
    '''SELECT empleado.nif, empleado.nombre, empleado.apellidos
    FROM empleado
    WHERE departamento_nom_dep NOT IN ('Diseño')''' ,

    '''SELECT *
    FROM empresa_ext
    WHERE nombre_emp NOT IN (SELECT empresa_ext_nombre_emp FROM universidad)''',

    '''select producto.nom_prod, producto.proyecto_nom_proy
    from producto
    where proyecto_nom_proy not in ('Protesis')''',

    # 5
    ''' SELECT nif, nombre, apellidos, sexo, departamento_nom_dep, salario
    FROM empleado
    WHERE departamento_nom_dep='Investigación' AND salario>ALL(SELECT salario FROM empleado WHERE departamento_nom_dep='Desarrollo')''',

    '''select producto.nom_prod, producto.coste
    from producto
    where producto.proyecto_nom_proy = 'Equipamiento' and coste > all(select producto.coste from producto where producto.proyecto_nom_proy = 'Protesis')''',

    '''SELECT *
    FROM empresa_ext
    WHERE coste/2<ALL(SELECT salario FROM empleado)''',

    # 6
    '''SELECT id_evento, fecha_final - fecha_inicio AS DURACIÓN_DÍAS
    FROM evento 
    ORDER BY DURACIÓN_DÍAS''',

    '''SELECT DEPARTAMENTO_NOM_DEP , AVG(SALARIO) AS MEDIA
    FROM EMPLEADO
    GROUP BY DEPARTAMENTO_NOM_DEP
    ORDER BY MEDIA DESC''',

    '''SELECT  ID, NOMBRE, APELLIDOS, NIF, TRUNC((SYSDATE - fecha_nacimiento)/365) AS EDAD
    FROM EMPLEADO
    ORDER BY EDAD'''
]