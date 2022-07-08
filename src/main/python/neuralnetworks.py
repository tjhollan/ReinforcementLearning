from tensorflow.keras import models, layers, optimizers, backend as K
import numpy as np

##########################
#  Neural Network Class  #
##########################

class NeuralNetwork():

    def __init__(self, n_inputs, n_hiddens_per_layer, n_outputs, activation_function='tanh', drop=False):
        inputs = layers.Input(name="input", shape=(n_inputs,))
        hidden_layers = self._create_hidden_layers(n_hiddens_per_layer, inputs, activation_function, drop)
        outputs = layers.Dense(name="output", units=n_outputs, activation='linear')(hidden_layers)
        self.model = models.Model(inputs=inputs, outputs=outputs, name="DeepNN")

    def _create_hidden_layers(self, n_hiddens_per_layer, input_layer, activation_function, drop):
        count = 0
        previous_layer = input_layer
        for size_of_hidden_layer in n_hiddens_per_layer:
            count += 1
            layer_name = f"hidden{count:03}"
            previous_layer = layers.Dense(name=layer_name, units=size_of_hidden_layer, activation=activation_function)(previous_layer)
            if drop:
                drop_name = f"drop{count:03}"
                previous_layer = layers.Dropout(name=drop_name, rate=0.1)(previous_layer)
        return previous_layer

    def R_squared(self, y, y_hat):
        ss_res =  K.sum(K.square(y - y_hat)) 
        ss_tot = K.sum(K.square(y - K.mean(y))) 
        return ( 1 - ss_res/(ss_tot + K.epsilon()) )

    def train(self, X, T, n_epochs, learning_rate=0.001, method='adam', verbose=False):
        if method == 'adam':
            optimizer = optimizers.Adam(learning_rate=learning_rate)
        else:
            optimizer = method
        self.model.compile(optimizer=optimizer, loss='mean_absolute_error', metrics=[self.R_squared])
        verbose_number = 0 if not verbose else 1
        self.model.fit(x=X, y=T, epochs=n_epochs, batch_size=None, shuffle=True, verbose=verbose_number, validation_split=0.0)
        return self
        
    def use(self, X):
        return self.model(X, training=False)
