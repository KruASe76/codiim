from pathlib import Path

import torch
from torchvision.models import EfficientNet_B5_Weights as base_model_weights
from PIL import Image

from misc.constants import resources_dir, Emotion


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = torch.load(Path(resources_dir, "model.pt"), map_location=device)
model.eval()

transforms = base_model_weights.IMAGENET1K_V1.transforms()


def predict(image_path: Path) -> Emotion:
    with torch.no_grad():
        return Emotion(torch.argmax(model(transforms(Image.open(image_path)).unsqueeze(0).to(device))).item())
