import torch
from contextLength import context_length
from positional_embedding import meanings

def get_rotary_position_encoding(input: torch.Tensor, base=10000, device="cpu"):
  batch_size, context_length, dimension = input.shape

  assert dimension % 2 == 0, "dimension must be even"

  half_dimension = dimension // 2

  freqs_indices = torch.arange(0, half_dimension, device=device, dtype=torch.float32)

  freqs = 1.0 / (base ** (freqs_indices / dimension))

  positions = torch.arange(0, context_length, device=device, dtype=torch.float32).unsqueeze(1)

  angles = positions * freqs

  sin_angles = torch.sin(angles)
  cos_angles = torch.cos(angles)

  input_even = input[:, :dimension // 2]
  input_odd = input[:, dimension // 2:] 

  input_even_rotated = input_even * cos_angles - input_odd * sin_angles
  input_odd_rotated = input_even * sin_angles + input_odd * cos_angles
  
  input_rotated = torch.empty_like(input)

  input_rotated[:, :dimension // 2] = input_even_rotated
  input_rotated[:, dimension // 2:] = input_odd_rotated

  return input_rotated

torch.manual_seed(1)
random_input = torch.randn(context_length, 4)

pos_rotary_encodings = get_rotary_position_encoding(random_input)
print(pos_rotary_encodings)

meanings_with_pos_encodings = get_rotary_position_encoding(meanings)
print(meanings_with_pos_encodings, meanings)