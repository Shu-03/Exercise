# 作者：shu qi
# 开发时间：2022/12/13 12:01
from pyecharts import Graph
import os
import json
with open(os.path.join("(ch-6.4.3)weibo.json"),"r",encoding="utf-8") as f:
    j=json.load(f)
    nodes,links,categories,count,mid,user1=j
graph=Graph("微博关系图",width=1200,height=600)
graph.add(
    "",
    nodes,
    links,
    categories,
    label_pos="right",
    graph_repulsion=50,
    is_legend_show=False,
    line_curve=0.2,
    label_text_color=None,
)
graph.render("微博关系图.html")