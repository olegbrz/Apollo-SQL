import core.ui
import core.config
import core.utils
import cx_Oracle


def connect_to_server():
    connection_settings = core.config.get_config()['connection']

    # Load dsn info from config.ini
    dsn_tns = cx_Oracle.makedsn(
        host=connection_settings['host'],
        port=connection_settings['port'],
        sid=connection_settings['sid'])

    conn = cx_Oracle.connect(
        user=connection_settings['user'],
        password=connection_settings['password'],
        dsn=dsn_tns,
        encoding="UTF-8",
        nencoding="UTF-8")

    # Autocommit after change
    conn.autocommit = True

    print('[i] Connected successfully.')
    input('\nPress ENTER')

    return conn.cursor()


if __name__ == "__main__":
    settings = core.config.get_config()
    connected_to = ''

    core.ui.print_banner()
    while True:
        try:
            switch = core.ui.print_menu(connected_to)
        except:
            print('\n(!) Please, check your selection.')
            input('\nPress ENTER')
            continue

        # [1] Connect/disconnect option
        if switch == 1:
            if not connected_to:
                try:
                    print('\n[*] Connecting...')
                    CURSOR = connect_to_server()
                    host = settings['connection']['host']
                    port = settings['connection']['port']
                    user = settings['connection']['user']
                    connected_to = f'\n [i] Connected to {host}:{port} as {user}'
                except:
                    print('\n[!] Connection failed, please check settings.')
                    input('\nPress ENTER')
            else:
                try:
                    CURSOR.close()
                    connected_to = ''
                    print('\n[i] Disconnected successfully.')
                    input('\nPress ENTER')
                except:
                    pass

        # [2] Query data function
        elif switch == 2:
            if connected_to == '':
                print('\n[!] Error, no connection was detected.')
                input('\nPress ENTER')
                continue
            core.utils.show_queries(CURSOR)

        # TODO: [3] Alter data function
        elif switch == 3:
            if connected_to == '':
                print('\n[!] Error, no connection was detected.')
                input('\nPress ENTER')
                continue
            core.utils.relate_data(CURSOR)

        # [4] Isert data function
        elif switch == 4:
            if connected_to == '':
                print('\n[!] Error, no connection was detected.')
                input('\nPress ENTER')
                continue
            core.utils.insert(CURSOR)

        # [4] Settings option
        elif switch == 5:
            option = 1
            while option != 0:
                option = core.ui.print_settings()
                if option == 0:
                    pass
                elif option != 0 and option < 6:
                    core.config.modify_config(option)
                    # Refresh settings
                    settings = core.config.get_config()
                else:
                    print(f'\n(!) Error, option {option} doesn\'t exist.')
                    input('\nPress ENTER')

        # [0] Exit execution
        elif switch == 0:
            # Close cursor before exit
            try:
                CURSOR.close()
            except:
                pass
            print('\n[i] Good bye.\n')
            break

        else:
            print(f'\n(!) Error, option {switch} doesn\'t exist.')
            input('\nPress ENTER')
