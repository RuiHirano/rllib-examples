# RLLib Examples


## Getting Started

### Modify .env
```
cp .env.templete .env
```

```
LOG_DIR=$PWD/ray_results
```

### Build
```
./build.sh
```

### Train
```
./run.sh rllib train -f config/cartpole-dqn.yaml --checkpoint-freq=1000
```

### Restore and Train
```
./run.sh rllib train -f config/cartpole-dqn.yaml --checkpoint-freq=1000 --restore=[checkpoint_path]
```

### Evaluating

```
./run.sh rllib rollout ~/ray_results/default/DQN_CartPole-v0_0upjmdgr0/checkpoint_1/checkpoint-1 --run DQN --env CartPole-v0 --steps 10000
```

### Using Tensorboard
```
./tb.sh
```

view at http://localhost:6006