#This implementation of task 1 will download pages corresponding to strings in name_arr as parameters and return the status of 
# execution after each download.

import asyncio
import aiohttp
import time             #include necessary packages

async def return_page(name:str):        #function to download a page corresponding to string in name_arr passed as parameters

    params={'q':name}                   #store the string entered in the form of a dictionary of parameters

    async with aiohttp.ClientSession() as session:          #start a session
        async with session.get('https://www.google.com/search',params=params) as resp:   #collect response to the sent GET request
            
            print("Status:",resp.status)
            print("Content-type:",resp.headers['content-type'])
            print(str(resp.url))
            html=await resp.text()                                  #print the parameters showing status of execution
            print("Body:", html[:15], "...")
            

async def main():       #main function to asynchronously call return_page function multiple times
    
    name_arr=['Yash','KOSS','Shreyas']
    start = time.time()

    await asyncio.gather(*(return_page(st) for st in name_arr))         #call the coroutines asynchronously

    time_taken = time.time() - start
    print('Time Taken {0}'.format(time_taken))      #Find total time for implementation

asyncio.run(main())         #generate event loop and run main() function

#end of program