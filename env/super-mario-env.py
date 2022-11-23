from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
import gym
from gym.spaces import Box
import numpy as np
import torch
from torchvision import transforms as T
from gym.wrappers import FrameStack

class SkipFrame(gym.Wrapper):
    def __init__(self, env, skip):
        """Return only every `skip`-th frame"""
        super().__init__(env)
        self._skip = skip

    def step(self, action):
        """Repeat action, and sum reward"""
        total_reward = 0.0
        for i in range(self._skip):
            # Accumulate reward and repeat the same action
            obs, reward, done, info = self.env.step(action)
            total_reward += reward
            if done:
                break
        return obs, total_reward, done, info


class GrayScaleObservation(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
        obs_shape = self.observation_space.shape[:2]
        self.observation_space = Box(low=0, high=255, shape=obs_shape, dtype=np.uint8)

    def permute_orientation(self, observation):
        # permute [H, W, C] array to [C, H, W] tensor
        observation = np.transpose(observation, (2, 0, 1))
        observation = torch.tensor(observation.copy(), dtype=torch.float)
        return observation

    def observation(self, observation):
        observation = self.permute_orientation(observation)
        transform = T.Grayscale()
        observation = transform(observation)
        return observation

class ResizeObservation(gym.ObservationWrapper):
    def __init__(self, env, shape):
        super().__init__(env)
        if isinstance(shape, int):
            self.shape = (shape, shape)
        else:
            self.shape = tuple(shape)

        obs_shape = self.shape + self.observation_space.shape[2:]
        self.observation_space = Box(low=0, high=255, shape=obs_shape, dtype=np.uint8)

    def observation(self, observation):
        transforms = T.Compose(
            [T.Resize(self.shape), T.Normalize(0, 255)]
        )
        observation = transforms(observation).squeeze(0)
        return observation

class SuperMarioBrosEnv(gym.Wrapper):
    def __init__(self):
        env = gym_super_mario_bros.make('SuperMarioBros-v0')
        env = JoypadSpace(env, [["right"], ["right", "A"]])
        env = SkipFrame(env, skip=4)
        env = GrayScaleObservation(env)
        env = ResizeObservation(env, shape=84)
        env = FrameStack(env, num_stack=4)
        super(SuperMarioBrosEnv, self).__init__(env)

if __name__ == "__main__":
    env = SuperMarioBrosEnv()

    for epi in range(10):
        state = env.reset()
        done = False
        step = 0
        while not done:
            step += 1
            state, reward, done, info = env.step(env.action_space.sample())
            print("episode: {}, step: {}, reward: {}, done: {}, info: {}, state_shape: {}".format(epi, step, reward, done, info, np.shape(state)))
            #env.render()
    env.close()