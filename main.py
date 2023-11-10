import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    # TODO -  implement top-down memoization
  if (S, T) in MED:
      return MED[(S, T)]
  if (S == ""):
      MED[(S, T)] = len(T)
  elif (T == ""):
      MED[(S, T)] = len(S)
  else:
      if (S[0] == T[0]):
          MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
      else:
          MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))
  return MED[(S, T)]


def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
  s_t = S,T
  if (S, T) in MED:
    return MED[(S, T)]
  elif (not S) and (not T):
    return 0
  elif not T:
    MED[len(S),0] = len(S)
    return S, MED[len(S),0] * '-'
  elif s_t in MED:
    return MED[s_t]
  elif S[0] == T[0]:
    return fast_MED(S[1:], T[1:])
  else:
    one = 1 + fast_MED(S, T[1:])
    two = 1 + fast_MED(S[1:], T)
    three = 1 + fast_MED(S[1:], T[1:])
    mini = min(one, two, three)
    MED[(S, T)] = mini
    return MED[(S, T)]

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

test_MED()
test_align()