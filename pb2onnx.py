import tensorflow as tf
import os
import cv2
# tf.python.gfile.GFile
model_name='detection/model.pb'
f=tf.python.gfile.FastGFile(model_name,'rb')#['image'] ['output/boxes', 'output/scores', 'output/labels']
# a=tf.compat.v1.GraphDef()
graph_def=tf.GraphDef()
print(graph_def)
graph_def.ParseFromString(f.read())
return_elements=['image:0', 'output/boxes:0', 'output/scores:0', 'output/labels:0']
return_tensors=tf.import_graph_def(graph_def,return_elements=return_elements)#
g=tf.get_default_graph()
sess=tf.Session(graph=g)
img=cv2.imread('E:/fjj/SeaShips_SMD/JPEGImages/MVI_1592_VIS_00169.jpg')
orig_shape = img.shape[:2]

resized_img = cv2.resize(img,(1067,600))#(H,W,C)
output=sess.run([return_tensors[1],return_tensors[2],return_tensors[3]],feed_dict={return_tensors[0]:resized_img})

# python -m tf2onnx.convert --input model.pb --inputs image:0[600,1067,3] --inputs-as-nchw image:0 --outputs output/boxes:0,output/scores:0,output/labels:0 --output ./model.onnx --verbose --opset 12



