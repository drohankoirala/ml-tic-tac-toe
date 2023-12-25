import os

if not os.path.exists('learn.csv'):
    print('File missing [res/learn.csv], ')
    exit()

from tensorflow import keras
import pandas as pd

data = pd.read_csv('learn.csv').drop_duplicates()

gf = ['a', 'b', 'c']
features = data[gf]
target = data['won']


def trainN():
    model = keras.Sequential([
        keras.layers.Dense(64, input_shape=(3,), activation='relu', kernel_initializer='he_normal'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(32, activation='relu', kernel_initializer='he_normal'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    model.fit(features, target, epochs=2000)
    model.save('learn.keras')


trainN()
