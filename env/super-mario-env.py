from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
import gym
from gym.spaces import Box
import numpy as np
from PIL import Image

class SuperMarioBrosEnv(gym.ObservationWrapper):
    def __init__(self):
        env = gym_super_mario_bros.make('SuperMarioBros-v0')
        env = JoypadSpace(env, SIMPLE_MOVEMENT)
        env.observation_space = Box(
            low=0,
            high=255,
            shape=(84, 84, 3),
            dtype=np.uint8
        )
        super(SuperMarioBrosEnv, self).__init__(env)

    def observation(self, obs):
        img = Image.fromarray(np.array(obs))
        img_resize = img.resize((84, 84))
        obs = np.array(img_resize)
        return obs

if __name__ == "__main__":
    env = SuperMarioBrosEnv()

    done = True
    for step in range(5000):
        if done:
            state = env.reset()
        state, reward, done, info = env.step(env.action_space.sample())
        print("step: {}, reward: {}, done: {}, info: {}".format(step, reward, done, info))
        #env.render()

    env.close()