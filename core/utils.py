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
    r = CURSOR.execute(query)
    return r.description

# Get columns names in a list
def get_column_names(CURSOR, tablename):
    r = get_columns_attr(CURSOR, tablename)
    return [i[0] for i in r]

# Prints query result with tabulate
def show_query(CURSOR, query):
    r = CURSOR.execute(query)
    data = list(r)
    headers = [i[0] for i in r.description]
    print(tabulate(data, headers=headers, tablefmt='github'))
    return data

# show_query() variant to query whole table
def show_table(CURSOR, tablename):
    query = f'SELECT * FROM {tablename}'
    show_query(CURSOR, query)

# Insert function with CLI prompt included
def insert(CURSOR):
    
    def is_date(string):
        isdate = True
        day, month, year = string.split('/')
        try: datetime(year=int(year), month=int(month), day=int(day))
        except: isdate = False
        return isdate
    
    def is_number(string):
        number = True
        try: float(string)
        except: number = False
        return number
    
    tables = get_tables(CURSOR)
    
    print('\n [i] Please, select table:\n')
    for k, v in zip(range(1, len(tables)+1), tables):
        print(f' [{k}]\t{v}')

    try: selected = int(input('> ')) - 1
    except: pass
    
    print(f'\nINSERTING INTO: {tables[selected]}')
    
    columns_attr = get_columns_attr(CURSOR, tables[selected])
    
    columns = []
    values = []
    
    print('\nInsert data per each column (* columns are required, ENTER if null):\n')
    
    for column in columns_attr:
        completed = False
        
        required = bool(not column[6])
        datatype = column[1].__name__
        
        if datatype == 'DATETIME': date_format = " (Format dd/mm/yyyy) "
        else: date_format = ""
            
        while not completed:
            # Asks user for data
            user_input = input(f' ({datatype}){date_format}: {column[0]}{"*" if required else ""}: ').strip()
            
            # If item is null and that's ok, pass
            if user_input == '' and not required:
                completed = True
                continue
                
            # Prevents set to null no nullable elements
            elif user_input == '' and required:
                print(f'[!] Error, {column[0]} is required.')
                continue
            
            # Checks if item lenght is valid
            elif len(user_input) > column[2]:
                print(f'[!] Error, {column[0]} maximum lenght is {column[2]}')
                continue
            
            # Checks if item is number
            elif datatype == 'NUMBER' and not is_number(user_input):
                print(f'[!] Error, {column[0]} has to be a number')
                continue
            
            # Cheks if item is datetime
            elif datatype == 'DATETIME' and not is_date(user_input):
                print(f'[!] Error, not a valid date')
                continue
                        
            # If all ok...
            else:
                # If it's a string, add ''
                if datatype == 'STRING' or datatype == 'FIXED_CHAR':
                    user_input = "'" + user_input + "'"
                # If it's a date, add TO_DATE clause
                elif datatype == 'DATETIME':
                    user_input = f"TO_DATE('{user_input}', 'dd/mm/yyyy')"
                
                # Add result 
                columns.append(column[0])
                values.append(user_input)
                completed = True
    
    values = ", ".join(values)
    columns = ", ".join(columns)
    
    # Prepare insert statement with customized data
    insert_statement = f'''INSERT INTO {tables[selected]} ({columns}) VALUES ({values})'''
    
    user_switch = input(f'\nInsert data to {tables[selected]}? (y/n)\n > ')

    if user_switch in ['y', 'Y']:
        # Execute insert to database
        try: CURSOR.execute(insert_statement)
        except:
            print('\n[!] Something went wrong, insert failed. Please, check item data types.')
        else:
            print('\n[i] Insert executed successfully.')
            
    elif user_switch in ['n', 'N']:
        print('\n[i] Okay, INSERT cancelled.\n')