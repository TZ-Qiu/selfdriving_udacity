qtz@QTZ-Ubuntu:~/program/python/selfdriving_udacity$ python model.py -h
Using TensorFlow backend.
loading data...
building model...
model.py:101: UserWarning: Update your `Conv2D` call to the Keras 2 API: `Conv2D(2, (3, 3), input_shape=(16, 32, 1..., activation="relu", padding="valid")`
  Conv2D(2, 3, 3, border_mode='valid', input_shape=(img_rows,img_cols,1), activation='relu'),
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
lambda_1 (Lambda)            (None, 16, 32, 1)         0
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 14, 30, 2)         20
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 3, 7, 2)           0
_________________________________________________________________
dropout_1 (Dropout)          (None, 3, 7, 2)           0
_________________________________________________________________
flatten_1 (Flatten)          (None, 42)                0
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 43
=================================================================
Total params: 63.0
Trainable params: 63.0
Non-trainable params: 0.0
_________________________________________________________________
training model...
/home/qtz/software/anaconda3/lib/python3.6/site-packages/keras/models.py:826: UserWarning: The `nb_epoch` argument in `fit` has been renamed `epochs`.
  warnings.warn('The `nb_epoch` argument in `fit` '
Train on 6420 samples, validate on 714 samples
Epoch 1/10
2017-07-20 15:29:47.397484: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-20 15:29:47.397518: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-20 15:29:47.397525: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-07-20 15:29:47.397530: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-20 15:29:47.397534: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
6420/6420 [==============================] - 0s - loss: 6.6681 - val_loss: 2.0872
Epoch 2/10
6420/6420 [==============================] - 0s - loss: 1.5532 - val_loss: 0.3957
Epoch 3/10
6420/6420 [==============================] - 0s - loss: 0.8121 - val_loss: 0.3817
Epoch 4/10
6420/6420 [==============================] - 0s - loss: 0.7198 - val_loss: 0.3689
Epoch 5/10
6420/6420 [==============================] - 0s - loss: 0.6780 - val_loss: 0.3611
Epoch 6/10
6420/6420 [==============================] - 0s - loss: 0.6324 - val_loss: 0.3549
Epoch 7/10
6420/6420 [==============================] - 0s - loss: 0.5987 - val_loss: 0.3493
Epoch 8/10
6420/6420 [==============================] - 0s - loss: 0.5477 - val_loss: 0.3448
Epoch 9/10
6420/6420 [==============================] - 0s - loss: 0.5037 - val_loss: 0.3406
Epoch 10/10
6420/6420 [==============================] - 0s - loss: 0.4798 - val_loss: 0.3354
Saving model...
Model Saved.