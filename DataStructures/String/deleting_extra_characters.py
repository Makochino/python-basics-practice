s = "  _!!_Maks: Всем привет, я изучаю Python!_!!_  "

s_cleaned = s.strip().replace("_!!_", "")

parts = s_cleaned.split(":")

name = parts[0]

message = parts[1].strip()

print(f"Пользователь {name[::-1].upper()} прислал текст: {message.replace('Python', 'Git')}")




