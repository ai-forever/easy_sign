from collections import deque

import cv2

from utils import SLInference


def main(config_path):
    """
    Main function of the app.
    """

    cap = cv2.VideoCapture(0)

    inference_thread = SLInference(config_path)
    inference_thread.start()

    gestures_deque = deque(maxlen=5)

    while True:
        _, img = cap.read()
        img_resized = cv2.resize(img, (224, 224))
        inference_thread.input_queue.append(img_resized)

        gesture = inference_thread.pred
        if gesture not in ['no', '']:
            if not gestures_deque:
                gestures_deque.append(gesture)
            elif gesture != gestures_deque[-1]:
                gestures_deque.append(gesture)

        if gestures_deque:
            print(gestures_deque[-1])

        cv2.imshow("img", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main("configs/config.json")