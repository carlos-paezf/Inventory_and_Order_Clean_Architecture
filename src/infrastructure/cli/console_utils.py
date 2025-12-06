import sys
from typing import Sequence


GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"


def pause() -> None:
    input(f"{MAGENTA}\nPresiona Enter para volver al menú...{RESET}")
    print("\n", "-" * 100)



def show_menu_options(options: Sequence[str], exit_label: str = "Salir de la demo") -> None:
    for i, opt in enumerate(options, start=1):
        print(f"\t{i}. {opt}")
    print(f"\t0. {exit_label}")


def read_option(n_options: int) -> int:
    while True:
        raw = input(f"{MAGENTA}>>>{RESET} Ingrese el número de la opción a ejecutar: ")

        try:
            option = int(raw)
        except ValueError:
            print(f"{RED}Por favor, solo ingrese solo el numeral de la opción{RESET}")
            continue

        if option == 0:
            print(f"{BLUE}\nSaliendo...{RESET} Gracias por usar la demo.")
            sys.exit(0)

        if 1 <= option <= n_options:
            return option

        print(
            f"{YELLOW}La opción ingresada no es válida.{RESET} "
            f"Ingrese un número entre 0 y {n_options}."
        )
