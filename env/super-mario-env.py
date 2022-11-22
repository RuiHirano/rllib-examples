from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
import gym

class SuperMarioBrosEnv(gym.Wrapper):
    def __init__(self):
        env = gym_super_mario_bros.make('SuperMarioBros-v0')
        env = JoypadSpace(env, SIMPLE_MOVEMENT)
        super(SuperMarioBrosEnv, self).__init__(env)

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