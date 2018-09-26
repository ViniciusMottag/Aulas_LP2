def termial(n):
    t=0
    for i in range(1,n+1):
        t=t+i 
    return t
        
print(termial(5))

def test_termial_1(): #correto
    assert termial(5) == 15

def test_termial_2():
    assert termial(6) == 21

def test_termial_3():
    assert termial(4) == 10

def test_termial_4(): #incorreto
    assert termial(5) == 15000