import time


def main() -> None:
    print("Iniciando robo de teste...")
    for numero in range(1, 11):
        print(f"Contagem: {numero}")
        time.sleep(1)
    print("Robo finalizado.")


if __name__ == "__main__":
    main()
