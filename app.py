#!/usr/bin/env python3
import sys
 
 
def app() -> None:
    try:
        from colorama import init, Fore, Style
         
        from tk import run
        init(autoreset=True)
        run()

    except ImportError as err:
        print(f"[ERROR] Missing dependency: {err}", file=sys.stderr)
        sys.exit(84)
    except Exception as err:
        print(f"[ERROR] Unexpected error: {err}", file=sys.stderr)
        sys.exit(84)
    sys.exit(0)
 
 
if __name__ == "__main__":
    app()
