# Signature Verification Using Deep Learning (CNN)
## Project Overview
This project presents a deep learning approach to verify signatures using a Convolutional Neural Network (CNN). Signature verification is an important application in identity authentication, helping in areas such as banking, legal documents, and security systems.

Our model aims to differentiate between genuine and forged signatures by learning unique signature patterns through supervised training.

## Table of Contents
- Project Overview
- Project Features
- Data Overview
- Model Architecture
- Results and Performance
- Requirements
- Future Scope
- References

## Project Features
- Signature Data Processing: Structured approach to handling real and forged signature samples.
- CNN Model: Built using Convolutional Neural Networks for feature extraction and signature classification.
- Accuracy Evaluation: Performance metrics used to evaluate model efficacy.

## Data Overview
The dataset consists of:
- Genuine and forged signatures for multiple individuals.
- Training and Testing Folders: The data is divided into train and test folders.
- Real Signatures: Stored under folders named by ID numbers (e.g., 001, 002).
- Forged Signatures: Stored under folders with IDs and _forg suffix (e.g., 001_forg, 002_forg).

## Model Architecture
Our CNN model is designed to capture spatial patterns in signatures, structured with:
- Convolutional Layers: To extract essential features of signature patterns.
- Pooling Layers: To reduce dimensionality and retain critical information.
- Fully Connected Layers: For classification of genuine and forged signatures.

## Layer-by-Layer Breakdown

<img width="460" alt="image" src="https://github.com/user-attachments/assets/eaf8979f-3b90-4c10-b5a5-7b9919d50cc2">


## Results and Performance
- Accuracy: Achieved an accuracy of around 98% on test data.
- Loss and Accuracy Graphs: Visualized performance across epochs.
- ROC Curve: Used to assess true positive rates vs. false positive rates.

## Requirements
- Python 3.x
- TensorFlow 2.x
- Numpy, Pandas (for data handling)
- Matplotlib (for visualization)

## Future Scope
This project currently uses CNN for classification. Potential improvements include:

- Incorporating Transformers: For enhanced learning of signature patterns.
- Transfer Learning: Applying pre-trained models to boost performance with limited data.
- Real-time Application: Deploying the model in web or mobile applications for practical use.

## References
[1] M. Ishfaq, A. Saadia, F. M. Alserhani and A. Gul, "Enhancing Security: Infused Hybrid Vision
 Transformer for Signature Verification," in IEEE Access, vol. 12, pp. 137504-137521, 2024
 
[2] V. Sreelekshmi, K. Pavithran and J. J. Nair, "SwinCNN: An Integrated Swin Transformer and
 CNN for Improved Breast Cancer Grade Classification," in IEEE Access, vol. 12, pp. 68697-68710,
 2024

[3]  X. Yang and L. Duan, "MPTC-FPN: A Multilayer Progressive FPN With Transformer-CNN
 Based Encoder for Salient Object Detection," in IEEE Access, vol. 10, pp. 98816-98827, 2022
 
[4] R. D. Rai and J. S. Lather, "Handwritten Signature Verification using TensorFlow," 2018 3rd
 IEEE International Conference on Recent Trends in Electronics, Information & Communication
 Technology (RTEICT), Bangalore, India, 2018, pp. 2012-2015
 
[5] R. Tolosana, R. Vera-Rodriguez, J. Fierrez and J. Ortega-Garcia, "DeepSign: Deep On-Line
 Signature Verification," in IEEE Transactions on Biometrics, Behavior, and Identity Science, vol. 3,
 no. 2, pp. 229-239, April 2021
