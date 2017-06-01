#生成json语法的图表

import vincent as vi

y = [1,2,3,4,5,6,7]
bar = vi.Bar(y)
bar.axis_titles(x='Index', y='Value')
bar.to_json('C:\\Users\\ZhangSSD\\Desktop\\新建文件夹\\vega.json')
