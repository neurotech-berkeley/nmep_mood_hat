# EEG Mood Hat

# Introduction

The EEG Mood Hat is artistic EEG visualizer project that works with the Muse to stream, process, and visualize the user EEG data onto an RGB LED matrix! This project is a great way to learn all the essential skills for Neurotech software projects, and a open-ended project that lets you experiment and explore your creative side with neurotechnology!

The project has been split into several sections/phases, each of which you can realistically finish in one or two sessions (hyperlinked below). 

1. Phase 1: Connecting headsets and streaming data
2. Phase 2: Data processing and MNE
3. Phase 3: Machine Learning
4. Phase 4: Circuits
5. Phase 5: Integration and Experimentation

# Phase 1: Connecting Headsets and Streaming Data

## Setting Up Your Environment
Instructions for installing miniconda can be found [here](https://docs.conda.io/projects/miniconda/en/latest/)
We would recommend installing miniconda from the command line, which can be found at the bottom of the page. Once downloaded and initialized, open a command line interface to manage environments. We'll follow the instructions on [this page](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment). Environments can be used to manage different versions of packages/python without interfering with other projects.

In order to create an environment, run the command "conda create --name [NAME]" where NAME is a name of your choosing. 
Once the environment has been created, activate it using the command "conda activate [NAME]". If activated properly, the environment name should be shown to the left of the command prompt.

Once the environment has been activated, we want to install python with "conda install python=3.9". If conda asks you "proceed ([y]/n)?", type y and press enter. 
Now that we have an environment with package managers, we want to install all the versions of the packages we want. These can be found in the requirements.txt file. To install everything, run "pip install -r requirements.txt". This should install everything needed for the project. 
To deactivate the environment, run "conda deactivate". Make sure to activate and deactivate the environment when you have started/finished your work to keep everything clean.


## Headset Information

The headset you will be using for the base version of this project is the Muse S Gen 2 (image below). 

![image](https://github.com/neurotech-berkeley/eeg_mood_hat/assets/74014913/7c564d9f-532d-4f99-be7a-e8cb728cd436)


Here are links to specifications to the Muse S, as well as some other helpful resources: 
- [Muse Product Comparison Page](https://choosemuse.my.site.com/s/article/Comparing-Muse-Headbands?language=en_US)
- [Muse S Gen 1 Technical Specification](https://images-na.ssl-images-amazon.com/images/I/71A9NwYDx9S.pdf) (should be mostly similar to the specifications of the Gen 2)
- [Muse S Product Page](https://choosemuse.com/products/muse-s-gen-2)
- [Using Muse: Rapid Mobile Assessment of Brain Performance (Paper)](https://www.frontiersin.org/articles/10.3389/fnins.2021.634147/full)

Here are the key bits of specification:
| Spec | Value |
| ----------- | ------------- |
| Wireless connection | BT 4.2 BTLE |
| EEG Channels | 4 EEG channels + 2 amplified Aux channels |
| | 256 Hz effective sample rate |
| | 12 bits/sample resolution |
| Reference electrode position | FPz (CMS/DRL) |
| Channel electrodes positions | TP9, AF7, AF8, TP10 (dry) |
| Accelerometer | Three-axis @ 52Hz, 16 bit resolution, range +/ - 4G |
| Gyroscope | +/- 1000 degrees per second |
| PPG sensor | IR/Red/Green, 64 samples/s, 16-bit resolution |
| Thermistor sensor | 12 bits/sample resolution, 16Hz sample rate |
| noise suppression | DRL – REF feedback with 2μV(RMS) noise floor |
| | No notch filter onboard |

The most important information is the EEG Channel information; we will be focusing on using streamed EEG data for the majority of the project, but you are free to stream and use data from the other sensors to extend your project in the final experimentation section! 

The Muse uses a BT 4.2 [BTLE](https://www.google.com/search?client=firefox-b-1-d&q=BTLE) connection to stream data to devices. You can hence connect the Muse to your iOS or Android devices for mobile applications, or connect to your laptops as we will do in this project. If you have an understanding of networking and wireless communications, you could create a tool to connect and directly stream information to your device, but for the sake of most projects we will use [Petals software](https://docs.petal.tech/).

### Connecting with Petals - Questions

1. Follow the [instructions on this page](https://docs.petal.tech/connect-to-muse/connect-a-muse-device) to install petals and connect to the Muse. Also make sure to follow the OS specific instructions for connecting linked on the same page. Write steps below on how to connect with the Muse.

2. The Petals Metrics software uses OSC or LSL. What are they? What is the difference between the two? What is UDP? What is the relation between UDP and OSC?

3. Read src/osc_muse_stream.py and get it to run. What is Python OSC? What is pythonosc.osc_server.ThreadingOSCUDPServer? What is pythonosc.dispatcher.Dispatcher()? 



### Troubleshooting

Sometimes Petal Metrics does not work with certain devices. If it doesn't and it is not a solvable issue, try doing the first phase of the project using muselsl and/or brainflow. Talk to other members or the leads if you want help trying this out. 

## Pipeline design





## Phase 2: Data processing and MNE
To be Released!

## Phase 3: Machine Learning
To be Released!

## Phase 4: Circuits
To be Released!

## Phase 5: Integration and Experimentation
To be Released!


## Contributers
- Anurag Rao
- Reuben Thomas
