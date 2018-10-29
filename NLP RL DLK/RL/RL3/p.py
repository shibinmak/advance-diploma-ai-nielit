import gym;
import numpy as np;



env = gym.make("Taxi-v2");
Q = np.zeros([500,6]);






alpha = 0.618;

for episode in range(1,1000):

	state = env.reset();
#	env.render();
	reward = 0;
	cnt  = 0;
	while reward !=20  :

		cnt = cnt + 1;
		action = np.argmax(Q[state]);
#env.action_space.sample();
		state2 , reward, done, info =  env.step(action);
#	print("State : " + str(state2)  + " Action : "+ str(action) + " Cnt :  " + str(cnt) + " Reward : " + str(reward) );
	
		Q[state,action] = reward  + alpha * np.max(Q[state2])
		state = state2;
	if episode % 50 == 0:
		print(" Cnt :  " + str(cnt) + " Reward : " + str(reward) + " Episode : " + str(episode));