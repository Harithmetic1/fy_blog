---
author: Harith Onigemo
description: Week 19, the AI model is ready to deploy to the cloud as an
  API, check out the issues i faced and how i set up the AI model for
  inference
image:
  alt: Inferences from the AI visual classifier
  url: /cv_detect.jpg
layout: ../../layouts/MarkdownPostLayout.astro
pubDate: March 01, 2024
tags:
  - home
title: Week 19 -- Code Implementation - Hosting the AI Model API
---

This week, I found an AI model on
[Huggingface](https://huggingface.co/turhancan97/yolov5-detect-trash-classification)
that uses Yolov5 for trash classification; it was trained on a dataset
of over 120k images from COCO, Trashnet, and TACO. This model would suit
my project if I did not make a model myself. I have tested it
extensively and used it as part of another project. Overall, the model
has an 80% average accuracy, classifying plastic bottles and tin cans
extremely well especially when they are isolated.

To use the AI model offline, I downloaded the weights file from the
Hugginface repo, which you can find
[here](https://huggingface.co/turhancan97/yolov5-detect-trash-classification),
then I created a class that will load the model using YOLOV5 and openCV
library and configured the model according to the documentation.
Finally, I created a method called classify, which takes an image as a
parameter and uses the model to make inferences.

![](./public/week19/media/image1.png)

These are some of the results after inference:

![](./public/week19/media/image2.png)

![](./public/week19/media/image3.png)

![A table with objects on it Description automatically
generated](./public/week19/media/image4.png)

After testing the AI model, I decided to move ahead and host it via an
API to access it from my ESP32 Cam + WIFI module or my Arduino Uno R4
WIFI. I used FastApi, a Python-backend REST framework, to host the API;
initially, I thought it worked quite well on my local device while
developing it but pushing it to the cloud for hosting was challenging.
It is either very expensive to find a cloud server to host the API
requirement, or I face many dependency issues. I ended up using Railway,
an online cloud provider for building, monitoring, and shipping
applications. So far, as I am writing this blog, I have been facing
issues with the OpenCV library as a dependency.

# Project Update

1.  Started 3D printing parts for my prototype.

2.  Purchased more parts for the prototype.

3.  Found and integrated an AI model for detecting waste

4.  Found a backend framework to host my API model.

5.  Trying to host the model in the cloud for https access (Currently
    facing dependency issues)

# Reflection

This week, I found FastApi. To be fair, I thought setting up the backend
for this project would take me a long time, but thanks to FastApi
documentation and ease-of-use I was able to set the model to work via an
API locally in a single night! I am so glad I found FastApi, anyone
looking for a backend framework for hobby projects should use FastApi.
