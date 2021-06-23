#This is an asynchronous implementation of Task 2 which will download 200 comic book strips using the given template URL
# and store each of them in separate files.
#Since async IO allows concurrent execution,this implementation will be faster.


import aiohttp
import asyncio
import aiofiles
import time		#include the necessary packages


async def downloadComic(session:aiohttp.ClientSession,comic_id:int):     #function to download comic strips

	url="https://xkcd.com/"+str(comic_id)+"/info.0.json"		#store URL for downloading strip as a string
	async with session.get(url) as resp:				#Use the open session to generate GET request
		 							#and collect response
		filename='comicasync'+str(comic_id)+'.txt'
		async with aiofiles.open(filename,"w") as file:		#create a new file for every comic strip and store 
			await file.write(str(await resp.json()))	#the contents in it
		
				
async def main():		#main function used to download all 200 comics by asynchronously calling the
				#downloadComic() function multiple times
	start=time.time()
	async with aiohttp.ClientSession() as session:		#create a session for downloading comics
		await asyncio.gather(*(downloadComic(session,i) for i in range(1,201)))
	time_taken=time.time()-start
	print("Time Taken: {0}".format(time_taken))		#Find total time taken for implementation


asyncio.run(main())		#generate event loop and call main() function

#end of program