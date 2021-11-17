from dotenv import load_dotenv
import os

load_dotenv("../tmp.env")

POKEMON_PATH = os.getenv("POKEMON_PATH")
ATTAQUE_PATH = os.getenv("ATTAQUE_PATH")
DEFENSE_PATH = os.getenv("DEFENSE_PATH")
