import cv2
import matplotlib.pyplot as plt

# ---------- STEP 1: Load your image ----------
image_path = "images.jpg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image file '{image_path}' not found.")

# ---------- STEP 2: Convert to grayscale ----------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ---------- STEP 3: Apply Global Thresholding ----------
T = 127  # Threshold value
_, thresh = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)

# ---------- STEP 4: Save the thresholded image ----------
output_filename = "threshold_output.png"
cv2.imwrite(output_filename, thresh)
print(f"Thresholded image saved as '{output_filename}'")

# ---------- STEP 5: Display ----------
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Grayscale")
plt.imshow(gray, cmap="gray")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title(f"Global Threshold (T={T})")
plt.imshow(thresh, cmap="gray")
plt.axis("off")

plt.show(block=True)
