import os

def main():
    print(f"Hello World! runs on actions")

    for i in [1, 2, 3]:
        print(f"XD"* i)
        
    name = os.getenv("USERNAME")
    print(f"Hello {name}")
    
    
    
if __name__ == "__main__":
    main()
    