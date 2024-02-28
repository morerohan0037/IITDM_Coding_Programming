import pandas as pa
import plotly.express as px
import plotly.graph_objects as go

data = pa.read_csv("/home/iiitdmk-sic23/Downloads/IPL_2022.csv")
print(data.head())

figure_1 = px.bar(data,
                x = data["match_winner"],
                title = "Match winners"
                )
figure_1.show()

data["won_by"] = data["won_by"].map({"Wickets" : "Chasing", "Runs": "Defending"})
won_by = data["won_by"].value_counts()
label = won_by.index
counts = won_by.values
colors = ["orange", "purple"]

figure_2 = go.Figure(data = [go.Pie(labels=label, values = counts)])
figure_2.update_layout(title = "No. of Matches won by chasing or defending")
figure_2.update_traces(hoverinfo= 'label + percent', textinfo = 'value', marker = dict(colors = colors,line = dict(color = 'black', width = 2)))
figure_2.show()

toss_decision = data["toss_decision"].value_counts()
label_toss_decision = toss_decision.index
counts_toss_decision = toss_decision.values
colors_toss_decision = ["green", "blue"]

figure_3 = go.Figure(data = [go.Pie(labels=label_toss_decision, values = counts_toss_decision)])
figure_3.update_layout(title = "Toss Decision")
figure_3.update_traces(hoverinfo= 'label + percent', textinfo = 'value', marker = dict(colors = colors,line = dict(color = 'black', width = 2)))
figure_3.show()

figure_4 = px.bar (
                    data,
                    x = data["top_scorer"],
                    y = data["highscore"],
                    title = "Top Scorer in IPL 2022"

)
figure_4.show()

figure_5 = px.bar(
                    data,
                    x = data["player_of_the_match"],
                    title = "Most player of the match"

)
figure_5.show()

figure_6 = px.bar(
                    data,
                    x = data["best_bowling"],
                    title = "Best bowling of the match"

)
figure_6.show()

figure_7 = go.Figure()
figure_7.add_trace(go.Bar(
    x = data["venue"],
    y = data["first_ings_wkts"],
    name = "First Inning Wickets",
    marker_color = "Green"
))

figure_7.add_trace(go.Bar(
    x= data["venue"],
    y = data["second_ings_wkts"],
    name = "Second Innings Wickets",
    marker_color = "Orange"
))

figure_7.update_layout(barmode = 'group', xaxis_tickangle = -45)
figure_7.show()

figure_8 = go.Figure()
figure_8.add_trace(go.Bar(
    x = data["venue"],
    y = data["first_ings_score"],
    name = "First Innings Score",
    marker_color = "Bisque"
))

figure_7.add_trace(go.Bar(
    x= data["venue"],
    y = data["second_ings_score"],
    name = "Second Innings Score",
    marker_color = "Aqua"
))

figure_8.update_layout(barmode = 'group', xaxis_tickangle = -45)
figure_8.show()

