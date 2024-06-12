import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# # Sample dataset of bit strings and their categories
# bit_strings = ["10101010", "01010101", "11110000", "00001111", "10111100"]
# categories = ["A", "B", "A", "B", "C"]

# # Convert bit strings to numerical features
# X = np.array([[int(bit) for bit in bit_string] for bit_string in bit_strings])

# # Convert categories to numerical labels
# label_encoder = LabelEncoder()
# y = label_encoder.fit_transform(categories)

path = "data_0_cloned"

data = []
for file in os.listdir(path):
    f = open(os.path.join(path,file), "r")
    s = f.read()
    d = [int(x) for x in s]
    data.append(d)

# randomized categories
categories = list(np.random.randint(low = 3,size=50))

X = np.array(data)
y = np.array(categories)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

size = X_train.shape[1]
print(size)
# Define the RNN model
model = Sequential([
    LSTM(128, input_shape=(size, 1)),  # LSTM layer with 64 units
    Dense(3, activation='softmax')                # Output layer with softmax activation for multi-class classification
])

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Reshape input data to fit the LSTM input shape
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=1, verbose=2)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy:", accuracy)