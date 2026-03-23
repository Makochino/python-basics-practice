try:
    with open("text.txt", "r") as file:
        content = file.read()
        print("File content:")
        print(content)

#to check main error
except FileNotFoundError:
    print("File doesn't exist")

#to check any other error which can be
except Exception as e:
    print(f"Another error: {e}")


