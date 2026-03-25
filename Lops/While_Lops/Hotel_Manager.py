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
            input("Извините за неудобство, но данный момент этот номер на ремонте. С уважением администрация\n\nНажмите нажмите любую клавишу, чтобы продолжить...")
            continue    

        elif booking in booked_rooms:
            input("Ой, этот номер уже зарезервировали, выберети другой из выше перечисленных:\n\nНажмите нажмите любую клавишу, чтобы продолжить...")
            continue

        elif booking in all_rooms:
            booked_rooms.append(booking)
            input(f"Вы успешно зарезервировали номер: {booking}\n\nНажмите нажмите любую клавишу, чтобы продолжить...")
        
        else:   
            input("Вы ввели не верный номер комнаты!!!\nПопробуйте снова\n\nНажмите нажмите любую клавишу, чтобы продолжить...")
            continue

    except ValueError:
        print("Вы точно ввели не номер попробуйте снова:")
        continue
    
