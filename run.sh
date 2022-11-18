source ./.env
echo LOG_DIR:  $LOG_DIR
docker run --rm -it -v $LOG_DIR:/root/ray_results rllib-examples:latest $@