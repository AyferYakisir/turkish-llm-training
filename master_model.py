import torch
import torch.nn as nn

def get_rotary_position_encoding(input: torch.Tensor, base=10000, device="cpu"):
    # input shape: (batch_size, context_length, dimension)
    batch_size, context_length, dimension = input.shape

    assert dimension % 2 == 0, "dimension must be even"

    half_dim = dimension // 2

    freqs_indices = torch.arange(0, half_dim, device=device, dtype=torch.float32)
    freqs = 1.0 / (base ** (freqs_indices / half_dim))  # shape: (half_dim,)

    positions = torch.arange(0, context_length, device=device, dtype=torch.float32).unsqueeze(1)  # (context_length, 1)
    angles = positions * freqs  # (context_length, half_dim)

    sin_angles = torch.sin(angles).unsqueeze(0).expand(batch_size, -1, -1)  # (batch_size, context_length, half_dim)
    cos_angles = torch.cos(angles).unsqueeze(0).expand(batch_size, -1, -1)  # (batch_size, context_length, half_dim)

    x1 = input[:, :, :half_dim]
    x2 = input[:, :, half_dim:]

    rotated_x1 = x1 * cos_angles - x2 * sin_angles
    rotated_x2 = x1 * sin_angles + x2 * cos_angles

    return torch.cat([rotated_x1, rotated_x2], dim=-1)


class MasterModel(nn.Module):
  def __init__(self, vocab_size, embedding_dim, context_length):
    super().__init__()

    self.embedding = nn.Embedding(vocab_size, embedding_dim)
    self.pos_embedding = nn.Embedding(context_length, embedding_dim)
    self.get_pos = get_rotary_position_encoding
 
  def forward(self, x):

    if isinstance(x, list):
        x = torch.tensor(x, dtype=torch.long).unsqueeze(0)  

    elif isinstance(x, torch.Tensor) and x.dim() == 1:
        x = x.unsqueeze(0)

    x = x.to(next(self.parameters()).device)

    x = self.embedding(x)
    x = self.get_pos(x)

    return x



    
    