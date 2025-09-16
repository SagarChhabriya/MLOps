import pandas as pd
import sys
import yaml
import os
from pathlib import Path

# Load parameters from param.yaml

base_dir = Path(os.getcwd())
params_path = base_dir / "params.yaml"
params = yaml.safe_load(open(params_path))['preprocess']

def preprocess(input_path, output_path):
    data = pd.read_csv(input_path)


    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path, header=None, index=False)
    print(f"Preprocessed data saved to {output_path}")


if __name__=="__main__":
    preprocess(params['input'], params['output'])