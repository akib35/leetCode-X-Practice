class Solution:
  def __init__(self):
    self.arr = []
    

  def gen(self, s:str , l: int):
    if len(s) == l:
      self.arr.append(s)
      return
    
    if len(s) == 0:
      self.gen(s+'a',l)
      self.gen(s+'b',l)
      self.gen(s+'c',l)
    elif s[len(s)-1] == 'a':
      self.gen(s+'b',l)
      self.gen(s+'c',l) 
    elif s[len(s)-1] == 'b':
      self.gen(s+'a',l)
      self.gen(s+'c',l)
    elif s[len(s)-1] == 'c':
      self.gen(s+'a',l)
      self.gen(s+'b',l)      
    
  def getHappyString(self, n: int, k: int) -> str:
    self.gen('',n)
    if k > len(self.arr):
      return ""
    else:
      return self.arr[k-1]
    


def main():
  s = Solution()
  s.gen('',3)
  print(s.arr)
  
if __name__ == '__main__':
  main()