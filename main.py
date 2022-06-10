for number in range(5) :
  print("------------------------------------------------------------")
  print("I am outer loop iteration "+str(number))

  for another_number in range(3):
    print("************************************")
    print("I am inner loop iteration "+str(another_number))