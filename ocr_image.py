import easyocr
import time

# --- SETUP ---
# This only needs to be done once. It will download the models for Hebrew and English.
print("Loading OCR models... (This might take a moment on the first run)")
# The list ['he', 'en'] tells EasyOCR which languages to look for.
reader = easyocr.Reader(['he', 'en']) 

IMAGE_PATH = 'thumbnails/300001.png' # <--- Put the path to your image here

# --- OCR PROCESS ---
print(f"Reading text from {IMAGE_PATH}...")
start_time = time.time()

# The readtext method is the core of EasyOCR.
# detail=0 gives you just the text, detail=1 gives you coordinates and confidence.
results = reader.readtext(IMAGE_PATH, detail=0, paragraph=True)

end_time = time.time()
print(f"OCR completed in {end_time - start_time:.2f} seconds.")

# --- DISPLAY RESULTS ---
print("\n--- Extracted Text ---")
for line in results:
    print(line)