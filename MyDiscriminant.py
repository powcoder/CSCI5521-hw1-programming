import numpy as np

class GaussianDiscriminant:
    def __init__(self,k=2,d=8,priors=None,shared_cov=False):
        self.mean = np.zeros((k,d)) # mean
        self.shared_cov = shared_cov # using class-independent covariance or not
        if self.shared_cov:
            self.S = np.zeros((d,d)) # class-independent covariance (S1=S2)
        else:
            self.S = np.zeros((k,d,d)) # class-dependent covariance (S1!=S2)
        if priors is not None:
            self.p = priors
        else:
            self.p = [1.0/k for i in range(k)] # assume equal priors if not given
        self.k = k
        self.d = d

    def fit(self, Xtrain, ytrain):
        # compute the mean for each class

        if self.shared_cov:
            # compute the class-independent covariance
            pass # placeholder
        else:
            # compute the class-dependent covariance
            pass

    def predict(self, Xtest):
        # predict function to get predictions on test set
        predicted_class = np.ones(Xtest.shape[0]) # placeholder

        for i in np.arange(Xtest.shape[0]): # for each test set example

            # calculate the value of discriminant function for each class
            for c in np.arange(self.k):
                if self.shared_cov:
                    pass # placeholder
                else:
                    pass

            # determine the predicted class based on the values of discriminant function


        return predicted_class

    def params(self):
        if self.shared_cov:
            return self.mean[0], self.mean[1], self.S
        else:
            return self.mean[0],self.mean[1],self.S[0,:,:],self.S[1,:,:]


class GaussianDiscriminant_Diagonal:
    def __init__(self,k=2,d=8,priors=None):
        self.mean = np.zeros((k,d)) # mean
        self.S = np.zeros((d,)) # variance
        if priors is not None:
            self.p = priors
        else:
            self.p = [1.0/k for i in range(k)] # assume equal priors if not given
        self.k = k
        self.d = d
    def fit(self, Xtrain, ytrain):
        # compute the mean for each class

        # compute the variance of different features

        pass # placeholder

    def predict(self, Xtest):
        # predict function to get prediction for test set
        predicted_class = np.ones(Xtest.shape[0]) # placeholder

        for i in np.arange(Xtest.shape[0]): # for each test set example
            # calculate the value of discriminant function for each class
            for c in np.arange(self.k):
                pass

            # determine the predicted class based on the values of discriminant function

        return predicted_class

    def params(self):
        return self.mean[0], self.mean[1], self.S
