import numpy as np
import matplotlib.pyplot as plt

def sigmoid_function(x):
    return 1.0 / (1.0 + np.exp(-x))

class RegularizedLogisticRegression(object):
    '''
    Regularized logistic regression for binary classification.

    The weight vector w should be learned by minimizing the regularized loss
    \l(h, (x,y)) = log(1 + exp(-y <w, x>)) + \lambda \|w\|_2^2. In other words, the objective
    function that we are trying to minimize is the log loss for binary logistic regression 
    plus Tikhonov regularization with a coefficient of \lambda.
    '''
    def __init__(self):

        # parameters
        self.learningRate = 0.00001 
        self.num_epochs = 10000 
        self.batch_size = 15 
        self.weights = None

        self.lmbda = 10 

    def train(self, X, Y):
        '''
        Train the model, using batch stochastic gradient descent
        @params:
            X: a 2D Numpy array where each row contains an example, padded by 1 column for the bias
            Y: a 1D Numpy array containing the corresponding labels for each example
        @return:
            None
        '''
        samples, features = X.shape
        self.weights = np.zeros(features)

        for _ in range(self.num_epochs):
            b_index = np.random.choice(samples, self.batch_size)
            batch_X = X[b_index]
            batch_Y = Y[b_index]

            x = np.matmul(batch_X, self.weights)
            h = sigmoid_function(x)

            grad = np.matmul((h - batch_Y), batch_X) 
            grad_reg = grad + (self.lmbda * (self.weights**2))
            self.weights -= (2*self.learningRate * grad_reg) / self.batch_size

    def predict(self, X):
        '''
        Compute predictions based on the learned parameters and examples X
        @params:
            X: a 2D Numpy array where each row contains an example, padded by 1 column for the bias
        @return:
            A 1D Numpy array with one element for each row in X containing the predicted class.
        '''
        res = []
        pred = np.matmul(X, self.weights)

        for i in range(len(pred)):
            res.append(sigmoid_function(pred[i]))
        return np.where(np.array(res) > 0.5, 1, 0)

    def accuracy(self,X, Y):
        '''
        Output the accuracy of the trained model on a given testing dataset X and labels Y.
        @params:
            X: a 2D Numpy array where each row contains an example, padded by 1 column for the bias
            Y: a 1D Numpy array containing the corresponding labels for each example
        @return:
            a float number indicating accuracy (between 0 and 1)
        '''

        return np.mean(self.predict(X) == Y)

    def runTrainTestValSplit(self, lambda_list, X_train, Y_train, X_val, Y_val):
        '''
        Given the training and validation data, fit the model with training data and test it with
        respect to each lambda. Record the training error and validation error, which are equivalent 
        to (1 - accuracy).

        @params:
            lambda_list: a list of lambdas
            X_train: a 2D Numpy array for trainig where each row contains an example,
            padded by 1 column for the bias
            Y_train: a 1D Numpy array for training containing the corresponding labels for each example
            X_val: a 2D Numpy array for validation where each row contains an example,
            padded by 1 column for the bias
            Y_val: a 1D Numpy array for validation containing the corresponding labels for each example
        @returns:
            train_errors: a list of training errors with respect to the lambda_list
            val_errors: a list of validation errors with respect to the lambda_list
        '''
        train_errors = []
        val_errors = []
        for lmbda in lambda_list:
            self.lmbda = lmbda
            
            self.train(X_train, Y_train)
            
            # training error
            train_error = 1 - self.accuracy(X_train, Y_train)
            train_errors.append(train_error)
            
            # validation error
            val_error = 1 - self.accuracy(X_val, Y_val)
            val_errors.append(val_error)
            
        return train_errors, val_errors


    def _kFoldSplitIndices(self, dataset, k):
        '''
        Helper function for k-fold cross validation. Evenly split the indices of a
        dataset into k groups.

        For example, indices = [0, 1, 2, 3] with k = 2 may have an output
        indices_split = [[1, 3], [2, 0]].
        
        Please don't change this.
        @params:
            dataset: a Numpy array where each row contains an example
            k: an integer, which is the number of folds
        @return:
            indices_split: a list containing k groups of indices
        '''
        num_data = dataset.shape[0]
        fold_size = int(num_data / k)
        indices = np.arange(num_data)
        np.random.shuffle(indices)
        indices_split = np.split(indices[:fold_size*k], k)
        return indices_split

    def runKFold(self, lambda_list, X, Y, k = 3):
        '''
        Run k-fold cross validation on X and Y with respect to each lambda. Return all k-fold
        errors.
        
        Each run of k-fold involves k iterations. For an arbitrary iteration i, the i-th fold is
        used as testing data while the rest k-1 folds are combined as one set of training data. The k results are
        averaged as the cross validation error.

        @params:
            lambda_list: a list of lambdas
            X: a 2D Numpy array where each row contains an example, padded by 1 column for the bias
            Y: a 1D Numpy array containing the corresponding labels for each example
            k: an integer, which is the number of folds, k is 3 by default
        @return:
            k_fold_errors: a list of k-fold errors with respect to the lambda_list
        '''
        k_fold_errors = []
        for lmbda in lambda_list:
            self.lmbda = lmbda
            fold_errors = []
            indices = self._kFoldSplitIndices(X, k)
            for i in range(k):
                # training
                train_indices = np.concatenate([indices[j] for j in range(k) if j != i])
                X_train = X[train_indices]
                Y_train = Y[train_indices]

                # validation
                val_indices = indices[i]
                X_val = X[val_indices]
                Y_val = Y[val_indices]

                # error
                self.train(X_train, Y_train)
                val_error = 1 - self.accuracy(X_val, Y_val)
                fold_errors.append(val_error)

            k_fold_error = np.mean(fold_errors)
            k_fold_errors.append(k_fold_error)
        return k_fold_errors

    def plotError(self, lambda_list, train_errors, val_errors, k_fold_errors):
        '''
        Produce a plot of the cost function on the training and validation sets, and the
        cost function of k-fold with respect to the regularization parameter lambda. Use this plot
        to determine a valid lambda.
        @params:
            lambda_list: a list of lambdas
            train_errors: a list of training errors with respect to the lambda_list
            val_errors: a list of validation errors with respect to the lambda_list
            k_fold_errors: a list of k-fold errors with respect to the lambda_list
        @return:
            None
        '''
        plt.figure()
        plt.semilogx(lambda_list, train_errors, label = 'training error')
        plt.semilogx(lambda_list, val_errors, label = 'validation error')
        plt.semilogx(lambda_list, k_fold_errors, label = 'k-fold error')
        plt.xlabel('lambda')
        plt.ylabel('error')
        plt.legend()
        plt.show()