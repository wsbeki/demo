import gym
#建立一个环境
env = gym.make('CartPole-v0')
for i_episode in range(20):
    #给环境一个监视
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        #确定事件
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break