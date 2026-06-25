import os

def main():
    print("Hello World! runs on actions")

    for i in [1, 2, 3, 4, 5]:
        print("XD" * i)

    name = os.getenv('USERNAME')
    print(f"Hola {name}")


if __name__ == "__main__":
    main()