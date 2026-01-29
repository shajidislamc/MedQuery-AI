import os
from dotenv import load_dotenv
import yaml

try:
    from pyprojroot import here 
except Exception:
    from pathlib import Path

    def here(p = ""):
        root = Path(__file__).resolve().parents{2}
        return root / p if p else root
    
import shutil
