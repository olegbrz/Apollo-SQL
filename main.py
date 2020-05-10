import core.ui
import core.config
import cx_Oracle


def connect_to_server():
    connection_settings = core.config.get_config()['connection']

    dsn_tns = cx_Oracle.makedsn(
        host=connection_settings['host'],
        port=connection_settings['port'],
        sid=connection_settings['sid'])

    conn = cx_Oracle.connect(
        user=connection_settings['user'],
        password=connection_settings['password'],
        dsn=dsn_tns)

    print('\n [i] Connected successfully.\n')
    return conn.cursor()


if __name__ == "__main__":
    settings = core.config.get_config()
    connected_to = ''

    core.ui.print_banner()
    while True:
        try: switch = core.ui.print_menu(connected_to)
        except:
            print('\n (!) Please, check your selection.\n')
            continue

        # [1] Connect/disconnect option
        if switch == 1:
            if not connected_to:
                try:
                    print('\n [*] Connecting...')
                    cursor = connect_to_server()
                    host = settings['connection']['host']
                    port = settings['connection']['port']
                    user = settings['connection']['user']
                    connected_to = f'\n [i] Connected to {host}:{port} as {user}'
                except:
                    print('\n [!] An error has ocurred, please check connection settings.')
            else:
                try:
                    cursor.close()
                    connected_to = ''
                    print('\n [i] Disconnected successfully.')
                except:
                    pass
            
        # TODO: Query data function
        elif switch == 2: pass
        # TODO: Alter data function
        elif switch == 3: pass

        # [4] Settings option
        elif switch == 4:
            option = 1
            while option != 0:
                option = core.ui.print_settings()
                if option != 0:
                    core.config.modify_config(option)
                    # Refresh settings
                    settings = core.config.get_config()

        # [0] Exit execution
        elif switch == 0:
            try: cursor.close()
            except:
                print('\n Good bye!\n')
                break

        else: print('\n (!) Please type a valid number.')