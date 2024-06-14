from aiofiles import open


async def read_file(filename):
    async with open(file=filename, mode="r") as f:
        return await f.read()


async def save_file(filename, content):
    async with open(file=filename, mode="a") as f:
        await f.writelines(content+'\n')
