# Promote straightness

We used a reward function that promotes the robot following the path straight. We used a dicrete action space from 0-2.5 m/s with 3 increments and -30 to 30 degrees with 5 increments. This model got 11.984 seconds and around 12 on the physical track with good reliability.

## Promote straightness 15 - 30 degrees

### Action space

Discrete

1-3 3 steps
-30 - 30 5 steps

15 actions

### Results

#### Virtual

##### Training

Rough, but it kinda got ther

##### Evaluation



#### Physical

Runs off of track occationally, cannot finnish a lap. Fast though.

## Promote straightness 15-30 degrees copy

### Action space

Same

### Results

#### Virtual

1. 11.794 - 100%
2. 6.199 - 52%
3. 11.741 - 100%

#### Physical

Same behaviour wasn't able to get it to stay on track

Wasn't able to test it in any other way

## Promote straightness 15-30 degrees copy 1.3-4 action space

### Action space

Increased max speed to 4

### Results

#### Virtual

9.398 second run 2 other runs that failed badly. It was a good model in sim when it worked.

#### Physical

Same behaviour, I think i have to retrain the base model and test it more on the physical track before I make this many models

Wasn't able to test it in any other way

## Promote straightness 15-30 degrees copy oval track

### Action space

Remained the same

### Results

#### Virtual

(On oval track)
1. 13.458 - 100%
2. 5.749 - 41%
3. 5.801 - 44%

Really cacious usually, but it worked well enough.

#### Physical

Way better, was able to stay on track. I think this behavior had something to do with the oval track having stricter sidelines that didn't exist in the other tracks. I am going to implement something like this in my code so that the model will preform better on the physical track.

I timed the car and at 95% speed it was able to get in the 12-14 range consistently

In 3 minutes it got 13 laps and only messed up 2 times.

## Takeaways from the training

We have to add more options to the preformance function to optimize preformance on the physical track. This will include adding a outer bound near the edges of the track so the model will always have more room for error and making the training more strict.i


All of the preformance functions are in the models folder. They will also be linked here when I complete all of that.
