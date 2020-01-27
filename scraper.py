import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen


def Get_Web_Page(address):
	sts = urlopen(address).getcode()
	print("status is: %d" % (sts))
	html = urlopen(address)
	page = html.read()
	return(page)

df = pd.DataFrame(columns = ['c_name', 'c_date', 'c_review', 'c_link', 'c_score'])

a = Get_Web_Page("https://www.rottentomatoes.com/m/goldeneye/reviews")

# Parse a

soup = BeautifulSoup(a, 'html.parser')

c_name = []
c_date = []
c_review = []
c_score = []
c_link = []

# find tables
tables = soup.find_all("div", class_="row review_table_row")
for table in tables:
	for name in table.find_all("a", class_="unstyled bold articleLink"):
		c_name.append(name.get_text())
	for date in table.find_all("div", class_="review-date subtle small"):
		c_date.append(date.get_text())
	for review in table.find_all("div", class_="the_review"):
		c_review.append(review.get_text().strip())
	for link in table.find_all("div", class_="small subtle review-link"):
		if not link.get_text():
			c_score.append("") 
		else:
			c_score.append(link.get_text().strip())
		if "Full Review" not in link.get_text():
			c_link.append("")
		else:
			for i in link.find_all('a'):
				c_link.append(i.get('href').strip())
print (len(c_name)) 
print (len(c_date)) 
print (len(c_review)) 
print (len(c_score)) 
print (len(c_link)) 

df = pd.DataFrame(
	{'Critic_Name': c_name,
	'Review_Date': c_date,
	'Review': c_review,
	'Score': c_score,
	'Review_Link': c_link})
print(df)

#print(df['Review_Link'])

df = df[df.Score.apply(lambda x: x.isnumeric())]
print(df['Score'])





#print(table)

# to find name of critics 

#names = soup.find_all("a", class_ = "unstyled bold articleLink")

#names_list = []
#for name in names:
#	names_list.append(name.get_text())

# to find the second page of this rotten tomatoes critic reviews
#reviews_link_list = []
#reviews_link = soup.find_all("div", class_= "small subtle review-link")
#for i in reviews_link:
#	for links in (i.find_all('a')):
#		reviews_link_list.append(links.get('href'))
 
 #store links in array to compare if same or not
#reviews_link_list = []
#for link in reviews_link:
#	reviews_link_list.append(link.get('href')) # stores path as q so we can compare if there is more

# Page 2 is /m/goldeneye/reviews?type=&sort=&page=2
# concatonate this with base url? https://www.rottentomatoes.com/m/goldeneye/reviews?type=&sort=&page=2
# need to store this new loink as a variable 
# if there are two link reutrn when running this for loop then compare both to previous

# first page and last page of reivews will have only one link, any pages in between weill have 2 links, limit = 2 (to test)





