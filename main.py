import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np


def detect_text(image_Path, threshold=0.25):
    """Detects text in an image using EasyOCR .

    Args:
        image_path (str): The path to the image.
        threshold (float): The minimum score required for a text detection to be considered valid.

    Returns:
        list: A list of text detections, each of which is a tuple of (bbox, text, score).
    """

    # Create a GPU-accelerated reader.
    reader = easyocr.Reader(['en'], gpu=True)

    # Detect text on the image.
    detected_text = reader.readtext(img)

    # Filter out text detections with a score below the threshold.
    text_ = [t for t in detected_text if t[2] > threshold]

    return text_


def draw_box():
    # Draw the bounding boxes and text on the image.

    for bbox, text, score in text_:
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 3)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.60, (255, 0, 0), 2)


if __name__ == "__main__":
    image_path = 'download (2).jpg'
    img = cv2.imread(image_path)
    text_ = detect_text(image_path)

    draw_box()

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
