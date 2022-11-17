FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-devel

COPY . /root/rllib-examples

WORKDIR /root/rllib-examples
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]