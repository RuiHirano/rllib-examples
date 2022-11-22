# Chapter3 -  カスタマイズされたEnvを利用する

## 1. Super Mario Envの作成
以下のコマンドでsuper-marioを実行し動作を確認します。
```
./run python env/super-mario-env.py
```
以下のような出力であれば問題ないです。
```
step: 4996, reward: 0.0, done: False, info: {'coins': 0, 'flag_get': False, 'life': 2, 'score': 0, 'stage': 1, 'status': 'small', 'time': 151, 'world': 1, 'x_pos': 594, 'y_pos': 89}
step: 4997, reward: 0.0, done: False, info: {'coins': 0, 'flag_get': False, 'life': 2, 'score': 0, 'stage': 1, 'status': 'small', 'time': 151, 'world': 1, 'x_pos': 594, 'y_pos': 93}
step: 4998, reward: -1.0, done: False, info: {'coins': 0, 'flag_get': False, 'life': 2, 'score': 0, 'stage': 1, 'status': 'small', 'time': 150, 'world': 1, 'x_pos': 594, 'y_pos': 97}
step: 4999, reward: 0.0, done: False, info: {'coins': 0, 'flag_get': False, 'life': 2, 'score': 0, 'stage': 1, 'status': 'small', 'time': 150, 'world': 1, 'x_pos': 594, 'y_pos': 100}
...
```