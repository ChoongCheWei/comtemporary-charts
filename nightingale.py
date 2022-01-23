import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts
from matplotlib import pyplot as plt

df = pd.read_csv("age 35-44.csv")
print(df)

age = df['Category'].values.tolist()
visit = df['Frequency'].values.tolist()

color_series = ['#C9DA36', '#9ECB3C',
                '#14ADCF', '#2B55A1', '#6A368B', '#6A368B']

rosechart = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))

rosechart.set_colors(color_series)

rosechart.add("", [list(z) for z in zip(age, visit)], radius=[
              "15%", "70%"], center=["30%", "60%"],  rosetype="area")

rosechart.set_global_opts(title_opts=opts.TitleOpts(title='Nightingale Rose Chart', subtitle="Age 25-34"),
                          legend_opts=opts.LegendOpts(is_show=False), toolbox_opts=opts.ToolboxOpts())

rosechart.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", font_size=12,
                          formatter="{b}:{c}%", font_style="italic", font_weight="bold", font_family="Century"),)

rosechart.render('nightingale rose.html')
# rosechart.render_notebook()
