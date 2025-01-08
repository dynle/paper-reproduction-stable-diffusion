import pandas as pd
import subprocess
import os

prompt_stealer_results = pd.read_csv("../paper-reproduction-prompt-stealing-attack/output/PS_results/prompt_stealer_results.csv")
# Start from the 1817th row where the previous run left off
filtered_results = prompt_stealer_results.iloc[3531:]

# Set the environment variable to use GPU 1
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

for idx, row in enumerate(filtered_results.iterrows()):
    id, inferred_prompt = row[1]['id'], row[1]['inferred_prompt']

    # run shell command here - python3 scripts/txt2img.py --n_samples 2 --prompt "inferred_prompt"
    subprocess.run(["python", "scripts/txt2img.py", "--n_samples", "2", "--prompt", f"{inferred_prompt}", "--output_name", f"{id}", "--skip_grid", "--outdir", "/data1/d-lee/ex2_generated_imgs"])
