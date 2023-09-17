## Build the image torchserve locally before running this: archiver and start model
## https://github.com/pytorch/serve/tree/master/docker
FROM projects.registry.vmware.com/models/tool/pytorch/torchserve:0.5.1-cpu
USER root
RUN apt-get update \
    && apt-get install -y libgl1-mesa-glx libglib2.0-0 python3-distutils \
    && apt-get install -y curl

COPY ./resources/ /home/model-server/resources/
RUN chmod -R a+rw /home/model-server/
USER model-server

RUN pip3 install --upgrade pip \
    && pip install torch-model-archiver -i https://pypi.douban.com/simple/ \
    && pip install opencv-python -i https://pypi.douban.com/simple/

RUN pip install -r /home/model-server/resources/helmet_yolov5/requirements.txt -i https://pypi.douban.com/simple/
EXPOSE 8080 8081

RUN torch-model-archiver --model-name helmet_detection \
--version 0.1 --serialized-file /home/model-server/resources/helmet.torchscript.pt \
--handler /home/model-server/resources/torchserve_handler.py \
--export-path /home/model-server/model-store/ \
--extra-files /home/model-server/resources/index_to_name.json,/home/model-server/resources/torchserve_handler.py

CMD [ "torchserve", "--start", "--model-store", "/home/model-server/model-store/", "--models", "./helmet_detection.mar", "--ts-config",  "/home/model-server/config.properties"]