# LOPInfer: A High-Performance Local-Operator Parallel Inference System for Service Workloads in Mobile Edge Computing


LOPInfer is a local-operator parallel inference system for MEC service workloads that enables fine-grained overlap of computation and transmission within a single inference. 
LOPInfer exploits local operators (i.e., operators whose computation can proceed on partial inputs rather than the entire input tensor), decomposes their computation (operation) into independent sub-operations.
By pipelining intra-layer and cross-layer sub-operations, LOPInfer reduces idle time, hides transmission delay, and thereby shortens end-to-end inference latency and lowers device energy consumption without altering the DNN’s semantics. 


We put LOPInfer to the test on our real-world robot, evaluating its performance in two typical real-world robotic applications: [KAPAO](https://github.com/wmcnally/kapao) and [AGRNav](https://github.com/jmwang0117/AGRNav) (as shown in `kapao-demo.mp4` and `agrnav-demo.mp4`). Additionally, we assessed LOPInfer's effectiveness on several models implemented in Torchvision (you can find these in `./ros_ws/src/torchvision/scripts/run_torchvision.py`).

To make it easier for you to explore and understand our work, we've organized our codebase as follows:
- The source code for LOPInfer is located in the `LOPInfer` folder.
- The scripts we used in our experiments can be found in the `exp_utils` folder.
- The relevant code for our workloads is placed in the `ros_ws` folder and two submodules of `KAPAO` and `AGRNav` in `third_parties`.
- We've also included some examples of our experiment logs in the `log` folder, giving you a glimpse into our experiment process.

We hope this structure helps you navigate our project more efficiently. If you have any questions or need further clarification on any aspect of our work, please don't hesitate to reach out. We're always excited to discuss our research and hear your thoughts and feedback!


## Installation
1. Clone this repo and enter the project folder.

2. Building and initiating the corresponding docker containers on both the server and robot sides based on the dockerfile file we provided (`Dockerfile.robot`, `Dockerfile.ros_robot` and `Dockerfile.server`), or execute the script we provided directly.

```
bash run_docker.sh
```
Note that `Dockerfile.ros_robot` is a special version of dockerfile for our robot hardware, as KAPAO and AGRNav needs to control the movement of the robot via ROS.

3. Install the dependency packages and LOPInfer in the docker containers on both the server and robot sides:
```
pip install -r requirement.txt
python setup.py install
```


## How to Use?
1. Integrate LOPInfer into your existing applications, requiring only three lines of code. 
For instance, applying LOPInfer to a VGG19 model is shown as follows, where ``192.168.50.1'' is the IP address of the GPU server.

```python
# Import package of LOPInfer
import LOPInfer
# Define a VGG19 model as usual
vgg19 = VGG19().to(device)
# Apply LOPInfer
LOPInf = LOPInfer(ip = "192.168.50.1")
LOPInf.start_client(model = vgg19)
# Run model for inference as usual
result = vgg19(input)
```
The corresponding modifications to our workload's source code, which are conveniently provided in the `ros_ws` folder.

2. To get started, simply run the following script on your GPU server to launch the LOPInfer server:
```
python exp_utils/start_server.py #on GPU server
```

It's essential to ensure that the LOPInfer client and server can communicate seamlessly, so please double-check the parameters on the GPU server side before running your application.

3. Once the LOPInfer server is up and running, you can start model inference on your mobile devices as usual via the LOPInfer client.

```
python ./ros_ws/src/torchvision/scripts/run_torchvision.py #on robot
```

Alternatively, we've provided a collection of scripts in the `exp_utils` folder specifically designed to streamline the execution of our workloads. Feel free to explore and utilize these scripts to simplify your experimentation process.


## Cite Us
Upcoming, the paper is under review.
