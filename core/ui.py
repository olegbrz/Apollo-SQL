import core.config

# CLI ELEMENTS

banner = r'''==============================================================
        ___                ____         _____ ____    __ 
       /   |  ____  ____  / / /___     / ___// __ \  / /
      / /| | / __ \/ __ \/ / / __ \    \__ \/ / / / / /  
     / ___ |/ /_/ / /_/ / / / /_/ /   ___/ / /_/ / / /___
    /_/  |_/ .___/\____/_/_/\____/   /____/\___\_\/_____/
          /_/                                       v.1.0
     - A lightweight Oracle SQL database Python client -

     (c) Lucía Arrabalí, Oleg Brezitskyy, Ainoa Fernández
                Sergio Martín, Viktor Yosava'''


def menu(conn=''):
    menu = f'''
==============================================================
   MENU
==============================================================

 [1] {'DIS' if conn else ''}CONNECT
 [2] QUERY DATA
 [3] RELATE DATA
 [4] INSERT DATA
 [5] SETTINGS

 [0] EXIT

=============================================================={conn}
'''
    return menu


bar = '''
=============================================================='''

settings = '''
==============================================================
   SETTINGS
==============================================================
'''

query_data_header = '''
==============================================================
   QUERY DATA
==============================================================
'''

query_data_footer = '''
 [98] Query whole table
 [99] Customized query (SQL)

 [ 0] BACK

=============================================================='''

insert_data_header = '''
==============================================================
   INSERT DATA
==============================================================
'''

insert_data_footer = '''\n [ 0] BACK

=============================================================='''


def inserting_into(tablename):
    return f'''
==============================================================
   INSERTING INTO {tablename}
=============================================================='''


query_result = '''
==============================================================
   QUERY RESULT
==============================================================
'''

relating_data = '''
==============================================================
   RELATE DATA          |  --- 1:1  |  <-- 1:N  |  <-> N:M  |
==============================================================
'''

# FUNCTIONS


def print_banner(): print(banner)


def print_menu(connected_to):
    print(menu(connected_to))
    try:
        mode = int(input('> '))
    except:
        pass

    return mode


def print_settings():
    print(settings)
    config = core.config.get_config()['connection']

    while 1:

        for i, k, v in zip(range(1, len(config) + 1), config.keys(), config.values()):
            if k == 'password':
                v = '*' * len(v)
            print(f' [{i}] {k}:\t{v}')
        print(f'\n [0] BACK\n{bar}')

        mode = get_user_input()

        if mode == -1:
            input('\nPress ENTER to continue.')
        else:
            return mode


def get_user_input(valid_options=[]):
    selected = input('\n > ')
    result = -1

    if not selected.isnumeric():
        print('\n(!) Error. Please, enter a number.')
        input('\nPress ENTER to continue.')
    elif valid_options and int(selected) not in valid_options:
        print(f'\n(!) Error. Option {selected} doesn\'t exist.')
        input('\nPress ENTER to continue.')
    else:
        selected = int(selected)
        result = selected

    return result