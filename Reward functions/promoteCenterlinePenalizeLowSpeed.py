## 45 minutes of training
## Action space: -30 - 30 degrees 0.5 - 3 m/s
## Results:
# Eval #1: 34% - 4.193 seconds
# Eval #2: 100% - 12.864 seconds
# Eval #3: 34% - 4.193 seconds
## 


def reward_function(params):

	# Calculate 3 marks that are farther and father away from the center line
	marker_1 = 0.1 * params['track_width']
	marker_2 = 0.25 * params['track_width']
	marker_3 = 0.5 * params['track_width']

	# Give higher reward if the car is closer to center line and vice versa
	if params['distance_from_center'] <= marker_1:
		reward = 1
	elif params['distance_from_center'] <= marker_2:
		reward = 0.5
	elif params['distance_from_center'] <= marker_3:
		reward = 0.1
	else:
		reward = 1e-3  # likely crashed/ close to off track

	# penalize reward for the car taking slow actions
	# speed is in m/s
	# we penalize any speed less than 0.5m/s
	SPEED_THRESHOLD = 0.5
	if params['speed'] < SPEED_THRESHOLD:
		reward *= 0.5
		
	SPEED_THRESHOLD = 1.5
	if params['speed'] < SPEED_THRESHOLD:
		reward *= 0.75
		
	SPEED_THRESHOLD = 2
	if params['speed'] < SPEED_THRESHOLD:
		reward *= 0.90


	return float(reward)