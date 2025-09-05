#!/usr/bin/env python3
"""
Upload CAD-LLM model to Hugging Face Hub
"""

import os
from huggingface_hub import HfApi, login, create_repo

# Configuration
HF_REPO = "polaris314/cadgpt-gpt2-train"
MODEL_DIR = "/home/ubuntu/cad-llm/cad_llm"

def upload_model_to_hf():
    """Upload the trained model to Hugging Face Hub"""
    
    # Load HF token
    with open("/home/ubuntu/cad-llm/notebooks/hf_token.txt", "r") as f:
        HF_TOKEN = f.read().strip()
    
    # Login to HF
    login(token=HF_TOKEN)
    
    # Initialize API
    api = HfApi(token=HF_TOKEN)
    
    # Create repository if it doesn't exist
    print(f"🚀 Creating/checking repository: {HF_REPO}")
    create_repo(HF_REPO, private=True, exist_ok=True, token=HF_TOKEN)
    
    # Check if model directory exists
    if not os.path.exists(MODEL_DIR):
        print(f"❌ Model directory not found: {MODEL_DIR}")
        return
    
    # Upload model files
    print(f"📦 Uploading model from {MODEL_DIR} to {HF_REPO}")
    
    try:
        api.upload_folder(
            folder_path=MODEL_DIR,
            repo_id=HF_REPO,
            token=HF_TOKEN,
            commit_message="Upload trained CAD-LLM GPT-2 model"
        )
        print(f"✅ Model successfully uploaded to {HF_REPO}")
        print(f"🔗 View your model at: https://huggingface.co/{HF_REPO}")
        
    except Exception as e:
        print(f"❌ Upload failed: {e}")

if __name__ == "__main__":
    upload_model_to_hf()
