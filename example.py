temperature = 10

def print_temperature():
    print(temperature)
    #return temperature

def test_temperature():
    assert print_temperature() == 10
