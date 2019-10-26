# wget http://download.tensorflow.org/models/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
# tar -xzvf ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz



export PYTHONPATH=$PYTHONPATH:/home/pi/git/tensorflow/models/research/object_detection:/home/pi/tensorflow1/models/research/slim
cd /home/pi/git/TensorFlow-Object-Detection-on-the-Raspberry-Pi
python3 Pet_detector.py



# cd /home/pi/tensorflow1/models/research/object_detection
# wget https://raw.githubusercontent.com/jlanej/TensorFlow-Object-Detection-on-the-Raspberry-Pi/master/Pet_detector.py
#  python3 Pet_detector.py.1