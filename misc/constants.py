from os import environ
from pathlib import Path
from enum import Enum
import simplejson as json


token = environ.get("TOKEN")
admin_ids = tuple(map(int, environ.get("ADMINS").split(",")))

resources_dir = Path("resources")
temp_dir = Path("/tmp", "codiim_bot")
temp_dir.mkdir(exist_ok=True)


class Emotion(Enum):
    ANGRY = 0
    HAPPY = 1
    RELAXED = 2
    SAD = 3


with Path(resources_dir, "result_phrases.json").open("r", encoding="utf-8") as file:
    result_phrases: dict[Emotion, str] = {Emotion[emotion.upper()]: value for emotion, value in json.load(file).items()}

with Path(resources_dir, "advices.json").open("r", encoding="utf-8") as file:
    advices: dict[Emotion, list[str]] = {Emotion[emotion.upper()]: value for emotion, value in json.load(file).items()}
