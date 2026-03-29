import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

all_rooms = []
for floors in range(1, 6):    
    for rooms in range(1, 5):        
        all_rooms.append((floors * 100) + rooms)
                
    print()

booked_rooms = []

while True:
    
    clear_screen()            
    
    print("---ДОСТУПНЫЕ НОМЕРА В ОТЕЛЕ---")
    for f in range(1, 6):
        print(f"Этаж {f}:", end = " ")
        for r in range(1, 5):
            room = (f * 100) + r

            if room in booked_rooms:
                print(f"[{room}]", end =" ")
            else:
                print(f"{room}", end =" ")
        print()
    print("-" * 30)

    try:
        
        booking = int(input("\nВведите номер(a) перечисленные выше для бронировки\n\n(для выхода из меню напишите -> 0): "))
        
        if booking == 0: 
            break     
        
        elif booking == 103 or booking == 304: 
            print("-" * 35)
            input("Извините за неудобство, но данный момент этот номер на ремонте. С уважением администрация\n\nНажмите нажмите Enter, чтобы продолжить...")
            continue    

        elif booking in booked_rooms:
            print("-" * 35)
            input("Ой, этот номер уже зарезервировали, выберети другой из выше перечисленных:\n\nНажмите нажмите Enter, чтобы продолжить...")
            continue

        elif booking in all_rooms:
            booked_rooms.append(booking)
            print("-" * 35)
            input(f"Вы успешно зарезервировали номер: {booking}\n\nНажмите Enter, чтобы продолжить...")

        else:   
            print("-" * 35)
            input("Вы ввели не верный номер комнаты!!!\nПопробуйте снова\n\nНажмите нажмите Enter, чтобы продолжить...")
            continue

    except ValueError:
        print("-" * 35)
        input("Вы точно ввели не номер попробуйте снова:\n\nНажмите нажмите Enter, чтобы продолжить...")
        continue

found = True   

while found == True:
    
    clear_screen()
    
    print("--- ПОИСК СВОБОДНОГО НОМЕРА ---")
    for f in range(1, 6):
        print(f"Этаж {f}:", end = " ")
        for r in range(1, 5):
            room = (f * 100) + r

            if room in booked_rooms:
                print(f"[{room}]", end =" ")
            else:
                print(f"{room}", end =" ")
        print()
    print("-" * 30)
     

    try:
        floor = int(input("\nДля подбора свободной комнаты введите номер этажа(1-5)\n\n(для выхода из меню напишите -> 0): "))
        
        if floor == 0:
            print("-" * 35)
            print("\nДо новых встреч :)\n")
            found = False
        
        elif floor > 0 and floor < 6:
            for room in range(1, 5):
                possible_room = (floor * 100) + room  
                
                if possible_room == 103 or possible_room == 304:
                    print("-" * 35)
                    input((f"\nИзвините за неудобства, но комната {possible_room} на данный момент на ремонте\n\nНажмите нажмите Enter, чтобы продолжить..."))
                    continue            
                
                elif possible_room not in booked_rooms: 
                    booked_rooms.append(possible_room)
                    print("-" * 35)
                    print(f"\nВаша новая комната {possible_room} была успешно зарезервирована!\n\nПриятного пользования :)")
                    found = False
                    break
                
                else:
                    print("-" * 35)
                    input(f"\nКомната {possible_room} на данный момент занята\n\nНажмите нажмите Enter, чтобы продолжить...")
                    continue
            print()
        
        else:
            print("-" * 35)
            input("Вы точно ввели не номер попробуйте снова:\n\nНажмите нажмите Enter, чтобы продолжить...")
            continue
    
    except ValueError:
        print("-" * 35)
        input("Вы точно ввели не номер попробуйте снова:\n\nНажмите нажмите Enter, чтобы продолжить...")
        continue