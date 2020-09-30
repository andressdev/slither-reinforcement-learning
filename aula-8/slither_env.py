import gym
from gym import spaces
import slither_api

class SlitherEnv(gym.Env):
  def __init__(self):
    self.lastScore = 0
    self.reset()

  def reset(self):
    self.lastScore = 0
    slither_api.beginGame()
    observation = self.getObservation()
    return observation

  def step(self, action):
    done = slither_api.endGame()
    currentScore = slither_api.readCurrentScore()
    reward = currentScore - self.lastScore
    self.lastScore = currentScore
    observation = self.getObservation()

    return observation, reward, done, {}
  
  def getObservation(self):
    return 0

  def render(self, mode='console'):
    pass