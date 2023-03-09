from typing import List

class NestedIterator:
    def __init__(self, nestedList: List):
        self.flatList = list(self.flatten(nestedList))
        self.cur = 0

    def flatten(self, l) -> List[int]:
        for item in l:
            if type(item) == int:
                yield item
            else:
                yield from self.flatten(item)

    # def next(self) -> int:
    #     if type(self.nestedList[self.cur]) == int:  
    #       self.cur += 1
    #       return self.nestedList[self.cur-1]
    #     else:
    #         l = self.nestedList.pop(self.cur)
    #         print(l, self.cur)
    #         for item in l:
    #             self.nestedList.insert(self.cur, item)

    def next(self) -> int:
        self.cur += 1
        return self.flatList[self.cur-1]

    def hasNext(self) -> bool:
        return self.cur < len(self.flatList)

res = []
it = NestedIterator([[1,1],2,[1,1]])
# it = NestedIterator([1,[4,[6]]])
while it.hasNext():
    res.append(it.next())
print(res)

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: List['NestedInteger']):
        self.flatList = list(self.flatten(nestedList))
        self.cur = 0

    def flatten(self, nestedList: List['NestedInteger']) -> List['NestedInteger']:
        for item in nestedList:
            if item.isInteger():
                yield item.getInteger()
            else:
                yield from self.flatten(item.getList())

    def next(self) -> int:
        self.cur += 1
        return self.flatList[self.cur - 1]
    
    def hasNext(self) -> bool:
        return self.cur < len(self.flatList)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())