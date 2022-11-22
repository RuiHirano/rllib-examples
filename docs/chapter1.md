# Chapter1 - チュートリアル

## 1. 環境を構築する

以下のコマンドでレポジトリを cloneしてください。
```
git clone https://github.com/RuiHirano/rllib-examples.git
cd rllib-examples
```

### 1-1. 環境変数の設定
以下のコマンドで.envファイルを作成します。
```
cp .env.templete .env
```

.envファイル内の環境変数は以下のようになっています。
RAY_RESULTS_DIRは学習結果が格納されるディレクトリを、TENSORBOARD_PORTはtensorboardの立ち上がるポートを示しています。
```
RAY_RESULTS_DIR=$PWD/ray_results
TENSORBOARD_PORT=6006
```

### 1-2. docker build
次に以下のコマンドで必要なdockerイメージをビルドします。
```
./build
```

以上で環境構築は終了です。

## 2. サンプルコードの実行

### 2.1 DQNでCartpoleを学習する
./runの後にrllib内のコマンドを付与することでdockerの中で実行してくれます。
```
./run rllib train -f config/cartpole-dqn.yaml
```

### 2.2 Tensorboardで学習状況を確認する
tbコマンドでtensorboardを立ち上げます。
デフォルトであればlocalhost:6006で学習状況が確認できます。
```
./tb
```

### 2.3 学習結果を評価する
学習結果は.envで定義したRAY_RESULTS_DIR内に作成されます。(デフォルトでは$PWD/ray_resultsです。)
ray_results/ch1-cartpole-dqn/DQN_CartPole-v1_xxxxx_ymd/内にcheckpoint_0000xx/というフォルダが存在するか確認してください。

rllibのrolloutコマンドでcheckpointフォルダを指定し実行します。
```
./run rllib rollout $PWD/ray_results/xxx/checkpoint_0000xx --run DQN --env CartPole-v1 --steps 10000
```
実行結果は以下のようになります。
```
Episode #1: reward: 500.0
Episode #2: reward: 500.0
Episode #3: reward: 500.0
Episode #4: reward: 500.0
Episode #5: reward: 500.0
Episode #6: reward: 500.0
Episode #7: reward: 500.0
Episode #8: reward: 500.0
Episode #9: reward: 500.0
Episode #10: reward: 500.0
Episode #11: reward: 500.0
Episode #12: reward: 500.0
Episode #13: reward: 500.0
Episode #14: reward: 500.0
Episode #15: reward: 500.0
Episode #16: reward: 500.0
Episode #17: reward: 500.0
Episode #18: reward: 500.0
Episode #19: reward: 500.0
Episode #20: reward: 500.0
```

以上でchapter1は終了です。