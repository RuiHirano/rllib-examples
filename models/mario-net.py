import torch
from torch import nn
import copy
from ray.rllib.models.torch.torch_modelv2 import TorchModelV2
from ray.rllib.utils.typing import ModelConfigDict, TensorType
import gym
from typing import Dict, List

class MarioNet(TorchModelV2, nn.Module):
    """mini cnn structure
  input -> (conv2d + relu) x 3 -> flatten -> (dense + relu) x 2 -> output
  """

    def __init__(
        self, 
        obs_space: gym.spaces.Space,
        action_space: gym.spaces.Space,
        num_outputs: int,
        model_config: ModelConfigDict,
        name: str,
    ):
        TorchModelV2.__init__(self, obs_space, action_space, num_outputs, model_config, name)
        nn.Module.__init__(self)
        c, h, w = obs_space.shape

        if h != 84:
            raise ValueError(f"Expecting input height: 84, got: {h}")
        if w != 84:
            raise ValueError(f"Expecting input width: 84, got: {w}")

        self.model = nn.Sequential(
            nn.Conv2d(in_channels=c, out_channels=32, kernel_size=8, stride=4),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=4, stride=2),
            nn.ReLU(),
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(3136, 512),
            nn.ReLU(),
            nn.Linear(512, action_space.n),
        )


    def forward(
        self,
        input_dict: Dict[str, TensorType],
        state: List[TensorType],
        seq_lens: TensorType,
    ):
        output = self.model(input_dict["obs"].float())
        return (output, state)

    def get_q_value_distributions(self, model_out):
        """
             Returns distributional values for Q(s, a) given a state embedding.
             Override this in your custom model to customize the Q output head.
            Args:
                model_out (Tensor): Embedding from the model layers.
            Returns:
                (action_scores, logits, dist) if num_atoms == 1, otherwise
                (action_scores, z, support_logits_per_action, logits, dist)
        """
        return model_out