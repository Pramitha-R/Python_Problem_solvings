def solution(name, surname, age):
    a=[];
    b=[];
    # Implement your solution here
    for i in range(2):
        a.append(name[i])
        b.append(surname[i])
    a=a+b
    a.append(str(age))
    x = "".join(a)

    print(x)

solution("pemmi","marisha",24)