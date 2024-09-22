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

To "submit" and push code for us and your peers to help with, you should push your code to a separate branch of the nmep_mood_hat remote repository. Have your full name in the branch name, as well as any additional information you wish (if you are making additional branches to temporarily test features). 

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




## Phase 2: Pipeline and Processing Blocks

_This section assumes you have an understanding of Python classes and [abstract classes](https://www.scaler.com/topics/abstract-class-in-python/)._

Pipelining is a data processing design in which data is passed through a series of blocks, each of which usually run some type of processing. In hardware design, parts of these blocks could be adders and multipliers. In software these could be reusable parts of processing code for different applications. 

In our project, we have three main types of classes of interest, and these can seen in the `BCI.py` file: `BCI`, `Pipe`, and `ProcessingBlock`.

**_BCI:_** This class is the first block of your pipeline. The BCI object is the first store/set of queues from which future blocks will receive data (see the "Multithreading" section below), and handles most of the handling with the Petals software and other streaming protocols to actually start streaming in data from your headset. You can take a look at the docstring for the class for more information about the class variables. 

**_Pipe:_** This class is the most fundamental "non-BCI" class, and essentially passes an identical copy of the data it receives to one or multiple processing blocks later in the pipeline (this will be very crucial for processing data in parallel and blocks that require multiple of the same output). 

_**ProcessingBlock:**_ An abstract class that serves as the template for all other processing blocks. It requires that all `ProcessingBlock` classes have an `__init__()` function, a `launch_server()` function that starts the block up to recieve and process data, and a `action()` function that actually does processing and is called by the `launch_server()` function. 



### Multithreading

Take a look at these videos and articles that explain multithreading:
- [(Article) Multithreading explained](https://www.techtarget.com/whatis/definition/multithreading)
- [(Video) Python Threading Library Explained in 8 Minutes](https://www.youtube.com/watch?v=A_Z1lgZLSNc)

Multithreading is used all over this project, and enables us to optimize a lot of the processing and to keep the output display rate as close as possible to "real time". As we can see above, the Muse S has a sampling rate of 256 Hz, which means it sends 256 samples every second. Your computer's CPU works at a **much** faster rate (what is the processing frequency of your laptop's CPU?), and hence there is a lot of work that could be done in between each sample. 

If we waited to recieve a sample, completed all the processing for that sample, and only _then_ looked for the next sample to process, we would waste a lot of time. In fact, we may actually spend more time than it would take to recieve the next sample. Many processing blocks also require a minimum number of samples before computing a value (e.g. averaging and PSD), which makes this waiting time even longer.

By using multithreading and queues, we can collect data while a block is held up computing on a particular set of samples, and make the processing done by different blocks independent of each other, which speeds up computation. 

Take a look at the `BCI.py` file, specifically the `BCI` and `Pipe` classes. You can see similar functions and behaviors as used in the Python Threading Library tutorial above, as well as the extensive usage of queues to handle the passing of data between different blocks. 

Questions to answer:

4. What is the default streaming protocol used in the `BCI` class? How does the `BCI` class switching between the two streaming protocols?
5. Queues are a data structure that follows FIFO - "First In First Out". Typically, the `deque` class is used when a queue data structure is required. What is special about the `Queue.queue` class that makes it useful for multithreading?
6. The `Pipe` class is an identity map: it takes samples and outputs the same samples. The `Pipe` class also has the option to take this input and send multiple copies to n sets of outupus, a "dimension 1 to dimension n" identity map. Why is this necessary for having data accessed by more than one block? Why can't the two blocks access the data directly by running `.get()` on the same input store? (Think about data races).


### Pipe Test

**Write a Python test file that uses the classes and functions in `BCI.py` to test the functionality of the `Pipe` class.** Create a set of 2 animations side-by-side using `matplotlib`, one showing the input data to the `Pipe` object, and the other showing the output of the `Pipe` instance. A successful `Pipe` and test file should have identical graphs, and should run pretty fast. **Include a GIF of this testbench working in your project documentation/report.**

**_Common errors_**:
- `Matplotlib`'s `animation.FuncAnimation` has an optional argument `interval` that determines the delay in milliseconds between each frame. This is set to 200ms by default, which would make your code _seem_ very slow. Decreasing this value (to the minimum viable number) will solve this problem.
- ChatGPT sometimes has meltdown understanding how to correct errors with `animation.FuncAnimation`. Look at documentation and examples online, these are often more reliable than wrestling with an LLM for an hour.


> [!NOTE]
> You should be writing test files like this to test the functionality of every processing block you write, and saving some result of a successful test, whether it be pictoral or GIF evidence, or CSVs/Python Notebooks of the resultant processed data. The latter set of evidence would make it much easier for your peers to help you. 


### `csvOutput` block

This is the first block that you will be implementing. In many situations, it will be useful to save the output of your pipeline into a CSV, which you can then read using Python or Jupyter Notebook to compare how your processing blocks compare against functions implemented in public libraries such as `mne`, `scipy`, and `numpy`. 

**Write a block `csvOutput` that takes incoming data and saves it into a single CSV. Make this agnostic of how many input channels there are, and how many inputs there are ** (if there are more than one block outputs that you want to save into the the CSV, your block should be able to handle it). You also may want to record your data for a very long time, and holding this data in a store in Python for very long time will be very memory intensive: **ensure that your block is adding data to the CSV continuously/in chunks over time, and not just all at once at the end.**




## Phase 3: Data processing and MNE
To be Released! (I will write this up soon)


## Phase 4: Display
To be Released! (I will write this up soon)

## Phase 5: Machine Learning
To be Released!


## Phase 6: Integration and Experimentation
To be Released! (I will write this up soon)


## Contributers
- Anurag Rao
- Reuben Thomas
