import skimage
import numpy as np
import argparse

def generate_snippet(img, color, start, end, target_height):
    

    height, width, _ = img.shape

    start_pixels = np.array((int(start[1] * height), int(start[0] * width)))
    end_pixels = np.array((int(end[1] * height), int(end[0] * width)))
    # rr, cc = skimage.draw.rectangle_perimeter((1, 1), end=(height - 2, width - 2), shape=img.shape)

    snippet = np.copy(img[start_pixels[0]:end_pixels[0], start_pixels[1]:end_pixels[1]])
    rr, cc = skimage.draw.rectangle_perimeter(start_pixels, end=end_pixels, shape=img.shape)
    img[rr, cc] = color
    rr, cc = skimage.draw.rectangle_perimeter(start_pixels + 1, end=end_pixels - 1, shape=img.shape)
    img[rr, cc] = color
    rr, cc = skimage.draw.rectangle_perimeter(start_pixels + 2, end=end_pixels - 2, shape=img.shape)
    img[rr, cc] = color

    scale = img.shape[0] / snippet.shape[0]
    snippet = skimage.transform.rescale(snippet, (scale, scale, 1), preserve_range=True)
    height, width, _ = snippet.shape
    rr, cc = skimage.draw.rectangle_perimeter((1, 1), end=(height - 2, width - 2), shape=snippet.shape)
    snippet[rr, cc] = color
    rr, cc = skimage.draw.rectangle_perimeter((2, 2), end=(height - 3, width - 3), shape=snippet.shape)
    snippet[rr, cc] = color
    rr, cc = skimage.draw.rectangle_perimeter((3, 3), end=(height - 4, width - 4), shape=snippet.shape)
    snippet[rr, cc] = color
    return snippet


def create_image_snippets(input_file):
    img = skimage.io.imread(input_file)

    target_height = 720
    scale = target_height / img.shape[0]
    img = skimage.transform.rescale(img, (scale, scale, 1), preserve_range=True, anti_aliasing=True)

    snippet1 = generate_snippet(img, (0, 255, 255), (0.07, 0.7), (0.13, 0.9), target_height)
    snippet2 = generate_snippet(img, (255, 255, 0), (0.35, 0.035), (0.55, 0.35), target_height)
    snippet3 = generate_snippet(img, (255, 0, 255), (0, 0.95), (0.02, 1), target_height)

    # stacked = np.hstack((img, snippet3, snippet1, snippet2))

    skimage.io.imsave("input_with_boxes.png", img)
    skimage.io.imsave("snippet1.png", snippet1)
    skimage.io.imsave("snippet2.png", snippet2)
    skimage.io.imsave("snippet3.png", snippet3)
    # skimage.io.imsave("stacked.png", stacked)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create image snippets')
    parser.add_argument('-input', type=str)

    args = parser.parse_args()
    create_image_snippets(args.input)
