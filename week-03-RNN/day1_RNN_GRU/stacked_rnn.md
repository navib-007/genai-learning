### Stacked LSTM
#### 🔁 What is a Deep RNN?
- A Deep RNN refers to a recurrent neural network with multiple layers of RNN cells (not just a single RNN layer).    
- These deeper architectures are more powerful and better at learning complex temporal patterns.

- 🧠 Think of it like stacking multiple RNNs, where the output of one layer becomes the input to the next, allowing the model to capture hierarchical representations of sequential data.

#### 🔄 What is a Bidirectional RNN?
- A Bidirectional RNN processes the input sequence in two directions:
* Forward (from start to end)
* Backward (from end to start)
- At each time step, it combines information from both directions, improving performance for tasks where context from both past and future is important.

#### 📊 Why Use Bidirectional RNN?
- In regular RNNs, predictions at time t can only use inputs from 𝑡 and before. But sometimes, the future input is also critical.

* ✅ Examples:
* Named Entity Recognition (NER): Understanding the full sentence helps decide if a word is a "Person" or "Location".
* Speech Recognition: Sound at the end of a word can help interpret its beginning.
* Sentiment Analysis: Knowing the entire sentence context improves classification.