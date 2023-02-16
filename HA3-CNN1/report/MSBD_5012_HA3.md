#<center>MSBD 5012 HA3 report<center/>

Student Name: Zuo Yifan 
Student ID: 20876522
Assignment #: Assignment HA3 
Student Email: yzuoah@connect.ust.hk
Course Name: MSBD5012

---

- Baseline:

  | Loss                                                         | Accuracy                                                     |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/baseline.png" alt="baseline" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/baseline_1.png" alt="baseline_1" style="zoom:50%;" /> |

- Alter number of hidden layer experiment:

  - Add two more hidden layer:

    We add nn.Linear(84, 60) and nn.Linear(60, 30) change fc3 to nn.Linear(30, 10)

    |                             Loss                             |                           Accuracy                           |
    | :----------------------------------------------------------: | :----------------------------------------------------------: |
    | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/two_more_hidden_layer.png" alt="two_more_hidden_layer" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/two_more_hidden_layer_1.png" alt="two_more_hidden_layer_1" style="zoom:50%;" /> |

    ``Compare to the baseline result, we can see that the loss decreases slower and the accuracy decreases which is due to the difficulty of gradients to propagate back to the lower layers since we add two more hidden layers.``

  - Drop one hidden layer:

    We drop fc2.

    |                             Loss                             |                           Accuracy                           |
    | :----------------------------------------------------------: | :----------------------------------------------------------: |
    | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/one_less_hidden_layer.png" alt="one_less_hidden_layer" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/one_less_hidden_layer_1.png" alt="one_less_hidden_layer_1" style="zoom:50%;" /> |

    ``Compare to the baseline result, we can see that the loss decreases slightly faster and the accuracy increases, because the less hidden layer we have, the easier the gradients can propagate back to the lower layers.``

- Alter number of filters experiment:

  - Increase number of filters:

    We increase conv1 filters from 6 to 15 and conv2 filters from 16 to 30.

    |                             Loss                             |                           Accuracy                           |
    | :----------------------------------------------------------: | :----------------------------------------------------------: |
    | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/add_filters.png" alt="add_filters" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/add_filters_1.png" alt="add_filters_1" style="zoom:50%;" /> |

    ``Compare to the baseline result, we can see that the loss decrease slightly faster  and the accuracy increases, because we increase the number of filters on convolutional layers increases the number of units in fc1 from 16*5*5 to 30*5*5, since the number of filters increases helps the modules learn more about different features from images which helps classify images.``

  - Decrease number of filters:

    We increase conv1 filters from 6 to 4 and conv2 filters from 16 to 6.

    |                             Loss                             |                           Accuracy                           |
    | :----------------------------------------------------------: | :----------------------------------------------------------: |
    | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/drop_filters.png" alt="drop_filters" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/drop_filters_1.png" alt="drop_filters_1" style="zoom:50%;" /> |

    ``Compare to the baseline result, we can see that the loss decrease slower and the accuracy decreases, because decreasing the number of filters on convolutional layers decreases the number of units in fc1 from 16*5*5 to 6*5*5, since the number of filters decreases, module get less features about images and higher loss decreases the accuracy.``

- Alter learning rate experiment:

  - Decrease learning rate:

    Learning rate from 0.001 to 0.0001

    |                             Loss                             |                           Accuracy                           |
    | :----------------------------------------------------------: | :----------------------------------------------------------: |
    | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/decrease_learing_rate.png" alt="decrease_learing_rate" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/decrease_learning_rate_1.png" alt="decrease_learning_rate_1" style="zoom:50%;" /> |

    ``Compare to the baseline result, we can see that the loss decrease slower and the accuracy decreases a lot, becrease in gradient descent process, decreasing learning rate means shrinking the step moved in the opposite direction of the derivative which leads to slow learning and low accuracy comparing with same amount of learning.``

  - Increase learning rate:

    Learning rate from 0.001 to 0.01

    |                             Loss                             |                           Accuracy                           |
    | :----------------------------------------------------------: | :----------------------------------------------------------: |
    | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/rise_learning_rate.png" alt="rise_learning_rate" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/rise_learning_rate_1.png" alt="rise_learning_rate_1" style="zoom:50%;" /> |

    ``Compare to the baseline result, we can see that the loss nearly remain the same over mini-batches and the accuracy decreases a lot, becrease in gradient descent process, we rising learning rate too much which leads to the step moved in the opposite direction of the derivative too much to miss the minima which leads to slow learning and low accuracy comparing with same amount of learning. ``

- Alter optimization method experiment:

  - AdaGrad:

    |                             Loss                             |                           Accuracy                           |
    | :----------------------------------------------------------: | :----------------------------------------------------------: |
    | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/AdaGrad.png" alt="AdaGrad" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/AdaGrad_1.png" alt="AdaGrad_1" style="zoom:50%;" /> |

    ``Compare to the baseline result, we can see that the loss decreases a little faster  then nearly remain the smae and the accuracy decreases a lot. This is because at the beginning stage the learning is fast and historical gradients is large, AdaGrad make the learning rate become small, then the learning is really slow which leads to low accuracy comparing with smae amount of learning. ``

  - Adam:

    |                             Loss                             |                           Accuracy                           |
    | :----------------------------------------------------------: | :----------------------------------------------------------: |
    | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/Adam.png" alt="Adam" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/Adam_1.png" alt="Adam_1" style="zoom:50%;" /> |

    ``Compare to the baseline result, we can see that the loss decreases dramatically faster than baseline and the accuracy increase a little since Adam combines RMSProp and Momentum which is the best optimizer over others, Adam dramatically increase learning speed. ``

  - RMSProp:

    |                             Loss                             |                           Accuracy                           |
    | :----------------------------------------------------------: | :----------------------------------------------------------: |
    | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/RMSProp.png" alt="RMSProp" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/RMSProp_1.png" alt="RMSProp_1" style="zoom:50%;" /> |

    ``Compare to the baseline result, we can see that the loss decreases dramatically faster then baseline and the accuracy is nearly the same. Since RMSProp use the same idea of AdaGrad except it uses an exponentially decaying average to discard history gradients from the extreme past. This optimizer perform better than Adagrad but no better than Adam.``

- Use batch normalization experiment:

  |                             Loss                             |                           Accuracy                           |
  | :----------------------------------------------------------: | :----------------------------------------------------------: |
  | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/batch_normalization.png" alt="batch_normalization" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/batch_normalization_1.png" alt="batch_normalization_1" style="zoom:50%;" /> |

  ``Compare to the baseline result, we can see that the loss decreases dramatically faster then baseline and the accuracy increases. This is because batch normalization makes different layers more independent and avoids covariate shift which accelerate training.``

---

# <center>Best Performance<center/>

- By dropping some hidden layers and increasing number of filters with Adam optimization and batch normalization, the best performance I can get is:

  |                             Loss                             |                           Accuracy                           |
  | :----------------------------------------------------------: | :----------------------------------------------------------: |
  | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/Best_performance.png" alt="Best_performance" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA3-CNN1/report/Best_performance_1.png" alt="Best_performance_1" style="zoom:50%;" /> |

  