# Checklist

## Data

1. Understand data and how much noise is present in it.
    1. Spend enough time exploring your data. Really understand its distribution, annotations and if its balanced or not. Is there noise? Too much noise?
    1. Solve data imbalance if imbalanced by undersampling and other techniques described in the chapter. Are your metrics correct depending on the data distribution
1. Shuffle dataset before training to ensure that you’re showing a random distribution in each batch.
1. Win small then win big: Try to overfit on a small representative dataset and then train with all the data.
1. Data Preprocessing
    1. Use Mean centering so normalize your dataset and make it follow a normal distribution as much as possible. Basically, Subtract mean, Normalize variances, Use same mu and sigma to normalize train and test set. The advantage is that normalized data is more symmetric - so you can use a lower learning rate on it
    1. If using a pretrained model, then use its own preprocessing functions.
1. Perform data augmentation that is relevant to the application and dataset
    1. Eg for text 90 degrees doesn't make much sense
    1. For selfies +- 30 is good
1. Don’t mix dimensions
    1. Sometimes height and width can be confused. Aspect ratios should be maintained

## Training

1. Develop a quick and simple/linear baseline
    1. This helps in confirming the need of a complex network and show that your network actually performs better.
1. Don’t be a hero: Use pretrained models and perform transfer learning.
1. Run quicker tests on small input size, then when you find the best set of parameters and model, train on the standard size
1. Be bug free: Verify all vectorizing code is working as expected
1. Parameters
    1. Initialize your model correctly: If all weights are zero, then you have a symmetric network which wont learn anything. If you initialize with too large a number then youll have saturation of activation function. If its too small, the weights will change values too easily and will be unstable. Ensure that train, test and val are all from the same distribution
    1. Initialize your parameters correctly. Always use random search. Use Xavier and He initializations for weights
    1. Use dropout. Dropout is applied both during forward prop and back prop but not during test time. Dropout at test time adds random noise - which is unwanted. When dropout is being used then the cost function is no longer well defined, so a handy check to make sure that code is working properly is to set keep-prob = 1 and then run and make sure cost function is monotonically decreasing and then run again with keep-prob as you want. 
    1. Batch normalization: Makes hyperparams search easier, Makes network robust to hyperparams, Makes deeper networks easier to train. Really useful in Normalizing hidden units elements. As a result, higher layer weights become more robust with respect to lower layer weights. During test time keep mu and sigma as exponentially weighted average.
    1. Regularization is key
    1. Adam is your pal optimizer
    1. Prefer ELU activation or Glorot.
        1. But if you really want to use tanh, use Xavier initialization.
    1. Schedule your learning rate. If learning rate is constant the loss will just meander around the minimum never reaching the actual global min. With smaller learning rate, you will meander around a smaller region, hopefully reaching the global min
    1. Don't let your gradients explode - the live visualization help in this
    1. Why use non linear activation function? If you don't use nonlinear activation function, the neural net always gives you a linear transformation no matter what the depth of the network (just multiply weight matrices from all the layers). The entire power of deep neural nets comes from the nonlinearities that help it better approximate arbitrary real-world functions.
1. Understand bias and variance:
    1. Overfitting is high variance - because it covers absolutely all training examples.
    1. Underfitting is high bias - because it covers only a few training examples.
    1. Bias is over training set, variance is over val set
1. Occam's Razor: Make the model as simple as possible. 
1. Early stop or loose late: Train your model with Early stopping enabled or you may realize too late that training failed.
1. Aren’t you ensembling yet?
1. Keep it LIT (Let It Train)
1. Are you using the correct loss function?
    1. Cross entropy loss - a handy check is the first loss should usually be ln(1/number of classes) as it is a random result. The second epoch loss should usually jump higher
    1. Sudden drop in loss - there was an issue in weights

## Tracebility

1. Keep a log of all updates you did to your model, dataset, annotation and what effect it had. Use existing tools to help out. Build pipelines whenever possible.
1. Keep a human baseline for comparison
