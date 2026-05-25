import torch
print(f"PyTorch版本: {torch.__version__}")
print(f"is available: {torch.cuda.is_available() if hasattr(torch, 'cuda') else 'CPU vesion'}")