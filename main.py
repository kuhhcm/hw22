import requests
import asyncio
import aiohttp

# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# with open('post.json', 'w') as file:
#     file.write(response.text)

# async def main():
#     url = ['https://jsonplaceholder.typicode.com/posts/1']
#     async with aiohttp.ClientSession() as session:
#         await with open('dats.json')

# Д/З

# response = requests.get('https://jsonplaceholder.typicode.com/todos')

# with open('todos.json', 'w') as file:
#     file.write(response.text)





# for i in range(1,11):
#     response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{i}')

#     with open(f'post{i}.json', 'w') as file:
#         file.write(response.text)




# async def main():
#     for i in range(100):
#         url = f'https://jsonplaceholder.typicode.com/todos/{i}'
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as response:
#                 with open(f'todo{i}.json','w') as file:
#                     file.write(await response.text())

# asyncio.run(main())







# for i in range(1,101):
#     response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{i}')

#     with open(f'post{i}.json', 'w') as folder:
        