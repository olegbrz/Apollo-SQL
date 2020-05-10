import core.config

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
 [3] ALTER DATA
 [4] SETTINGS

 [0] EXIT

=============================================================={conn}
'''
    return menu

bar = '''
==============================================================
'''

settings = '''
==============================================================
   SETTINGS
==============================================================
'''

def print_banner(): print(banner)

def print_menu(connected_to):
    print(menu(connected_to))
    try: mode = int(input('> '))
    except: pass

    return mode

def print_settings():
    print(settings)
    config = core.config.get_config()['connection']

    for i, k, v in zip(range(1, len(config) + 1), config.keys(), config.values()):
        if k == 'password': v = '*' * len(v)
        print(f' [{i}] {k}:\t{v}')
    print(f'\n [0] BACK\n{bar}')
     
    try: mode = int(input('> '))
    except: pass

    return mode

