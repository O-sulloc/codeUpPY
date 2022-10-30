list1 =[1,2,3,4,5]
list2 = [6,7,8,9,10]

#순서대로 더하기
result = map(lambda a,b: a+b, list1,list2)
#list1에 있는 0번재 원소 + list2에 있는 0번째 원소
#더하기 해서 result에 넣고

print(list(result)) #list형식으로 REsult 출력