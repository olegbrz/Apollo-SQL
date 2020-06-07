import core.ui
from custom import db_data
from datetime import datetime
from extra.tabulate.tabulate import tabulate


# Get customized queries from queries.sql and queries.py files
def get_queries():
    f = open('custom/queries.sql', encoding='utf-8')
    full_sql = f.read()
    sql_commands = full_sql.split(';')

    queries = [sql_command for sql_command in sql_commands]
    return queries


# Get all user tables in a list
def get_tables(CURSOR):
    query = '''
    SELECT table_name
    FROM user_tables
    ORDER BY table_name'''
    response = CURSOR.execute(query)
    return [i[0] for i in response]


# Get columns attributes in a list
# (name, type, display_size, internal_size, precision, scale, null_ok)
def get_columns_attr(CURSOR, tablename):
    query = f'''
    SELECT * from {tablename}'''
    response = CURSOR.execute(query)
    return response.description


# Get columns names in a list
def get_column_names(CURSOR, tablename):
    response = get_columns_attr(CURSOR, tablename)
    return [i[0] for i in response]


# Prints query result with tabulate
def show_query(CURSOR, query):
    response = CURSOR.execute(query)
    data = list(response)
    headers = [i[0] for i in response.description]
    print(tabulate(data, headers=headers, tablefmt='fancy_grid'))

    return data


# INSERT FUNCTION
def insert(CURSOR):

    def is_date(string):
        isdate = True
        day, month, year = string.split('/')
        try:
            datetime(year=int(year), month=int(month), day=int(day))
        except:
            isdate = False
        return isdate

    def is_number(string):
        number = True
        try:
            float(string)
        except:
            number = False
        return number

    tables = get_tables(CURSOR)

    while 1:

        print(core.ui.insert_data_header)

        for k, v in zip(range(1, len(tables)+1), tables):
            print(' [{:>2}] {}'.format(k, v))

        print(core.ui.insert_data_footer)

        selected = core.ui.get_user_input() - 1

        if selected == -2:
            continue

        elif selected == -1:
            return

        elif selected in [-1] + list(range(0, len(tables))):

            print(core.ui.inserting_into(tables[selected]))

            columns_attr = get_columns_attr(CURSOR, tables[selected])

            columns = []
            values = []

            print(
                '\n[i] Insert data per each column (* columns are required, ENTER if null):\n')

            # Get user data and check data type per each column
            for column in columns_attr:

                completed = False
                required = bool(not column[6])
                datatype = column[1].__name__

                if datatype == 'DATETIME':
                    date_format = " (Format dd/mm/yyyy) "
                else:
                    date_format = ""

                while not completed:
                    # Asks user for data
                    user_input = input(
                        f' [?] ({datatype}){date_format}: {column[0]}{"*" if required else ""}: ').strip()

                    # If item is null and that's ok, pass
                    if user_input == '' and not required:
                        completed = True
                        continue

                    # Prevents set to null no nullable elements
                    elif user_input == '' and required:
                        print(f'\n(!) Error, {column[0]} is required.')
                        input('\nPress ENTER to continue.')
                        continue

                    # Checks if item lenght is valid
                    elif len(user_input) > column[2]:
                        print(
                            f'\n(!) Error, {column[0]} maximum lenght is {column[2]}.')
                        input('\nPress ENTER to continue.')
                        continue

                    # Checks if item is number
                    elif datatype == 'NUMBER' and not is_number(user_input):
                        print(
                            f'\n(!) Error, {column[0]} has to be a number.')
                        input('\nPress ENTER to continue.')
                        continue

                    # Cheks if item is datetime
                    elif datatype == 'DATETIME' and not is_date(user_input):
                        print(f'\n(!) Error, not a valid date.')
                        input('\nPress ENTER to continue.')
                        continue

                    # If all ok...
                    else:
                        # If it's a string, add ''
                        if datatype in ['STRING', 'FIXED_CHAR']:
                            user_input = "'" + user_input + "'"

                        # If it's a date, add TO_DATE clause
                        elif datatype == 'DATETIME':
                            user_input = f"TO_DATE('{user_input}', 'dd/mm/yyyy')"

                        # Add result
                        columns.append(column[0])
                        values.append(user_input)
                        completed = True

            # Generate columns and values string for INSERT statement
            values = ", ".join(values)
            columns = ", ".join(columns)

            # Prepare insert statement with customized data
            insert_statement = f'''INSERT INTO {tables[selected]} ({columns}) VALUES ({values})'''

            # Check if user is sure about the insert
            user_switch = input(
                f'\n[?] Insert data to {tables[selected]}? (y/n)\n\n > ')

            if user_switch in ['y', 'Y']:
                # Execute insert to database
                try:
                    CURSOR.execute(insert_statement)
                except:
                    print(
                        '\n[!] Something went wrong, insert failed. Please, check item data types.')
                    input('\nPress ENTER to continue.')
                else:
                    print('\n[i] Insert executed successfully.')
                    input('\nPress ENTER to continue.')

            else:
                print('\n(!) INSERT cancelled.')
                input('\nPress ENTER to continue.')

        else:
            print(f'\n(!) Error, option {selected+1} doesn\'t exist')
            input('\nPress ENTER to continue.')


# QUERIES FUNCTION
def show_queries(CURSOR):

    quer = get_queries()
    desc = db_data.descriptions

    while 1:
        selection_ok = True
        print(core.ui.query_data_header)
        for i, v in zip(range(1, len(desc)+1), desc):
            print(' [{:>2}] {}'.format(i, v))
        print(core.ui.query_data_footer)

        selected = core.ui.get_user_input() - 1

        if selected == -2:
            continue

        elif selected == -1:
            break

        elif selected in list(range(0, len(desc))):
            query = quer[selected]

        elif selected == 97:

            tables = get_tables(CURSOR)

            while 1:
                for i, table_name in zip(range(1, len(tables)+1), tables):
                    print(' [{:>2}] {}'.format(i, table_name))
                print('\n [ 0] BACK')

                selected = core.ui.get_user_input() - 1

                if selected == -2:
                    continue

                elif selected == -1:
                    break

                elif selected in list(range(0, len(tables))):
                    query = f'SELECT * FROM {tables[selected]}'
                    break

                else:
                    print(f'\n(!) Error, option {selected} doesn\'t exist')
                    input('\nPress ENTER to continue.')

            if selected == -1:
                continue

        elif selected == 98:
            query = input('\n[?] Type your customized SQL query\n\n > ')

        else:
            selection_ok = False
            print(f'\n(!) Error, option {selected+1} doesn\'t exist')
            input('\nPress ENTER to continue.')

        print(core.ui.query_result)

        if selection_ok:
            try:
                show_query(CURSOR, query)
            except:
                print('\n(!) An error has occurred.')
            finally:
                input('\nPress ENTER to continue.')


# Relate data
def relate_data(CURSOR):

    # Types of constraints: P - primary, R - referential or foreign
    def get_constraints(CURSOR, tablename, type='P'):
        query = f'''
        SELECT column_name
        FROM all_cons_columns
        WHERE constraint_name = (
            SELECT constraint_name
            FROM user_constraints 
            WHERE UPPER(table_name) = UPPER('{tablename}') AND CONSTRAINT_TYPE = '{type}')'''

        response = CURSOR.execute(query)
        return [i[0] for i in response]

    def get_key_column(CURSOR, tablename):
        constraints = get_constraints(CURSOR, tablename)
        if len(constraints) != 1:
            constraints = ', '.join(constraints)
        else:
            constraints = constraints[0]
        query = f'''
        SELECT {constraints}
        FROM {tablename}'''
        response = CURSOR.execute(query)

        res = [i for i in response]

        if len(res[0]) == 1:
            res = [[i[0]] for i in res]

        return res

    while 1:

        print(core.ui.relating_data)

        for i, v in zip(range(1, len(db_data.relations) + 1), db_data.relations):
            '''
            From custom.db_data.py
            Relation: [destination, origin(s), type]
            Types of relationships:
            1 -> 1:1, 2 -> 1:N, 3 -> N:M
            '''
            if v[-1] == 1:
                print(' [{:>2}] {} --- {}'.format(i, v[0], v[1]))
            elif v[-1] == 2:
                print(' [{:>2}] {} <-- {}'.format(i, v[0], v[1]))
            elif v[-1] == 3:
                print(' [{:>2}] {}: {} <-> {}'.format(i, v[0], v[1][0], v[1][1]))
        print('\n [ 0] BACK')
        print(core.ui.bar)

        n = core.ui.get_user_input(range(0, len(db_data.relations)+1)) - 1

        if n == -1:
            break
        elif n == -2:
            continue

        relation = db_data.relations[n]

        # TODO: 1:1 relation (P-keys interchange)
        if relation[-1] == 1:
            pass

        # Type 2: 1:N (destination table gets
        # P-key from origin as F-key)
        elif relation[-1] == 2:
            entities1 = get_key_column(CURSOR, relation[0])
            entities2 = get_key_column(CURSOR, relation[1])

            # convert entities lists in print-ready versions without brackets
            entities1_disp = [', '.join([str(e) for e in e1])
                              for e1 in entities1]
            entities2_disp = [', '.join([str(e) for e in e2])
                              for e2 in entities2]

            print(f'\nSelect entity from {relation[0]}:\n')

            for i, v in zip(range(1, len(entities1)+1), entities1_disp):
                print(f' [{i}] {v}')

            n1 = core.ui.get_user_input(range(0, len(entities1) + 1)) - 1

            if n1 == -2:
                continue

            print(
                f'\nSelect entity from {relation[1]} to link to {relation[0]}:\n')

            for i, v in zip(range(1, len(entities2)+1), entities2_disp):
                print(f' [{i}] {v}')

            n2 = core.ui.get_user_input(range(0, len(entities2) + 1)) - 1

            if n2 == -2:
                continue

            entity1 = entities1[n1]
            entity2 = entities2[n2]

            FK = get_constraints(CURSOR, relation[0], 'R')

            # creating update statement payload:
            # column1 = value2, column2 = value2, ...
            payload = []
            for column, value in zip(FK, entity2):
                if type(value) == str:
                    value = f"'{value}'"
                payload.append(f'{column} = {value}')
            payload = ', '.join(payload)

            # we need only one key to identify the identity
            PK = get_constraints(CURSOR, relation[0])[0]
            PK_value = entity1[0]

            # string correction ''
            if type(PK_value) == str:
                PK_value = f"'{PK_value}'"

            update = f'''
            UPDATE {relation[0]}
            SET {payload}
            WHERE {PK} = {PK_value}
            '''

            print(update)
            op = input(
                f'\n[?] Establish relationship {relation[0]}({entities1_disp[n1]}) <-- {relation[1]}({entities2_disp[n2]})? (y/n) \n\n > ')

            if op in ['y', 'Y', 'yes', 'Yes', 'YES']:
                CURSOR.execute(update)
                print('\n[i] Operation executed successfully.')
                input('\nPress ENTER to continue.')
                break
            else:
                print('\n(!) Operation cancelled')
                input('\nPress ENTER to continue.')

        # Type 3: N:M (destination table gets P-keys
        # from both origin tables as PF-keys)
        elif relation[-1] == 3:

            print('\nSelect table:\n')

            for i, v in zip(range(1, len(relation[1])+1), relation[1]):
                print(f' [{i}] {v}')

            n = core.ui.get_user_input(range(1, len(relation[1]) + 1)) - 1

            if n == -2:
                continue

            table1 = relation[1][n]
            table2 = relation[1][n-1]

            print(f'\nSelect entity from {table1}:\n')

            entities1 = [i[0] for i in get_key_column(CURSOR, table1)]
            entities2 = [i[0] for i in get_key_column(CURSOR, table2)]

            for i, v in zip(range(1, len(entities1)+1), entities1):
                print(f' [{i}] {v}')

            n = core.ui.get_user_input(range(1, len(entities1) + 1)) - 1

            if n == -2:
                continue

            entity1 = entities1[n]

            print(f'\nSelect entity from {table2}:\n')

            for i, v in zip(range(1, len(entities2)+1), entities2):
                print(f' [{i}] {v}')

            n = core.ui.get_user_input(range(1, len(entities2) + 1)) - 1

            if n == -2:
                continue

            entity2 = entities2[n]

            keys = get_constraints(CURSOR, relation[0])

            if table1.upper() in keys[0]:
                values = [entity1] + [entity2]
            else:
                values = [entity2] + [entity1]

            # String '' correction
            for i in range(len(values)):
                values[i] = "'" + values[i] + "'"

            keys = ', '.join(keys)
            values = ', '.join(values)

            insert_statement = f'''
            INSERT INTO {relation[0]} ({keys}) VALUES ({values})
            '''

            op = input(
                f'\n[?] Establish relationship {relation[0]}({table1}:{entity1} <-> {table2}:{entity2})? (y/n) \n\n > ')

            if op in ['y', 'Y', 'yes', 'Yes', 'YES']:
                CURSOR.execute(insert_statement)
                print('\n[i] Operation executed successfully.')
                input('\nPress ENTER to continue.')
                break
            else:
                print('\n(!) Operation cancelled')
                input('\nPress ENTER to continue.')

    print(core.ui.bar)
