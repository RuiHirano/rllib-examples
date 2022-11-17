FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-devel

RUN apt update && apt install -y \
    git vim

COPY . /root/rllib-examples

WORKDIR /root/rllib-examples
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /root
RUN git clone https://github.com/ray-project/rl-experiments.git

CMD ["bash"]