from typing import List
import sys
import json

#!/usr/bin/env python3
# File: /workspaces/leetCode-X-Practice/daily/Maximize Area of Square Hole in Grid.py
# Run: python "Maximize Area of Square Hole in Grid.py"


class Solution:
  def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
    """
    Stub for LeetCode-style solution.
    Args:
      n: number of horizontal grid lines (or height-related param)
      m: number of vertical grid lines (or width-related param)
      hBars: list of horizontal bar positions
      vBars: list of vertical bar positions
    Returns:
      int: maximum area of a square hole (implementation needed)
    Note:
      Replace the body with the actual algorithm.
    """
    
    hBars.sort()
    vBars.sort()
    hmax, vmax, hcur, vcur = 1,1,1,1
    for i in range(1, len(hBars)):
      if hBars[i] == hBars[i-1] +1:
        hcur += 1
      else:
        hcur =1
      hmax = max(hmax, hcur)
    for i in range(1, len(vBars)):
      if vBars[i] == vBars[i-1] +1:
        vcur += 1
      else:
        vcur =1
      vmax = max(vmax, vcur)
    
    side = min(hmax,vmax) + 1
    return side**2

def run_case(case):
  n = case["n"]
  m = case["m"]
  hBars = case["hBars"]
  vBars = case["vBars"]
  print("Input:", case)
  res = Solution().maximizeSquareHoleArea(n, m, hBars, vBars)
  print("Output:", res)
  print("-" * 40)

if __name__ == "__main__":
  # If JSON is piped in or passed as first argument, parse it:
  # Accepted formats:
  # 1) A single JSON object: {"n": ..., "m": ..., "hBars": [...], "vBars": [...]} 
  # 2) A JSON array of such objects for multiple test cases.
  input_data = None
  if not sys.stdin.isatty():
    raw = sys.stdin.read()
    raw = raw.strip()
    if raw:
      input_data = json.loads(raw)
  elif len(sys.argv) > 1:
    # python file.py '{"n":3,"m":4,"hBars":[0,2],"vBars":[1,3]}'
    try:
      input_data = json.loads(sys.argv[1])
    except Exception:
      pass

  if input_data is None:
    # Default example tests
    tests = [
      {"n": 5, "m": 5, "hBars": [0, 2, 5], "vBars": [0, 3, 5]},
    ]
  else:
    if isinstance(input_data, list):
      tests = input_data
    else:
      tests = [input_data]

  for tc in tests:
    run_case(tc)