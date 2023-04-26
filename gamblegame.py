
def return_expected_reward(reward_list, win_probability_list):
  expected_reward = [0,0,0,0,0,0,0,0,0,0]
  endurance_probability = [1,1,1,1,1,1,1,1,1,1]
  cumulative_reward = []
  for i in range(0,len(reward_list)):
    cumulative_reward.append(reward_list[i])
    endurance_probability[i] = win_probability_list[i]
    for j in range(0,i):
      endurance_probability[i] = endurance_probability[i] * win_probability_list[j]
      cumulative_reward[i]=cumulative_reward[i]+reward_list[j]
    print()
    print()
    print("endurance_probability for round " + str(i+1) + " is " + str(endurance_probability[i]))
    print("cumulative reward for round " + str(i+1) + " is " + str(cumulative_reward[i]))
    expected_reward[i] = cumulative_reward[i] * endurance_probability[i]
    print()
    print()
    print("expected reward for round " + str(i+1) + " is " + str(expected_reward[i]))
  return expected_reward


if (__name__ == "__main__"):
  expected_reward=return_expected_reward([100,500,1000,5000,10000,50000,100000,500000,1000000,5000000],[0.99,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1])
  print()
  print()
  print(" round " + str(expected_reward.index(max(expected_reward))+1) + " is ideal for quitting")
  print("maximum expected reward is " + str(max(expected_reward)))
      
    