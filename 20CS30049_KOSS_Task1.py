#This implementation of task 1 will download pages corresponding to elements in arr as parameters and return the status of 
# execution after each download.

import asyncio
import aiohttp
import time             #include necessary packages

async def return_page(el:int):        #function to download a page corresponding to element in arr passed as parameters

    url="https://reqres.in/api/users?page"+str(el)                   #store the string entered in the form of a dictionary of parameters

    async with aiohttp.ClientSession() as session:          #start a session
        async with session.get(url) as resp:   #collect response to the sent GET request
            
            print("Status:",resp.status)
            print("Content-type:",resp.headers['content-type'])
            print(str(resp.url))
            html=await resp.text()                                  #print the parameters showing status of execution
            print("Body:", html[:15], "...")
            

async def main():       #main function to asynchronously call return_page function multiple times
    
    arr=[1,2,3]
    start = time.time()

    await asyncio.gather(*(return_page(i) for i in arr))         #call the coroutines asynchronously

    time_taken = time.time() - start
    print('Time Taken {0}'.format(time_taken))      #Find total time for implementation

asyncio.run(main())         #generate event loop and run main() function

#end of program