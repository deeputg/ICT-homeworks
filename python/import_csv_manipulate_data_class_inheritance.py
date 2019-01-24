import pandas as pd

class ImportCsv:
	df= pd.read_csv("MOCK_DATA.csv")
	maleUsers = []
	femaleUsers = []
	for index, row in df.iterrows():
		if(row['gender']=="Male"):
			tempUserInnerList = [row['id'],row['first_name']]
			maleUsers.append(tempUserInnerList)
		else:
			tempUserInnerList = [row['id'],row['first_name']]
			femaleUsers.append(tempUserInnerList)
class GrandScolarship(ImportCsv):
	sholarshipEligible = []


myObj = GrandScolarship()
print(myObj.femaleUsers)