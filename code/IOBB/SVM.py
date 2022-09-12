import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

np.random.seed(202205456)

data0506 = [
            "../All_Data/new_data/手2022-05-06 114900-4.csv",
            "../All_Data/new_data/手2022-05-06 113600-4.csv",
            "../All_Data/new_data/手2022-05-06 115200-2.csv",
            "../All_Data/new_data/腳2022-05-06 120000-4.csv",
            "../All_Data/new_data/腳2022-05-06 120300-3.csv",
            "../All_Data/new_data/腳2022-05-06 120500-4.csv"]
                                                    
data0510 = [
            "../All_Data/0510data/手2022-05-10 103600.csv",
            "../All_Data/0510data/手2022-05-10 103800.csv",
            "../All_Data/0510data/手2022-05-10 104000.csv",
            "../All_Data/0510data/腳2022-05-10 103600.csv",
            "../All_Data/0510data/腳2022-05-10 103800.csv",
            "../All_Data/0510data/腳2022-05-10 104000.csv"]

def SVM(data):     
    data = np.array(pd.read_csv(data))
    labelSeries = data[:,15]
    dataSeries = data[:,1:10]
    x_train, x_test, y_train, y_test = train_test_split(dataSeries, labelSeries,test_size=0.2, random_state=222)


    svm = SVC(kernel="rbf",gamma = 0.5, probability=True)
    y_train=y_train.astype('str')
    y_test=y_test.astype('str')
    svm.fit(x_train,y_train)

    predict = svm.predict(x_test)
    #predictP = svm.predict_proba(x_test)
    svm_score = svm.score(x_test, y_test) 
    print(classification_report(y_test,predict))
    return svm_score

def DT(data):
    data = np.array(pd.read_csv(data))
    labelSeries= data[:,15]
    dataSeries = data[:,1:10]
    
    # 使用訓練資料訓練模型
    x_train, x_test, y_train, y_test = train_test_split(dataSeries, labelSeries,test_size=0.2, random_state=222)

    decisionTreeModel = DecisionTreeClassifier()
    y_train=y_train.astype('str')
    y_test=y_test.astype('str')
    decisionTreeModel.fit(x_train, y_train)
    # 使用訓練資料預測

    predict= decisionTreeModel.predict(x_test)
    
    DT_score = decisionTreeModel.score(x_test,y_test)
    #print(classification_report(y_test,predict))
    return DT_score

def RF(data,data1):
    data = np.array(pd.read_csv(data))
    labelSeries = data[:,16]
    dataSeries = data[:,1:9]
    #x_train, x_test, y_train, y_test = train_test_split(dataSeries, labelSeries,test_size=0.2, random_state=222)
    data1 = np.array(pd.read_csv(data1))
    labelSeries1 = data1[:,16]
    dataSeries1 = data1[:,1:9]
    #x_train1, x_test1, y_train1, y_test1 = train_test_split(dataSeries1, labelSeries1,test_size=0.2, random_state=222)

    randomForestModel = RandomForestClassifier(random_state=1,n_estimators=60 , max_depth=1 ,min_samples_split=70)
    # 使用訓練資料訓練模型
    #x_train=x_train.astype('int')
    #y_train=y_train.astype('str')
    #x_test=x_test.astype('int')
    #y_test=y_test.astype('str')
    randomForestModel.fit(dataSeries, labelSeries)
    # 使用訓練資料預測
    predict = randomForestModel.predict(dataSeries1)
    RF_score = randomForestModel.score(dataSeries1,labelSeries1)
    print(classification_report(labelSeries1,predict))
    return RF_score

#Support Vector Machine支援向量機
# print("--------Support Vector Machine ---------")
# for i in range(len(data0510)//2):
#     print("Hand:",SVM(data0510[i]))
#     print("")
#     print("Foot:",SVM(data0510[i+2]))
#     print("________________________________________________________")

#print("--------------------------------\nDecision Treeeeeeeeeeeeeeeeeeee\n-------------------------------")
#for i in range(len(data0510)//2):
    #print("Hand:",DT(data0510[i]))
    #print("")
    #print("Foot:",DT(data0510[i+2]))
    #print("________________________________________________________")


print("--------------------------------\nRandomForest\n-------------------------------")
#for i in range(len(data0506)//2):
for i in range(1):
    print("Hand:",RF(data0506[i],data0506[i+1]))
    print("")
    print("Foot:",RF(data0506[i+2],data0506[i+3]))
    print("________________________________________________________")

