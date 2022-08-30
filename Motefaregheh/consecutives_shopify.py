 # test_list3 = [1,3,4,5,6,7,9]
 # test_output3 = [(1,1), (3,7), (9,9)]

def consecutives(ary):
    li = []
       
    index = 0
    flag = False    
    while index < len(ary) :    
      if not flag:
        first = last = ary[index]
        flag = True
        index+=1
      elif ary[index] == last+1:
         last = ary[index]
         index+=1
      else:         
         li.append((first, last))
         flag = False         
        
    if flag:
       li.append((first, last)) 
    print(li)
    
    
    def cons_2():
      li = []       
      index = 0
      first = ary[index]
      while index+1 < len(ary) and ary[index+1] == ary[index] + 1:
        index +=1
      li.append((first, ary[index]))
      index+=1
      if index <len(ary):
         first = ary[index]
    print(li)
    
    def consecutives_3(ary):
      li = []
    first_index = last_index = 0
    while first_index < len(ary) and last_index < len(ary)  :    
      while last_index+1 < len(ary) and ary[last_index+1] == ary[last_index] + 1:
        last_index +=1
      li.append((ary[first_index], ary[last_index]))
      first_index = last_index = last_index + 1
      
    print(li)

      
      
      
      
      
consecutives([1,3,4,5,6,7,9])      
         
      
     
         
    
    

