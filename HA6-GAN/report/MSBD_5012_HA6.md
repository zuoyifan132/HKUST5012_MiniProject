#<center>MSBD 5012 HA6 report<center/>

Student Name: Zuo Yifan 
Student ID: 20876522
Assignment #: Assignment HA6
Student Email: yzuoah@connect.ust.hk
Course Name: MSBD5012

---

- Baseline:

  - Latent_size = 64
  - Discriminator number of steps: 600
  - Architecture: 
    - D: $$728\rightarrow256\rightarrow256\rightarrow1$$
    - G: $$64\rightarrow256\rightarrow256\rightarrow728$$
  
  |        FID         |
  | :----------------: |
  | 233.53466224362248 |

- Decrease latent size from 64 to 10:

  |       FID        |
  | :--------------: |
  | 245.525035634547 |

  ``Compare to the baseline result, we can see that the FID increase meaning that the quality of generated images become lower since small latent size makes the neural newtork simpler which cannot capture more infomration about the real images.``

- Increase latent size from 64 to 128:

  |        FID         |
  | :----------------: |
  | 272.71312209744684 |

  ``compare to the baseline result, we can see that the FID increase meaning that the quality of generated images become lower since larger latent size makes too much randomness involve in the newtwork which lower the images' quality.``

- Change the architecture:

  Add one more layer for discriminator:

  |        FID         |
  | :----------------: |
  | 205.74105611075774 |

  ``compare to the baseline result, we can see that the FID decrease meaning that the quality of generated images become higher since the discriminator becomes more complex and stronger, the ability of distinguish fake and real images becomes higher, the generator is hard to fool the discriminator therefore the generator can learn more about real images and produce high quality images that similar to real images.``

- Change the architecture:

  Add one more layer for generator:

  |        FID         |
  | :----------------: |
  | 318.42682769262115 |

  ``compare to the baseline result, we can see that the FID increase meaning that the quality of generated images become lower since the generator becomes more complex and stronger so that the generator can easily fool the discriminator therefore the generator gerenate bad quality images most of time``

- Increase the number of steps for discriminator:

  4 times steps of generator:

  |         FID         |
  | :-----------------: |
  | 201.532243414567178 |

  ``compare to the baseline result, we can see that the FID decrease meaning that the quality of generated images become higher since the discriminator becomes stronger due to increase number training time comapre to that of generator. The ability of discriminator to distinguish fake and real images becomes stronger, the generator is hard to fool the discriminator therefore the generator can learn more about real images and produce high quality images that similar to real images.``

- Decrease the number of steps from for discriminator:

  2 times less of steps than generator:
  
  |         FID         |
  | :-----------------: |
  | 331.102393817378381 |
  
  ``compare to the baseline result, we can see that the FID increase meaning that the quality of generated images become lower since the discriminator becomes weaker due to decrease number training time comapre to that of generator. The ability of discriminator to distinguish fake and real images becomes weaker, the generator is easy to fool the discriminator therefore the generator can learn less about real images and produce lower quality images.``
