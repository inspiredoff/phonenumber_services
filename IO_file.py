from aiofiles import open


async def read_file(filename):
    async with open(file=filename, mode="r") as f:
        return await f.read()


async def save_file(filename: str, content: object) -> object:
    async with open(file=filename, mode="a") as f:
        await f.write(content+'\n')
