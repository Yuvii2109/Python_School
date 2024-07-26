n = int(input("Enter the the last number till which the series last - "))
def sumOfSeries(n): 
    return sum([i*(i+1)/2 for i in range(1, n + 1)])
if __name__ == "__main__":
  print(sumOfSeries(n))
