import pydotplus
from IPython.display import Image
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

file = "C:\\Users\\ZhangSSD\\Desktop\\新建文件夹\\tree.dot"
graph = pydotplus.graph_from_dot_file(file)
graph.write_pdf("C:\\Users\\ZhangSSD\\Desktop\\新建文件夹\\iris.pdf")
graph.write_png("C:\\Users\\ZhangSSD\\Desktop\\新建文件夹\\iris.png")
Image(graph.create_png())
