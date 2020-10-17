# Sentiment Analysis- Amazon Mobile Phones Product Reviews

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Directory Tree](#directory-tree)
  * [To Do](#to-do)
  * [Bug / Feature Request](#bug---feature-request)
  * [Technologies Used](#technologies-used)
  * [Team](#team)
  * [License](#license)
  * [Resources](#resources)
  

## Overview
Sentiment analysis refers to the class of computational and natural language processing based techniques used to identify, extract or characterize subjective information, such as opinions, expressed in a given piece of text. The main purpose of sentiment analysis is to classify a writer’s attitude towards various topics into positive, negative or neutral categories.Sentiment analysis has gain much attention in recent years. In this paper, we aim to tackle the problem of sentiment polarity categorization, which is one of the fundamental problems of sentiment analysis. A general process for sentiment polarity categorization is proposed with detailed process descriptions. Data used in this study are online product reviews collected from amazon. Experiments for both sentence-level categorization and review-level categorization are performed with promising outcomes. At last, we also give insight into our future work on sentiment analysis.

## Technical Aspect

In order to have an efficient object detection (here, the vehicle number plates), I have used the most recently developed algorithm of YOLO series i.e. YOLOv4 backed up over a framework of Darknet.

Yolov4: Yolo abbreviates to You Only Look Once depicting its ability to detect objects and entities by using CNN (Convolutional Neural Network).Neural Network in YOLO uses weights trained by the user through annotated training data by using bounding boxes. Hence YOLO takes an image as input puts it through a Neural Network and gives the output in the image through bounding boxes.The input image is divided into SXS grid of cells.Each cell contributes to the object detection. Each cell predicts Bounding Boxes as well as Class probabilities. The prediction consists of 5 components (x,y,w,h,confidence).(x,y) represents the centre of the bounding box and (w,h) are the width and the height of the boxes.Confidence represents the Estimated Prediction Accuracy of the object.YOLO is extremely fast and accurate as compared to other algorithms and hence was our primary choice for this project.

![](https://github.com/ikigai-aa/Automatic-License-Plate-Recognition/blob/master/images/architecture.png)
