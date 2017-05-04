""" Three layer neural network
"""

# Package imports
import numpy as np


# Neural Network class
class Neural_Network:

    def __init__(self, input_layer, hidden_layer, output_layer):
        """
        input_layer   # no. of neurons in input layer
        hidden_layer  # no. of neurons in hidden layer
        output_layer  # no. of neurons in output layer
        """
        # biases for hidden layer
        self.bh = np.random.randn(hidden_layer,1)
        # weights for input layer to hidden layer
        self.wh = np.random.randn(hidden_layer, input_layer)
        
        # biases for output layer
        self.bo = np.random.randn(output_layer,1)
        # weights for hidden layer to output layer
        self.wo = np.random.randn(output_layer, hidden_layer)


    def train(self, training_data, passes, learning_rate):
        """
        Train the neural network using gradient descent.
        The ``training_data`` is a list of tuples ``(x, y)``
        representing the training inputs and the desired
        outputs.
        """
        for j in range(passes):
            self.update(training_data, learning_rate)
            if (j % 1000) == 0:
                print("Pass {0} complete".format(j))


    def update(self, training_data, learning_rate):
        """
        Update the network's weights and biases by applying
        gradient descent using backpropagation.
        """
        m = len(list(training_data))
        nabla_bh = np.zeros(self.bh.shape)
        nabla_wh = np.zeros(self.wh.shape)
        nabla_bo = np.zeros(self.bo.shape)
        nabla_wo = np.zeros(self.wo.shape)
        
        for x, y in training_data:
            delta_nabla_bh, delta_nabla_wh, delta_nabla_bo, delta_nabla_wo = \
                            self.backprop(x, y)
            nabla_bh = nabla_bh + delta_nabla_bh
            nabla_wh = nabla_wh + delta_nabla_wh
            nabla_bo = nabla_bo + delta_nabla_bo
            nabla_wo = nabla_wo + delta_nabla_wo
            
        self.wh = self.wh - (learning_rate / m) * nabla_wh
        self.bh = self.bh - (learning_rate / m) * nabla_bh
        self.wo = self.wo - (learning_rate / m) * nabla_wo
        self.bo = self.bo - (learning_rate / m) * nabla_bo

        
    def backprop(self, x, y):
        """
        Return a tuple ``nabla_b, nabla_w`` for output and hidden layers
        """
        nabla_bh = np.zeros(self.bh.shape)
        nabla_wh = np.zeros(self.wh.shape)
        nabla_bo = np.zeros(self.bo.shape)
        nabla_wo = np.zeros(self.wo.shape)
        
        # feedforward
        # input to hidden
        zh = []
        sig_h = []
        for b, w in zip(self.bh, self.wh):
            z = np.dot(w, x)+ b
            zh.append(z)
            sig_h.append(sigmoid(z))

        # hidden to output
        zo = []
        sig_o = []
        for b, w in zip(self.bo, self.wo):
            z = np.dot(w, sig_h)+ b
            zo.append(z)
            sig_o.append(sigmoid(z))
            
        # backward pass
        # output to hidden
        err = [actual - expected for actual, expected in zip(sig_o,y)]
        delta = [error * der for error, der in zip(err, sigmoid_der(zo))]
        nabla_bo = delta
        nabla_wo = np.dot(delta, np.array(sig_h).transpose())
        
        # hidden to input
        delta = np.dot(self.wo.transpose(), delta) * sigmoid_der(zh)
        nabla_bh = delta
        nabla_wh = np.dot(delta, [x])

        return (nabla_bh, nabla_wh, nabla_bo, nabla_wo)


    def test(self, test_data):
        """
        Return the test results for the test data
        """
        test_results = self.output(test_data)
        return test_results[0]
    
    
    def output(self, a_in):
        """
        For input "a_in" calculate output by applying biases, weights and sigmoid function:
          a = sigma(weights * a_in + biases)
        """
        # input layer to hidden layer
        zs = [a + b for a, b in zip(np.dot(self.wh, a_in), self.bh)]
        ah = [sigmoid(z) for z in zs]
        # hidden layer to output layer
        a_out = np.round(sigmoid(np.dot(self.wo, ah) + self.bo))
        return a_out.transpose()

# sigma functions

def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))


def sigmoid_der(zs):
    """Derivative of the sigmoid function."""
    return [sigmoid(z)*(1-sigmoid(z)) for z in zs]

