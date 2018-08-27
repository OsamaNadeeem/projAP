import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
data = pd.read_csv('tendulkarsp.csv').query("Runs !='DNB'")

class Algorithm:


    def linear_regression(self):
        y=[]
        num=0
        for i in data.Runs :
            num=num+1
            y.append(num)
        data['Runs'] = pd.to_numeric(data['Runs'])
        from scipy.stats import linregress
        data1 = linregress(y,data.Runs)
        print('Results According to Linear Regression are: ')
        print(data1.intercept+(data1.slope*(len(data.Runs)+1)))


    def Naive_Bays(self):
            print("In")
            fifties=[]
            for i in data.Runs:
                if (i>49):
                    fifties.append(1)
                else:
                    fifties.append(0)
            df = data
            df.drop(['Innings', 'Runs', 'Mins','BF','4s','6s','SR','Pos','Dismissal','Start Date','ha','result'], 1, inplace=True)
            seen_oppositions = set()
            all_oppositions = []
            for x in df.Opposition:
                if x not in seen_oppositions:
                    all_oppositions.append(x)
                    seen_oppositions.add(x)

            seen_venue = set()
            all_venue = []
            for x in df.Ground:
                if x not in seen_venue:
                    all_venue.append(x)
                    seen_venue.add(x)
                
            xyz="DNB"
            average=[]
            for x in all_venue:
                data2 = pd.read_csv('tendulkarsp.csv').query("Runs !=@xyz and Ground==@x")
                average.append((sum(data2.Runs))/len(data2.Runs))
            #print(average)
            new_df=list(zip(all_venue,average))
            new_df = sorted(new_df, key=lambda x: x[1])
            #new_df=zip(*new_df)
            #print(new_df)
            my_array=[]
            for a,b in new_df:
                my_array.append(a)
                    
            #print(my_array)
            all_venue=my_array

            opps_num = []
            venue_num = []
            k=-1
            for i in all_oppositions:
                k=k+1
                opps_num.append(k)

            k=-1

            for i in all_venue:
                k=k+1
                venue_num.append(k)
            k=0
            l=0

            temp=0
##            while(temp<len(all_oppositions)):
##                print(opps_num[temp]," : ",all_oppositions[temp])
##                temp=temp+1
##            temp=0
##            while(temp<len(all_venue)):
##                print(venue_num[temp]," : ",all_venue[temp])
##                temp=temp+1

            
            for i in df.Opposition:
                l=0
                for j in all_oppositions:        
                    if(i==j):            
                        df.loc[k, 'Opposition'] = opps_num[l]
                    l=l+1
                k=k+1

            k=0
            for i in df.Ground:
                l=0
                for j in all_venue:        
                    if(i==j):            
                        df.loc[k, 'Ground'] = venue_num[l]
                    l=l+1
                k=k+1
            Inn=0
            GR=0
            Opp=0
            from sklearn.naive_bayes import GaussianNB
            clf = GaussianNB()
            clf.fit(df, fifties)
            i=0

            print(clf.predict([[1,6,8]]))




    def decision_tree(self):
        print("In Decesion Tree")
        fifties=[]
        for i in data.Runs:
            if (i>49):
                fifties.append(1)
            else:
                fifties.append(0)
        df = data
        df.drop(['Innings', 'Runs', 'Mins','BF','4s','6s','SR','Pos','Dismissal','Start Date','ha','result'], 1, inplace=True)
        seen_oppositions = set()
        all_oppositions = []
        average=[]
        xyz='DNB'
        
        
        for x in df.Opposition:
            if x not in seen_oppositions:
                all_oppositions.append(x)
                seen_oppositions.add(x)

        seen_venue = set()
        all_venue = []
        for x in df.Ground:
            if x not in seen_venue:
                all_venue.append(x)
                seen_venue.add(x)


        for x in all_venue:
            data2 = pd.read_csv('tendulkarsp.csv').query("Runs !=@xyz and Ground==@x")
            average.append((sum(data2.Runs))/len(data2.Runs))
        new_df=list(zip(all_venue,average))
        new_df = sorted(new_df, key=lambda x: x[1])
        my_array=[]
        for a,b in new_df:
            my_array.append(a)
        all_venue=my_array




        

        opps_num = []
        venue_num = []
        k=-1
        for i in all_oppositions:
            k=k+1
            opps_num.append(k)

        k=-1

        for i in all_venue:
            k=k+1
            venue_num.append(k)
        k=0
        l=0

        temp=0
        while(temp<len(all_oppositions)):
            print(opps_num[temp]," : ",all_oppositions[temp])
            temp=temp+1
        temp=0
        while(temp<len(all_venue)):
            print(venue_num[temp]," : ",all_venue[temp])
            temp=temp+1
        for i in df.Opposition:
            l=0
            for j in all_oppositions:        
                if(i==j):            
                    df.loc[k, 'Opposition'] = opps_num[l]
                l=l+1
            k=k+1

        k=0
        for i in df.Ground:
            l=0
            for j in all_venue:        
                if(i==j):            
                    df.loc[k, 'Ground'] = venue_num[l]
                l=l+1
            k=k+1
        Inn=0
        GR=0
        Opp=0
        #df=df.sort_values(by='Opposition', ascending=0)
        #print(df)
        

        

        #df=df.sort_values(by='Ground', ascending=0)
        #print(df)
        from sklearn import tree
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(df, fifties)
        with open("clf.txt", "w") as f:
                       f = tree.export_graphviz(clf, out_file=f)
        while(1):
            Inn=1
            Opp=input("Opponent : ")
            GR=input("Venue : ")
            print(clf.predict([[Inn,Opp,GR]]))





if __name__ == '__main__':
    algo = Algorithm()
    #algo.Naive_Bays()
    algo.decision_tree();
    
