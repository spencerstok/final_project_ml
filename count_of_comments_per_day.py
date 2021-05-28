import pandas as pd
import glob
import os

file_list = glob.glob("stock_dfs/*.csv")
##print(file_list)

for file in file_list:
    csv_name = os.path.basename(file)
    #Uses filtered stock data
    comment_data = pd.read_csv(file)
    comment_data['polarity'] = comment_data['polarity'].astype(float)
    comment_data['subjectivity'] = comment_data['subjectivity'].astype(float)
    #Stock Data
    stock_data = pd.read_csv(f"stock_cleaned/{csv_name}")
    stock_data['Volume'] = stock_data['Volume'].str.replace(',','')
    stock_data['Volume'] = stock_data['Volume'].astype(int)
    stock_data['Close'] = stock_data['Close'].astype(float)
    
    stock_data["volume_change"] = ''
    stock_data["stock_change"] = ''
    stock_data['comment_volume'] = ''
    stock_data['polarity_avg'] = ''
    stock_data['subjectivity_avg'] = ''
    
    for x in range(len(stock_data)):
        date = stock_data["Date"].iat[x]
        temp_comment = comment_data[comment_data["date"] == date]

        stock_data['comment_volume'].iat[x] = len(temp_comment)

        pol_filt = temp_comment[temp_comment["polarity"] != float(0)]
        stock_data['polarity_avg'].iat[x] = pol_filt["polarity"].mean()
        sub_filt = temp_comment[temp_comment["subjectivity"] != float(0)]
        stock_data['subjectivity_avg'].iat[x] = sub_filt["subjectivity"].mean()

        stock_data['volume_change'].iat[x] = (stock_data['Volume'].iat[x] - stock_data['Volume'].iat[x-1])/stock_data['Volume'].iat[x-1]
        stock_data['stock_change'].iat[x] = (stock_data['Close'].iat[x] - stock_data['Close'].iat[x-1])/stock_data['Close'].iat[x-1]

    stock_data= stock_data.fillna(0)
    stock_data.to_csv(f"stock_comment_count//{csv_name}")
                      

        

                
    
    
    
