import core.ui
import core.config
import core.utils
import cx_Oracle

def connect_to_server():

    dsn_tns = cx_Oracle.makedsn(
        host='afrodita.lcc.uma.es',
        port=1521,
        sid='bdsalud')

    conn = cx_Oracle.connect(
        user='Uy4903207n',
        password='y4903207n',
        dsn=dsn_tns,
        encoding="UTF-8",
        nencoding="UTF-8")
    
    conn.autocommit = True
    
    print('\n [i] Connected successfully.\n')
    
    return conn.cursor()

if __name__ == "__main__":
    settings = core.config.get_config()
    connected_to = ''

    core.ui.print_banner()
    while True:
        try: switch = core.ui.print_menu(connected_to)
        except:
            print('\n (!) Please, check your selection.')
            continue

        # [1] Connect/disconnect option
        if switch == 1:
            if not connected_to:
                try:
                    print('\n [*] Connecting...')
                    CURSOR = connect_to_server()
                    host = settings['connection']['host']
                    port = settings['connection']['port']
                    user = settings['connection']['user']
                    connected_to = f'\n [i] Connected to {host}:{port} as {user}'
                except:
                    print('\n [!] Connection failed, please check settings.')
            else:
                try:
                    CURSOR.close()
                    connected_to = ''
                    print('\n [i] Disconnected successfully.')
                except: pass
            
        # T[2] Query data function
        elif switch == 2:
            if connected_to == '':
                print('\n[!] Error, no connection was detected.')
                continue
            core.utils.show_queries(CURSOR)

        # TODO: [3] Alter data function
        elif switch == 3: pass
        
        # [4] Isert data function
        elif switch == 4:
            if connected_to == '':
                print('\n[!] Error, no connection was detected.')
                continue
            core.utils.insert(CURSOR)

        # [4] Settings option
        elif switch == 5:
            option = 1
            while option != 0:
                option = core.ui.print_settings()
                if option != 0:
                    core.config.modify_config(option)
                    # Refresh settings
                    settings = core.config.get_config()

        # [0] Exit execution
        elif switch == 0:
            try: CURSOR.close()
            except: pass
            print('\n Good bye!\n')
            break

        else: print(f'\n (!) Error, option {switch} doesn\'t exist.')