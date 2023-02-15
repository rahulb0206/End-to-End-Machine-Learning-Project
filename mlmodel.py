import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pickle
import os
class marks():
    def __init__(self,df=None):
        self.df=df

    def sat_gpa (self,file_path):
        self.df =pd.read_csv(file_path)
        os.remove(file_path)

    def y_value(self,Y):
        df=self.df
        if Y=='SAT':
            Y=df.SAT
            X=df.GPA
            X =df.iloc[:, 1:2]
            
        elif Y=='GPA':
            X=df.SAT
            Y=df.GPA
            X= df.iloc[:, :1]

        x_train, x_test, y_train, y_test = train_test_split(X.values, Y, random_state=1)
        regressor = LinearRegression()
        regressor.fit(x_train, y_train)
        pred_y=regressor.predict(x_test)
        pred_yy=regressor.predict(x_train)
        mean_absolute_error(y_test,pred_y)
        mean_absolute_error(y_train,pred_yy)
        print(mean_absolute_error(y_train,pred_yy))
        print(mean_absolute_error(y_test,pred_y))
        pickle.dump(regressor, open('model.pkl','wb')) 

