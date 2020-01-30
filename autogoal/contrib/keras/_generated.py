from keras.layers import Conv1D as _Conv1D
from keras.layers import Dense as _Dense
from keras.layers import Embedding as _Embedding
from keras.layers import LSTM as _LSTM
from keras.layers import Reshape, MaxPool1D, Flatten, Bidirectional

from autogoal.grammar import Boolean, Categorical, Discrete, Continuous


class Seq2SeqLSTM(_LSTM):
    def __init__(
        self,
        units: Discrete(32, 1024),
        activation: Categorical("tanh", "sigmoid", "relu", "linear"),
        recurrent_activation: Categorical("tanh", "sigmoid", "relu", "linear"),
        dropout: Continuous(0, 0.5),
        recurrent_dropout: Continuous(0, 0.5),
    ):
        super().__init__(
            units=units,
            activation=activation,
            recurrent_activation=recurrent_activation,
            dropout=dropout,
            recurrent_dropout=recurrent_dropout,
            return_sequences=True,
        )


class Seq2VecLSTM(_LSTM):
    def __init__(
        self,
        units: Discrete(32, 1024),
        activation: Categorical("tanh", "sigmoid", "relu", "linear"),
        recurrent_activation: Categorical("tanh", "sigmoid", "relu", "linear"),
        dropout: Continuous(0, 0.5),
        recurrent_dropout: Continuous(0, 0.5),
    ):
        super().__init__(
            units=units,
            activation=activation,
            recurrent_activation=recurrent_activation,
            dropout=dropout,
            recurrent_dropout=recurrent_dropout,
            return_sequences=False,
        )


class Seq2SeqBiLSTM(Bidirectional):
    def __init__(
        self,
        merge_mode: Categorical("sum", "mul", "concat", "ave"),
        units: Discrete(32, 1024),
        activation: Categorical("tanh", "sigmoid", "relu", "linear"),
        recurrent_activation: Categorical("tanh", "sigmoid", "relu", "linear"),
        dropout: Continuous(0, 0.5),
        recurrent_dropout: Continuous(0, 0.5),
    ):
        super().__init__(
            layer=_LSTM(
                units=units,
                activation=activation,
                recurrent_activation=recurrent_activation,
                dropout=dropout,
                recurrent_dropout=recurrent_dropout,
                return_sequences=True,
            ),
            merge_mode=merge_mode,
        )


class Seq2VecBiLSTM(Bidirectional):
    def __init__(
        self,
        merge_mode: Categorical("sum", "mul", "concat", "ave"),
        units: Discrete(32, 1024),
        activation: Categorical("tanh", "sigmoid", "relu", "linear"),
        recurrent_activation: Categorical("tanh", "sigmoid", "relu", "linear"),
        dropout: Continuous(0, 0.5),
        recurrent_dropout: Continuous(0, 0.5),
    ):
        super().__init__(
            layer=_LSTM(
                units=units,
                activation=activation,
                recurrent_activation=recurrent_activation,
                dropout=dropout,
                recurrent_dropout=recurrent_dropout,
                return_sequences=False,
            ),
            merge_mode=merge_mode,
        )


class Reshape2D(Reshape):
    def __init__(self):
        super().__init__(target_shape=(-1, 1))


class Embedding(_Embedding):
    def __init__(self, output_dim: Discrete(32, 128)):
        super().__init__(input_dim=1000, output_dim=output_dim)


class Dense(_Dense):
    def __init__(self, units: Discrete(128, 1024), **kwargs):
        super().__init__(units=units, **kwargs)


class Conv1D(_Conv1D):
    def __init__(self, filters: Discrete(5, 20), kernel_size: Categorical(3, 5, 7)):
        super().__init__(filters=filters, kernel_size=kernel_size, padding="causal")