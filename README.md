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
./run rllib train -f config/cartpole-dqn.yaml
```

### Restore and Train

./config/cartpole-dqn.yaml
```
cartpole-dqn:
    env: CartPole-v1
    run: DQN
    restore: xxx/xxx/checkpoint  <- Add restore option
    stop:
        episode_reward_mean: 100
        timesteps_total: 100000
    ...
```

```
./run rllib train -f config/cartpole-dqn.yaml
```

### Evaluating

```
./run rllib rollout /path/to/ray_results/xxx/checkpoint --run DQN --env CartPole-v1 --steps 10000
```

if you run source command, you can use $RAY_RESULTS_DIR variable.
```
source ./.env
./run rllib rollout $RAY_RESULTS_DIR/xxx/checkpoint --run DQN --env CartPole-v1 --steps 10000
```

### Using Tensorboard
```
./tb
```

view at http://localhost:6006