# from bokeh.sampledata.autompg import autompg_clean as df
import pandas as pd
import hvplot.pandas
import panel as pn
import datetime as dt
import numpy as np

# pn.extension('tabulator', sizing_mode='stretch_width')

df = pd.read_csv('C:/Users/emmal/Desktop/turnout_reg_pers_mob_voters_with_reg_increase_by_precinct_all_int.csv')

# def exp_plot(county_city, turnout_20):
#     return (
#         df[(df.County_City == county_city) & (df.Perc_Turnout_2020 == turnout_20)]
#         .sort_values(by="Perc_of_Registered_Voters")
#         .hvplot(x="Perc_of_Registered_Voters", y="Ratio_Pers_Total")
#     )

# def exp_plot(turnout_20):
#     return (
#         df[(df.Perc_Turnout_2020 == turnout_20)]
#         .sort_values(by="Perc_of_Registered_Voters")
#         .hvplot(x="Perc_of_Registered_Voters", y="Ratio_Pers_Total")
#     )

def exp_plot(county_city, yaxis):
    return (
        df[(df.County_City == county_city)]
        .sort_values(by="Perc_of_Registered_Voters")
        .hvplot(x="Perc_of_Registered_Voters", y=yaxis)
    )




counties_cities = ["Dodge County", "Olmsted County (non-Rochester)", "Rochester (Olmsted County)"]
county_city = pn.widgets.Select(options=counties_cities, name="County / City")
yaxis = pn.widgets.RadioButtonGroup(
    name = 'Y axis',
    options = ['Ratio_Pers_Total', 'Perc_Turnout_2020', 'Perc_of_Voters_in_District _2020', 'Perc_Registration_Increase_2020_2022'],
    button_type = 'success'
)
# turnout_20 = pn.widgets.IntSlider(name="Perc_Turnout_2020", start=82, end=95, step=1)
# data_table = pn.widgets.DataFrame(df)
template = pn.template.BootstrapTemplate(title="Pathway to Victory - Precinct Comparison by County / City", header_background='#528AAE', accent_base_color='#528AAE')

template.sidebar.append(county_city)
template.sidebar.append(yaxis)

# template.sidebar.append(turnout_20)
# template.main.append(pn.bind(exp_plot, county_city, yaxis, data_table))
template.main.append(pn.bind(exp_plot, county_city, yaxis))
template.servable()