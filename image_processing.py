import numpy as np

def simulate_image_processing():
    # -------------------------------------------------------------
    # 1. Image Initialization & Reshaping
    # -------------------------------------------------------------
    print("--- 1. Initializing and Reshaping Image ---")
    # Simulate a flat array of 16 pixels (grayscale values between 0 and 255)
    flat_pixels = np.array([
        10,  20,  30,  40,
        50,  60,  70,  80,
        90,  100, 110, 120,
        130, 140, 150, 160
    ], dtype=np.uint8)
    
    # Reshape the flat 1D array into a 4x4 2D image matrix
    image_matrix = flat_pixels.reshape(4, 4)
    print("Original 4x4 Image Matrix:\n", image_matrix)
    
    # -------------------------------------------------------------
    # 2. Slicing Specific Regions (Region of Interest - ROI)
    # -------------------------------------------------------------
    print("\n--- 2. Slicing Specific Regions (ROI) ---")
    # Extract the center 2x2 sub-matrix (rows 1-2, columns 1-2)
    center_roi = image_matrix[1:3, 1:3]
    print("Extracted Center 2x2 Region:\n", center_roi)
    
    # -------------------------------------------------------------
    # 3. Brightness Adjustment Using Broadcasting
    # -------------------------------------------------------------
    print("\n--- 3. Brightness Adjustment (Broadcasting) ---")
    brightness_offset = 40
    
    # Add scalar value to matrix (broadcasted across all elements)
    # Using np.clip to prevent 8-bit overflow (keeps values between 0 and 255)
    bright_image = np.clip(image_matrix.astype(np.int16) + brightness_offset, 0, 255).astype(np.uint8)
    print(f"Brightened Image Matrix (+{brightness_offset}):\n", bright_image)
    
    # -------------------------------------------------------------
    # 4. Matrix Multiplication for Transformation Effects
    # -------------------------------------------------------------
    print("\n--- 4. Matrix Transformation (Multiplication) ---")
    # Define a simple 4x4 transformation matrix (e.g., acts as a blending/mixing filter)
    transformation_filter = np.array([
        [0.5, 0.5, 0.0, 0.0],
        [0.0, 0.5, 0.5, 0.0],
        [0.0, 0.0, 0.5, 0.5],
        [0.5, 0.0, 0.0, 0.5]
    ])
    
    # Perform matrix multiplication (dot product) using the @ operator
    transformed_image = image_matrix @ transformation_filter
    print("Transformed Image Matrix (after filter multiplication):\n", transformed_image)

if __name__ == "__main__":
    simulate_image_processing()
