def login(username, password):
    try:
        assert username != "", "User name cannot be empty"
        password = int(password)
        if password >= 1000:
            print("Access granted")
        else:
            raise ValueError("Password is too short")
    
    except ValueError as e:
        print(e)
    
    except AssertionError as e:
        print(e)

    finally:
        print("Login attempt finished")
    
login("", "1000")