from transformers import pipeline;

import torch
def get_device():
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("Using CUDA")
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
        print("Using MPS")
    else:
        device = torch.device("cpu")
        print("Using CPU")
    return device

get_device()
print(pipeline('sentiment-analysis')('I love you'))