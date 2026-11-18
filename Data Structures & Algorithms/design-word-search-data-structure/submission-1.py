class TrieNode:
    def __init__(self):
        self.children=dict()
        self.isEnd=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()        

    def addWord(self, word: str) -> None:
        cur=self.root

        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur = cur.children[c]
        
        cur.isEnd=True
        
    def sub_search(self,cur,word):
        for i,c in enumerate(word):
            if c==".":
                ## check all children
                for child in cur.children.values():
                    if len(word)==1 and child.isEnd:
                        return True
                    else:
                        res = self.sub_search(child,word[i+1:]) 
                        if res:
                            return True
                return False

            elif c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.isEnd

    def search(self, word: str) -> bool:
        cur=self.root
        return self.sub_search(cur,word)

        # for c in word:
        #     if c==".":
        #         ## which cur? all chilren are cur
        #         continue
        #     elif c not in cur.children:
        #         return False
        #     cur = cur.children[c]
        
        # return cur.isEnd


        
