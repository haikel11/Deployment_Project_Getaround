docker run -it\
 -p 4000:4000\
 -v "$(pwd):/home/app"\
 -e APP_URI="APP_URI"\
 -e PORT=4000\
 -e AWS_ACCESS_KEY_ID="AWS_ACCESS_KEY_ID"\
 -e AWS_SECRET_ACCESS_KEY="AWS_SECRET_ACCESS_KEY"\
 mlflow #python train.py