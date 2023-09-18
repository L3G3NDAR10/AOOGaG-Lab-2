from PIL import Image, ImageDraw

# Встановлюємо розміри вікна
canvas_width = 540
canvas_height = 960

# Створюємо пусте полотно
canvas = Image.new('RGB', (canvas_width, canvas_height), 'white')
draw = ImageDraw.Draw(canvas)

# Зчитуємо датасет з файлу "DS8.txt"
dataset_filename = "DS8.txt"

with open(dataset_filename, 'r') as file:
    lines = file.readlines()

# Перетворюємо рядки у координати
dataset = []
for line in lines:
    parts = line.strip().split()
    if len(parts) >= 2:
        x, y = map(int, parts[:2])
        dataset.append((x, y))

# Відображаємо точки на полотні
for x, y in dataset:
    draw.point((x, y), fill='blue')

# Зберігаємо результат у графічний файл (замініть "output.png" на ім'я файлу, у який ви хочете зберегти результат)
output_filename = "output.png"
canvas.save(output_filename)

# Виводимо результат
canvas.show()

# Виводимо повідомлення про успішне завершення
print(f"Результат збережено в файлі {output_filename}")
