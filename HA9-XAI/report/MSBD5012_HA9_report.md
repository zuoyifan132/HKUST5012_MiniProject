#<center>MSBD 5012 HA9 report<center/>

Student Name: Zuo Yifan 
Student ID: 20876522
Assignment #: Assignment HA9
Student Email: yzuoah@connect.ust.hk
Course Name: MSBD5012

---

- Grad_cam:

  - |        |           Predictive scores           |                       Gra_CAM Heat map                       | Lime Heat map                                                |
    | :----: | :-----------------------------------: | :----------------------------------------------------------: | ------------------------------------------------------------ |
    | 1.png  |     'n11879895', 'rapeseed', 1.0      | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/heatmap/1_heatmap.jpeg" alt="1_heatmap" style="zoom:33%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/Lime_heatmap/1_heatmap.png" alt="1_heatmap" style="zoom:50%;" /> |
    | 2.png  |      'n01806143', 'peacock', 1.0      | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/heatmap/2_heatmap.jpeg" alt="2_heatmap" style="zoom:33%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/Lime_heatmap/2_heatmap.png" alt="2_heatmap" style="zoom:50%;" /> |
    | 3.png  |       'n04613696', 'yurt', 1.0        | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/heatmap/3_heatmap.jpeg" alt="3_heatmap" style="zoom:33%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/Lime_heatmap/3_heatmap.png" alt="3_heatmap" style="zoom:50%;" /> |
    | 4.png  |     'n03544143', 'hourglass', 1.0     | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/heatmap/4_heatmap.jpeg" alt="4_heatmap" style="zoom:33%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/Lime_heatmap/4_heatmap.png" alt="4_heatmap" style="zoom:50%;" /> |
    | 5.png  | 'n04562935', 'water_tower', 0.9999994 | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/heatmap/5_heatmap.jpeg" alt="5_heatmap" style="zoom:33%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/Lime_heatmap/5_heatmap.png" alt="5_heatmap" style="zoom:50%;" /> |
    | 6.png  |    'n02391049', 'zebra', 0.9999896    | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/heatmap/6_heatmap.jpeg" alt="6_heatmap" style="zoom:33%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/Lime_heatmap/6_heatmap.png" alt="6_heatmap" style="zoom:50%;" /> |
    | 7.png  | 'n04146614', 'school_bus', 0.9999945  | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/heatmap/7_heatmap.jpeg" alt="7_heatmap" style="zoom:33%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/Lime_heatmap/7_heatmap.png" alt="7_heatmap" style="zoom:50%;" /> |
    | 8.png  |   'n03938244', 'pillow', 0.99999976   | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/heatmap/8_heatmap.jpeg" alt="8_heatmap" style="zoom:33%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/Lime_heatmap/8_heatmap.png" alt="8_heatmap" style="zoom:50%;" /> |
    | 9.png  |  'n03344393', 'fireboat', 0.9999939   | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/heatmap/9_heatmap.jpeg" alt="9_heatmap" style="zoom:33%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/Lime_heatmap/9_heatmap.png" alt="9_heatmap" style="zoom:50%;" /> |
    | 10.png |  'n02966193', 'carousel', 0.9999975   | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/heatmap/10_heatmap.jpeg" alt="10_heatmap" style="zoom:33%;" /> | <img src="/Users/sakazuho/Desktop/HKUST/first_term/5012/ha/HA9-XAI/report/Lime_heatmap/10_heatmap.png" alt="10_heatmap" style="zoom:50%;" /> |

    Interesting Finding:

    Base on the RestNet50 by using Grad-CAM, it all focus on the center of the images since the center of the images are the identified objects which dominant in the images. Note that in 6.png which identifies the image as zebra, note that the zebra far away from camera is less significant compare to the zebra which near the camera, but the former is still be counted. 

  - Comparison:

    On 3.png, the Grad_CAM is focus on center of image but the Lime is focus on the top corner of the yurt which is clearly a shape of triangle. In the 9.png, we see that Grad_CAM is focus on the water be jet instead of the boat, but the Lime is more focus on then boat instead of the water jet.