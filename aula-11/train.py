import gym

from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines import DQN
from slither_env import SlitherEnv

env = SlitherEnv()

model = DQN(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=100)
model.save("slither_train1")