import pandas as pd
import subprocess
import os

prompt_stealer_results = pd.read_csv("../paper-reproduction-prompt-stealing-attack/output/PS_results/prompt_stealer_results.csv")

for idx, row in enumerate(prompt_stealer_results.iterrows()):
    id, inferred_prompt = row[1]['id'], row[1]['inferred_prompt']

    # run shell command here - python3 scripts/txt2img.py --n_samples 2 --prompt "inferred_prompt" --output_name "id" --skip_grid --outdir directory_path
    subprocess.run(["python",
                    "scripts/txt2img.py",
                    "--n_samples",
                    "2", "--prompt",
                    f"{inferred_prompt}",
                    "--output_name", f"{id}",
                    "--skip_grid",
                    "--outdir",
                    "directory_path_here"]
                   )
