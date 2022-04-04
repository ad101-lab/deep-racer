import math

# Fix Calculations
# Add stay on track code.
# Last model that used this was fast
# Discrete action space; 30-30 5 actions 0-2.5 3 actions
# 

def reward_function(params):
    ###############################################################################
    '''
    Example of using waypoints and heading to make the car point in the right direction
    '''

    # Read input variables
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    # Initialize the reward with typical value
    reward = 1.0

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD1 = 15.0
    DIRECTION_THRESHOLD2 = 25.0
    directionOff = False
    if direction_diff > DIRECTION_THRESHOLD2:
        reward *= 0.3
        directionOff = True
    elif direction_diff > DIRECTION_THRESHOLD1:
        reward *= 0.7
        directionOff = True
    
    if params['distance_from_center'] > 0.4*params['track_width']:
        reward *= 0.001
    
    return reward