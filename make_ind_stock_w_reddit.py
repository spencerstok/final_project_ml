import pandas as pd

df = pd.read_csv("reddit_classified_split.csv")

def split_datetime():

    df['date'] = ''
    df['time'] = ''    

    for x in range(len(df)):
        split_timestamp = str(df['timestamp'].iat[x]).split(" ")
        df['date'].iat[x] = split_timestamp[0]
        df['time'].iat[x] = split_timestamp[1]
        

    df.to_csv("reddit_classified_split.csv", index = False)      

##split_datetime()  

stock_list = ["KODK", "AMC", "GME", "BB", "AAPL"]
##company_list = ["kodak", "theatres", "gamestop", "blackberry", "aaple"]

for ticker in stock_list:
##    company = company_list[ticker]
##    print(company)
    #Filter for ticker in comment
    stock_df = df[df['body'].str.contains(str(ticker), case=False, na=False)]

    #Filter for company in comment
##    company_df = df[df['body'].str.contains(str(company), case=False)]

    #Recombind
        
    #Drop Duplicates (on comment ID
##    df.drop

    # Get count of comments for each day


    #Volume of comments


##Filter by mention ticker or company
##
##
##Avg Polarity of that day
##
##Avg subjectivity of that day


    stock_df.to_csv("stock_dfs/"+ticker+".csv")
    
