# Adaptation of the Cross-Age Celebrity Dataset (Verification Subset)

Date: 2023-09-26  
Author: J. Chazalon

## Context and references
Face verification, i.e. the process of automatically deciding whether two pictures of a face represent the same identity, is an interesting machine learning problem as an introduction to few-shots learning. Also, many databases are available, making the problem suitable for an in-class study.

We adapted here the Verification Subset of the Cross-Age Celebrity Dataset from Chen et. al (see references below) to ease its use, separate training, validation and test sets, and shuffle the test set.

Reference publications:

> Bor-Chun Chen, Chu-Song Chen, Winston H. Hsu. Cross-Age Reference Coding for Age-Invariant Face Recognition and Retrieval, ECCV 2014

> Bor-Chun Chen, Chu-Song Chen, Winston H. Hsu. Face Recognition using Cross-Age Reference Coding with Cross-Age Celebrity Dataset, IEEE Transactions on Multimedia, 2015.

## Dataset format

This adapted dataset is split into 3 subsets:

- `train/` directory: training set containing 3200 images pairs
- `val/` directory: validation set containing 400 images pairs
- `test/` directory: test set containing 400 images pairs

Each subset as an equal number of positive (same identity) and negative (different identities) pairs.

For each set the naming of the images have the following format: `NNNN_P.jpg` where

- `NNNN` is a 4 digits number representing the pair ID within the current subset
- `P` $\in \{0, 1\}$ is the image ID (left or right image)

**For the training and validation sets**, every two pairs is positive, and the other negative, i.e.:

- if `NNNN` is even, then the pair is a positive example (same identity)
- if `NNNN` is odd, then the pair is a negative example (different identities)

For the test set only, pair IDs were randomized. For teachers, we made available a separate file named `CACD_VS_cropped_test_targets.npy` which contains a table mapping pair IDs to a boolean value indicating whether the current pair is positive or negative.


## Image preprocessing
All images were produced by cropping the original dataset images using an implementation of MTCNN, and the images were aligned using landmarks and resized to the shape `(160, 160, 3)`. Each image is saved as an RGB JPEG image.

When loading the images, appropriate preprocessing / normalization should be applied.
The [facenet-pytorch](https://github.com/timesler/facenet-pytorch) implementation we used simply applies the following transforms sequentially:

- convert to float32
- convert to Tensor
- center `(image_tensor - 127.5) / 128.0`

## License
This adapted dataset version is for internal use only, and must not be redistributed.
