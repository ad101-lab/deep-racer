# Promote straightness, but also stay near the center of the track.

The ideas behind this model are used is that following the centerline will allow the robot to do more advanced and fast paths, and with testing on the track we learned that the models do best when it can see more of track and has more margin for error, so we promoted staying near the center of the track. 

## Reward function

Stay straight with the trak; 2 steps at 10 and 20 degrees, also stay near the center line.

## First version

1 - 2 action space

Slow, but worked, 100% completition in sim. not very good on the physical track, it was kinda slow and was not able to stay on the track too well. 

## Second model

1 - 2.5 action space

Fast, and worked well when I tested it virtually and on the physical track. 

## Second clone 1

1 - 3 action space. 

Worked well in the virtual enviroment, got around 12 seconds, and in the physical space it was reliable and got about the same times as the virtual ones. 

## Second clone 2

1 - 4 action space

Didn't work well in the virtual enviroment. The model was unreliable and only got to aobut 50% reliablility in training, but with a fast run of 10.80 on the virtual track and more robustness built into the reward function I think this model will work well when I test it.


