import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
import plotly
import plotly.express as px

data=pd.read_csv("/Users/Tanishq/Desktop/Datascience/lesson14/planet_dataset.csv")

top_7=pd.DataFrame(data.groupby("Planet")["Size_km"].mean().nlargest(7).sort_values(ascending=False))

fig1=px.scatter(top_7,x=top_7.index,y="Size_km",size="Size_km",size_max=230,color=top_7.index,title="Top 7 planets by size in km")
fig1.write_html("fig1.html",auto_open=True)

top_7a=pd.DataFrame(data.groupby("Planet")["Habitability_second"].mean().nlargest(7).sort_values(ascending=False))

fig2=px.scatter(top_7a,x=top_7a.index,y="Habitability_second",size="Habitability_second",size_max=230,color=top_7a.index,title="Top 7 planets by how many seconds you can survive on them")
fig2.write_html("fig2.html",auto_open=True)

top_7b=pd.DataFrame(data.groupby("Planet")["Age_billion_years"].mean().nlargest(7).sort_values(ascending=False))

fig3=px.scatter(top_7b,x=top_7b.index,y="Age_billion_years",size="Age_billion_years",size_max=230,color=top_7b.index,title="Top 7 planets by age")
fig3.write_html("fig3.html",auto_open=True)

top_7c=pd.DataFrame(data.groupby("Planet")["Moons"].mean().nlargest(7).sort_values(ascending=False))

fig4=px.scatter(top_7c,x=top_7c.index,y="Moons",size="Moons",size_max=230,color=top_7c.index,title="Top 7 planets by amount of moons")
fig4.write_html("fig4.html",auto_open=True)