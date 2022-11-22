# RLLib Examples


## Getting Started

### Modify .env
```
cp .env.templete .env
```

Edit .env
```
RAY_RESULTS_DIR=$PWD/ray_results
TENSORBOARD_PORT=6006
```

### Build
```
./build
```

### Train
```
./run rllib train -f config/cartpole-dqn.yaml --checkpoint-freq 1000
```

### Restore and Train
```
./run rllib train -f config/cartpole-dqn.yaml --checkpoint-freq 1000 --restore [checkpoint_path]
```

### Evaluating

```
./run rllib rollout ~/ray_results/default/DQN_CartPole-v0_0upjmdgr0/checkpoint_1/checkpoint-1 --run DQN --env CartPole-v0 --steps 10000
```

### Using Tensorboard
```
./tb
```

view at http://localhost:6006