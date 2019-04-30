START_TIME=$SECONDS

python /opt/notebooks/pi.py

ELAPSED_TIME=$(($SECONDS - $START_TIME))

echo $ELAPSED_TIME
