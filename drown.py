import random as r
fp=open('drown.csv','w') # Open the file in writing mode
fp.write('heartrate,systolicbp,diastolicbp,spo2,status\n')
for i in range(60000):
    hr=r.randint(60,110)
    sbp=r.randint(75,130)
    dbp=r.randint(55,85)
    spo2=r.randint(85,101)
    # probab of danger %
    status= 0
    flag = 0
    if hr>95 and sbp<95 and dbp<70 and spo2<90 : # 100
        status= 4 
        flag = 1
        
    elif hr>90 and sbp<100 and dbp<72 and spo2<92 : # 75
        status= 3 
        flag = 1
        
    elif hr>85 and sbp<105 and dbp<74 and spo2<94 : # 50
        status= 2
        flag = 1
        
    elif hr>80 and sbp<110 and dbp<76 and spo2<96 : # 25
        status= 1 
        flag = 1
        
    elif hr<81 and sbp>109 and dbp>75 and spo2>95: # 0
        status= 0 # normal healthy
        flag = 1
         
    if flag == 1:
        heart='%d,%d,%d,%d,%d\n'%(hr,sbp,dbp,spo2,status)
        fp.write(heart) # Writing to the file line by line
    flag = 0
fp.close()
print ('Done! \n Open file to view the dataset.')
