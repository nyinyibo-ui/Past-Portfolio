#import libs

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit  as st
from datetime import datetime

#define functions


def loadData():
    
    """Load the data and do light feature engineering"""
    #load data
    df_agg=pd.read_csv("Project_data/Aggregated_Metrics_By_Video.csv").iloc[1:,:]
    df_agg_sub=pd.read_csv("Project_data/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv")
    df_comment=pd.read_csv("Project_data/All_Comments_Final.csv")
    df_datetime=pd.read_csv("Project_data/Video_Performance_Over_Time.csv")
    #feature engineering
    #fix the columns for proper looking
    df_agg.columns = ['Video','Video title','Video publish time','Comments added','Shares','Dislikes','Likes',
                          'Subscribers lost','Subscribers gained','RPM(USD)','CPM(USD)','Average % viewed','Average view duration',
                          'Views','Watch time (hours)','Subscribers','Your estimated revenue (USD)','Impressions','Impressions ctr(%)']


    #change dtypes
    df_agg["Video publish time"]=pd.to_datetime(df_agg["Video publish time"])
    df_agg["Average view duration"]=df_agg["Average view duration"].apply(lambda x: datetime.strptime(x,"%H:%M:%S"))
    df_agg["Average duration sec"]=df_agg["Average view duration"].apply(lambda x: x.second+x.minute*60+x.hour*360)
    df_datetime["Date"]=pd.to_datetime(df_datetime["Date"])

    #add some necessary features
    df_agg["Engagement_ratio"]=(df_agg["Comments added"]+df_agg["Shares"]+df_agg["Dislikes"]+df_agg["Likes"])/df_agg["Views"]
    df_agg["ViewsPerSubscriber_gained"]=df_agg["Views"]/df_agg["Subscribers gained"]#number of views to gain subsriber


    df_agg.sort_values(by="Video publish time",ascending=False,inplace=True)
    
    return df_agg,df_agg_sub,df_comment,df_datetime




#create dataframes using the function

df_agg,df_agg_sub,df_comment,df_time=loadData()


###################################################
#Start building Streamlit App
###################################################
add_sidebar=st.sidebar.selectbox('Aggregate or Individual Video', ('Aggregate Metrics','Individual Video Analysis'))