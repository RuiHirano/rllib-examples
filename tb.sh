source ./.env
echo LOG_DIR:  $LOG_DIR
tensorboard --logdir=$LOG_DIR --bind_all