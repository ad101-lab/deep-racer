# The reward function

The reward function is how you determine how the robot is doing in each itteration of the model

## Tips

* Return a very small number by default to make convergence faster(1e-3)
* You should keep the reward from 0-1

## Different examples

### Staying on track

Use one of the input booleans for all wheels on track to give variable reward

* Pros
  * Can create faster paths
  * Easy to understand
* Cons
  * Since this doesn't reward and specific actions this type of function will take longer to converge on a faster solution
  * Isn't able to find the most optimal solution because you only have to keep one wheel on the track by the rules

### Following the centerline



### Preventing Zig-Zag



## Reward function inputs

Use fewer because this will keep it simple and make it easier for you

[Reward function input parameters](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-input.html)

## How you can improve your reward function

Use these variables, tune the ammount of reward each item gives. Change the prioritization of these parameters. Adjust one item at a time to find which one caused it. 

