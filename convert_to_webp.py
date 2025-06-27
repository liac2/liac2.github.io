from PIL import Image
import os

input_folder = "source"
output_folder = "source-webp"  
quality = 85  # 80–85 empfohlen

os.makedirs(output_folder, exist_ok=True)

for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith(".png"):
            input_path = os.path.join(root, file)
            relative_path = os.path.relpath(input_path, input_folder)
            output_path = os.path.join(output_folder, os.path.splitext(relative_path)[0] + ".webp")

            # Zielordner erstellen, falls nötig
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            with Image.open(input_path) as img:
                img.save(output_path, "webp", quality=quality)
                print(f"✅ Konvertiert: {input_path} → {output_path}")
