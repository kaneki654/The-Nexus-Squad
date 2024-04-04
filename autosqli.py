import pyfiglet
from autosqli import log 
from autosqli.parse_args import argument_parse  
from autosqli import save
from autosqli import stages


class colors:
    clear = "\033[1;37m"

a = 'CREATED BY TNS'

print(colors.clear + a)

ascii_banner = pyfiglet.figlet_format("TNS AUTO SQLI")
print(ascii_banner)

def main():
    args = argument_parse()

    if args.debug:
        log.debug("Ok boss, launching in debug mode")
        import pudb
        pudb.set_trace()  # XXX BREAKPOINT

    log.info("Welcome into AutoSQLi!")
    log.info("CREATED BY TNS")
    log.debug("Checking for saves...")
    save.saveStartup(args)
    log.debug("Loading save...")
    save.importSave()

    log.debug("current_save.stage in main(): " + str(save.getStage()))

    while True:
        log.debug("Getting into the next stage")
        need_to_continue = stages.nextStage(args)
        save.writeSave() 
        log.debug("Save exported")
        if save.getStage() == stages.REPORT_STAGE or need_to_continue is False:
            break

    log.info("Goodbye!")


if __name__ == "__main__":
    main()
