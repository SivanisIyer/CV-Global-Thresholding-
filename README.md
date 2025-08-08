# CV-Global-Thresholding-

# 🧠 CV Global Thresholding

This project demonstrates **Global Thresholding** in Computer Vision using OpenCV. It is a fundamental image processing technique used to convert grayscale images into binary images by applying a fixed threshold value across the entire image.

---

## 📌 What is Global Thresholding?

Global Thresholding is a basic image segmentation technique where a **single constant threshold** is applied to all the pixels in an image:

- If the pixel intensity is **greater than or equal** to the threshold → it is set to **maximum value** (usually 255).
- If the pixel intensity is **less** than the threshold → it is set to **0**.

This produces a **binary image** that highlights regions of interest based on pixel intensity.

---

## 🖼️ Input

A grayscale image (`images.jpg`) is used for thresholding.

---
## Output
The output is a binary image where pixel intensities are either 0 or 255 based on the defined threshold value (e.g., 127).
