import os
from PIL import Image
import numpy as np
from pytorch_fid import fid_score

# Resize real event poster images to 256x256
real_posters_dir = "event_posters"
generated_dir = './generated_posters'  # Directory containing generated posters

def resize_posters(folder_path, target_size=(256, 256)):
    for filename in os.listdir(folder_path):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            filepath = os.path.join(folder_path, filename)
            try:
                img = Image.open(filepath).convert("RGB")
                img = img.resize(target_size)
                img.save(filepath)  # Overwrite the original image
            except Exception as e:
                print(f"Error resizing {filename}: {e}")

# Resize posters in both directories
resize_posters(real_posters_dir)  # Resize real posters

# Calculate FID score after ensuring all images have the same size
fid_value = fid_score.calculate_fid_given_paths([real_posters_dir, generated_dir], batch_size=50, device='cpu', dims=2048)
print(f"FID Score: {fid_value}")
