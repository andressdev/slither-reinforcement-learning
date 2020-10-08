import gym
from gym import spaces
import slither_api
import numpy as np
import time

class SlitherEnv(gym.Env):
  def __init__(self):
    n_actions = 8
    self.action_space = spaces.Discrete(n_actions)
    self.width = 956
    self.height = 515
    self.observation_space = spaces.Box(low=0, high=255, shape=(self.height, self.width, 1), dtype=np.uint8)
    self.lastScore = 0
    self.initTime = time.time()
    #self.reset()

  def reset(self):
    self.initTime = time.time()
    self.lastScore = 0
    slither_api.beginGame()
    observation = self.getObservation()
    return observation

  def step(self, action):
    self.takeAction(action)
    done = slither_api.endGame()
    currentTime = time.time()
    diffTime = currentTime - self.initTime
    if(diffTime < 10): done = False
    currentScore = slither_api.readCurrentScore()
    reward = currentScore - self.lastScore
    self.lastScore = currentScore
    observation = self.getObservation()
    print('Current Score: ', currentScore, 'Reward: ', reward, 'Done: ', done)
    return observation, reward, done, {}
  
  def takeAction(self, action):
    if action == 0:
      slither_api.moveTop()
    elif action == 1:
      slither_api.moveDown()
    elif action == 2:
      slither_api.moveLeft()
    elif action == 3:
      slither_api.moveRight()
    elif action == 4:
      slither_api.moveTopLeft()
    elif action == 5:
      slither_api.moveTopRight()
    elif action == 6:
      slither_api.moveDownLeft()
    elif action == 7:
      slither_api.moveDownRight()
    
  def getObservation(self):
    return slither_api.returnGameScreen(self.width, self.height)

  def render(self, mode='console'):
    pass