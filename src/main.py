def pars_input(file_path):
    with open(file_path, 'r') as file :
        return [line.strip() for line in file]

def main():
    print("hello word !")

if __name__ == "__main__":
    main()