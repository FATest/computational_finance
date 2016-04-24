__author__ = 'DushyanthK'



from numpy import *
import numpy as np
import operator
class Option:
    def __init__(self, strike, maturity, bid, ask, underlying, typ, vol = 0):
        self.bid        = bid
        self.ask        = ask
        self.maturity   = maturity
        self.underlying = underlying
        self.strike     = strike
        self.vol        = vol
        self.typ        = typ

def readTDAmeritradeData(fileName, max_chain_size = 1024):
    W = dict()
    chain = []
    try:
      data = np.genfromtxt(str(fileName),delimiter=',',dtype=None,skip_header=1)
    except IOError as e:
      print "I/O error({0}): {1}".format(e.errno, e.strerror)
      raise
    except ValueError:
      print "Could not convert data to an integer."
      raise
    except:
      print "Unexpected error:", sys.exc_info()[0]
      raise

    for i in range(len(data)):
        tau = (data[i][1])/365.0
        o = Option(float(data[i][16]),tau,float(data[i][11]),float(data[i][13]), float(data[i][0]),'C',float(data[i][7]))
        chain.append(o)
        if ((o.ask -o.bid) <> 0.0):
          W[i] = 1.0/(o.ask-o.bid)
        else:
          W[i] = 1e-3

    sort_w = dict()
    sort_w = sorted(W.items(), key=operator.itemgetter(1))
    sort_w.reverse()
    m_keys = []
    for i in range(1024):
        m_keys.append(sort_w[i][0])

    m_chain = []
    for i in range(1024):
        m_chain.append(chain[m_keys[i]])
    return m_chain

if __name__ == "__main__":
    m_chain = []
    m_chain = readTDAmeritradeData("/Users/DushyanthK/Documents/MSF/MSF 526/Lectures/Lecture 10/SPX_08082013.csv")
