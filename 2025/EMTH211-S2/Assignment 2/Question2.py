'''Assignment 2
SEAN FAULKNER EMTH211-S2
Question 2'''

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os

def load_image_to_array(filename):
    """Loads an image and converts it to a NumPy array in range [0, 1]."""
    image = mpimg.imread(filename).astype(np.float64)

    # Normalize to [0, 1] if needed
    if image.max() > 1.0:
        image /= 255.0

    # Remove alpha channel if present
    if image.shape[2] == 4:
        image = image[..., :3]

    return image


def svd_colour_channels(image, channel):
    """Applies SVD on one of the image's colour channels."""
    U, S, Vt = np.linalg.svd(image[:, :, channel], full_matrices=False)
    return U, S, Vt


def reconstruct_channel(U, S, Vt, k):
    """Reconstructs a single colour channel with rank k."""
    return U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]


def svd_method(image, k, image_num):
    """Applies SVD on all three colour channels and reconstructs an image of rank k."""
    # Perform SVD per colour channel
    U_r, S_r, Vt_r = svd_colour_channels(image, 0)
    U_g, S_g, Vt_g = svd_colour_channels(image, 1)
    U_b, S_b, Vt_b = svd_colour_channels(image, 2)

    # Reconstruct each channel using the top k singular values
    new_red = reconstruct_channel(U_r, S_r, Vt_r, k)
    new_green = reconstruct_channel(U_g, S_g, Vt_g, k)
    new_blue = reconstruct_channel(U_b, S_b, Vt_b, k)

    # Stack the three channels back into a colour image
    reconstructed_image = np.stack([new_red, new_green, new_blue], axis=2)
    reconstructed_image = np.clip(reconstructed_image, 0, 1)

    # Save the reconstructed image
    mpimg.imsave(f"image{image_num}_rank{k}.png", reconstructed_image)

    return reconstructed_image


def display_results(image, ranks, image_num):
    """Displays the reconstructed images for each rank."""
    fig, axs = plt.subplots(1, len(ranks) + 1, figsize=(18, 6))

    # Show original image
    axs[0].imshow(image)
    axs[0].set_title("Original")
    axs[0].axis("off")

    # Loop through each rank and show reconstruction
    for i, rank in enumerate(ranks):
        reconstructed_image = svd_method(image, rank, image_num)
        display_compression(image, rank)
        axs[i + 1].imshow(reconstructed_image)
        axs[i + 1].set_title(f"Rank {rank}")
        axs[i + 1].axis("off")

    plt.tight_layout()
    fig.savefig(f"image_{image_num}_comparison.png")
    plt.show()

def display_compression(image, rank):
    """Shows the change in numbers stored in terms of rank"""
    m, n, _ = image.shape  # height, width, channels

    # How many numbers are stored for one color channel:
    # U: m*k, S: k, Vt: k*n
    single_channel_storage = m * rank + rank + n * rank

    # For three channels:
    compressed_total = 3 * single_channel_storage

    # Original image storage:
    original_total = 3 * m * n

    compression_ratio = compressed_total / original_total

    print("\nCompression Analysis:")
    print(f"Image dimensions: {m} x {n}")
    print(f"Rank used: {rank}")
    print(f"Original storage: {original_total} numbers")
    print(f"Compressed storage: {compressed_total} numbers")
    print(f"Compression ratio: {compression_ratio:.4f}")

if __name__ == "__main__":
    image_1 = "/Users/seanfaulkner/Desktop/image1.png"
    image_3 = "/Users/seanfaulkner/Desktop/image5.png"
    image_paths = [image_3] #image_3]

    ranks = [360]

    image_num = 1
    for path in image_paths:
        image = load_image_to_array(path)
        display_results(image, ranks, image_num)
        image_num += 1
