for floors in range(1, 6):
    print(f"Этаж {floors}:", end = " ")
    for rooms in range(1, 5):
        hotel_rooms = (floors * 100) + rooms            
        print(f"{hotel_rooms}", end = " ")
        
    print()