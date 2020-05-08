import core.ui

if __name__ == "__main__":
    core.ui.banner()
    while True:
        try:
            switch = core.ui.menu()
            if 0:
                pass
            else:
                print('\nPlease type a valid number.\n'), input()
        except:
            print('\nPlease, check your selection.\n')