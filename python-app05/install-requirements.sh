export LD_LIBRARY_PATH=/opt/rh/rh-python34/root/usr/lib64:/opt/rh/rh-nodejs6/root/usr/lib64:/opt/rh/httpd24/root/usr/lib64
cd /opt/app-root/src/confluent-kafka-python
python setup.py build
python setup.py install

cd /opt/app-root/src/kafkacat
./configure
make
make install