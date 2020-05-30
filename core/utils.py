import core.queries
import core.ui
from datetime import datetime
from extra.tabulate.tabulate import tabulate


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
            input('\nPress ENTER')
            continue

        elif selected == -1:
            return

        elif selected in [-1] + list(range(0, len(tables))):

            print(core.ui.inserting_into(tables[selected]))

            columns_attr = get_columns_attr(CURSOR, tables[selected])

            columns = []
            values = []

            print(
                '\nInsert data per each column (* columns are required, ENTER if null):\n')

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
                        f' ({datatype}){date_format}: {column[0]}{"*" if required else ""}: ').strip()

                    # If item is null and that's ok, pass
                    if user_input == '' and not required:
                        completed = True
                        continue

                    # Prevents set to null no nullable elements
                    elif user_input == '' and required:
                        print(f'\n(!) Error, {column[0]} is required.\n')
                        continue

                    # Checks if item lenght is valid
                    elif len(user_input) > column[2]:
                        print(
                            f'\n(!) Error, {column[0]} maximum lenght is {column[2]}.\n')
                        continue

                    # Checks if item is number
                    elif datatype == 'NUMBER' and not is_number(user_input):
                        print(
                            f'\n(!) Error, {column[0]} has to be a number.\n')
                        continue

                    # Cheks if item is datetime
                    elif datatype == 'DATETIME' and not is_date(user_input):
                        print(f'\n(!) Error, not a valid date.\n')
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
                else:
                    print('\n[i] Insert executed successfully.')

            else:
                print('\n(!) INSERT cancelled.')
                input('Press ENTER')

        else:
            print(f'\n(!) Error, option {selected+1} doesn\'t exist')
            input('\nPress ENTER')


# QUERIES FUNCTION
def show_queries(CURSOR):

    quer = core.queries.predesigned_queries
    desc = core.queries.descriptions

    while 1:
        print(core.ui.query_data_header)
        for i, v in zip(range(1, len(desc)+1), desc):
            print(' [{:>2}] {}'.format(i, v))
        print(core.ui.query_data_footer)

        selected = core.ui.get_user_input() - 1

        if selected == -2:
            input('\nPress ENTER')
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
                    input('\nPress ENTER')
                    continue

                elif selected == -1:
                    break

                elif selected in list(range(0, len(tables))):
                    query = f'SELECT * FROM {tables[selected]}'
                    break

                else:
                    print(f'\n(!) Error, option {selected} doesn\'t exist')
                    input('\nPress ENTER')

        elif selected == 98:
            query = input('\n[?] Type your customized SQL query\n\n > ')

        else:
            print(f'\n(!) Error, option {selected+1} doesn\'t exist')
            input('\nPress ENTER')

        print(core.ui.query_result)

        try:
            show_query(CURSOR, query)
        except:
            print('\n(!) An error has occurred.')
        finally:
            input('\nPress ENTER')
