# Online News Popularity Prediction
### Project for DS4400: Machine Learning/Data Mining 1 SEC 04 F2025

## Introduction
Online news plays a central role in shaping public discourse, distributing information, and influencing social behavior, yet the factors that drive an article’s popularity remain difficult to predict. Understanding what makes content widely shared is increasingly important for media organizations, marketers, and analysts who aim to optimize audience engagement. This project examines whether the popularity of a news article—measured through total social media shares—can be modeled using traditional machine learning methods. By analyzing the metadata, linguistic attributes, sentiment measures, and structural features of thousands of online articles, this study evaluates how these characteristics relate to engagement and whether predictive patterns exist.

Our dataset, Online News Popularity, was published by the UCI Machine Learning Repository and retrieved directly from their public archive. It is provided as a structured CSV containing nearly 40,000 articles and 58 predictive attributes, each describing different aspects of article composition, subject matter, and publication behavior. The dataset enables a comprehensive exploration of how written content, sentiment, topic, and multimedia elements influence an article’s likelihood of being shared widely across social networks.

https://archive.ics.uci.edu/dataset/332/online+news+popularity

## Objectives
Determine the following:
1. Which features most strongly influence article popularity, including linguistic complexity, sentiment polarity, engagement-related metrics, and publication timing.
2. Whether regularization improves predictive performance, by comparing Linear Regression, Ridge (L2), and Lasso (L1) models.
3. How model complexity affects overfitting and underfitting, measured through validation performance, RMSE, MAE, and coefficient behavior.
4. Whether dimensionality reduction (PCA) enhances generalization, and how compressed representations compare to full-feature modeling.

## Team
Brianna Quinn & Bingqiao Qian
