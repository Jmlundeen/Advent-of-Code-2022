import re

data = [line.strip() for line in open('./Day7/input.txt').readlines()]
# Tree for file structure
class NonBinTree:
    
    def __init__(self,name,size = 0,parent = None):
        self.parent = parent
        self.name = name
        self.size = size
        self.nodes = []

    def insert(self,name,size=0) -> None:
        self.nodes.append(NonBinTree(name,size,parent=self))

    def updateSize(self,val):
        node: NonBinTree
        self.size += val
        node = self.parent
        while node is not None:
            node.size += val
            node = node.parent

    def getNode(self, name):
        node:NonBinTree
        for node in self.nodes:
            if node.name == name:
                return node
        return None

    def getBestDir(self,size):
        if self is None:
            return None
        minNode = None
        if self.size > size:
            minNode = self
        for node in self.nodes:
            result = node.getBestDir(size)
            if result is not None:
                if minNode is None or result.size < minNode.size:
                    minNode = result
        return minNode
        

    def __repr__(self) -> str:
        return f'({self.name},{self.size})'


def solution():
    currDir = ''
    root = ''
    ans = []
    sizeNeeded = 0
    bestDir = []
    for line in data:
        # Going into new directory
        if (cdDir := re.search(r'cd (.*)', line)) is not None:
            cdDir = cdDir.group(1)
            if cdDir == '..':
                if currDir.size < 100000:
                    ans.append(currDir.size)
                if currDir.size >= sizeNeeded:
                    bestDir.append(currDir.size)
                currDir = currDir.parent
            else:
                if cdDir == '/':
                    root = NonBinTree(cdDir)
                    currDir = root
                else:
                    currDir = currDir.getNode(cdDir)
        # Increasing directory size
        if (fileSize := re.search(r'\d{1,99}',line)) is not None:
            fileSize = int(fileSize.group())
            currDir.updateSize(fileSize)
            sizeNeeded = 30000000 - (70000000 - root.size)
        # Add child directory
        if (subDir := re.search(r'dir (.*)', line)) is not None:
            subDir = subDir.group(1)
            currDir.insert(subDir)
    # check last directory
    if currDir.size >= sizeNeeded:
        bestDir.append(currDir.size)
    bestDir = min((filter((lambda x: x >= sizeNeeded),bestDir)))
    print(f'Part 1: {sum(ans)}')
    print(f'Part 2: {root.getBestDir(sizeNeeded).size}')


solution()