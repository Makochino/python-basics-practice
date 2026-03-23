students = {
    "Анна": 80,
    "Игорь": 72,
    "Марина": 90
}

nothing = []

for name, score in students.items():
    if score > 75:
        nothing.append(name)

print(", ".join(nothing))
