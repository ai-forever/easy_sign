from sys import platform
import onnxruntime as rt
from einops import rearrange
import numpy as np

if platform in {"win32", "win64"}:
    import onnxruntime.tools.add_openvino_win_libs as utils
    utils.add_openvino_libs_to_path()


class Predictor:
    def __init__(self, model_config):
        """
        Initialize the Predictor class.

        Args:
            model_config (dict): Model configuration containing path_to_model,
                path_to_class_list, threshold, and topk values.
        """
        self.config = model_config
        self.provider = self.config["provider"]
        self.threshold = self.config["threshold"]
        self.labels = {}

        self.model_init(self.config["path_to_model"])
        self.create_labels()

    def create_labels(self):
        """
        Create a dictionary of labels from the provided path_to_class_list.
        """
        with open(self.config["path_to_class_list"], "r") as f:
            labels = [line.strip() for line in f]
            labels = self.decode_preds(labels)

            idx_lbl_pairs = [x.split("\t") for x in labels]
            self.labels = {int(x[0]): x[1] for x in idx_lbl_pairs}


    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

    def predict(self, x):
        """
        Make a prediction using the provided input frames.

        Args:
            x (list): List of input frames.

        Returns:
            dict: Dictionary containing predicted labels and confidence values.
        """
        clip = np.array(x).astype(np.float32) / 255.0
        clip = rearrange(clip, "t h w c -> 1 c t h w")

        prediction = self.model([self.output_name], {self.input_name: clip})[0]
        prediction = self.softmax(prediction)
        prediction = np.squeeze(prediction)
        topk_labels = prediction.argsort()[-self.config["topk"] :][::-1]
        topk_confidence = prediction[topk_labels]

        result = [self.labels[lbl_idx] for lbl_idx in topk_labels]
        if np.max(topk_confidence) < self.threshold:
            return None

        return {
            "labels": dict(zip([i for i in range(len(result))], result)),
            "confidence": dict(zip([i for i in range(len(result))], topk_confidence)),
        }

    def model_init(self, path_to_model: str) -> None:
        """
        Load and init the ONNX model using the provided path.

        Args:
            path_to_model (str): Path to the ONNX model file.

        Returns:
            None
        """
        session = rt.InferenceSession(path_to_model, providers=[self.provider])
        self.input_name = session.get_inputs()[0].name
        self.output_name = session.get_outputs()[0].name

        self.model = session.run

    def decode_preds(self, data):
        if platform in {"win32", "win64"}:
            data = [i.encode("cp1251").decode("utf-8") for i in data]
        return data