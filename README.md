Multivariate Anomaly Detection

Dataset:
Configurable Multidimensional Gaussian Data with standard deviation of 1

## Purpose
Gain familiarity with the algorithm by developing it from scratch.  
Hence, best ML practices such as train/test/cross-validation splits 
are NOT prioritized.  

# Run
python Runner.py  

## Implementation
Mostly as described in Andrew NG's ML lectures for Anomaly Detection.  
1. Generate multidimensional normally distributed data.
2. Calculate means for all features
3. Calculate covariance matrix for the training data
4. Use 2 and 3 to calculate the probability for all training records
5. 4 uses the formula from Andrew Ng's Coursera Lecture on   
"Anomaly Detection with the Multivariate Gaussian":
![Multivariate Gauss Anomaly Detection](img/multivariate_anomaly.PNG)  
6. Z-score is calculated for the probabilities of all training records
7. A test record is considered anomalous if the z-score of its probability  
is lower than the minimum training record probability z-score 
