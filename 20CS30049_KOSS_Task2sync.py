#This is a synchronous implementation of Task 2 which will download 200 comic book strips using the given template URL
# and store each of them in distinct files. 
#Since synchronous execution involves blocking calls,this implemenation will be slower.

import requests
import time		#include the necessary packages


def downloadComic():		#function to download all the comic strips

	with requests.Session() as session:		#initiate the session
		for i in range(1,201):

			comic_id=i

			url="https://xkcd.com/"+str(comic_id)+"/info.0.json"	#store URL for each comic strip as a string
			with session.get(url) as resp:				#send a GET request and collect the response 

				filename='comicsync'+str(i)+'.txt'
				with open(filename,"w") as file:
					file.write(str(resp.json()))		#create a new file for each strip and store 
										#the contents obtained as response

				
				


def main():		#main function to call the downloadComic() function
	start=time.time()
	downloadComic()
	time_taken=time.time()-start
	print('Time Taken {0}'.format(time_taken))	#Find the total time taken for implementation


main()		#call main() function

#end of program