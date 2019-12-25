import pytest, os, yaml,sys
from Base.geidata import GetData
sys.path.append(os.getcwd())
def get_sum_data():
    sum_list = []
    data = GetData().get_yml_data("value2.yml")
    for i in data.values():
            sum_list.append(tuple(i.values()))
    return sum_list


# get_sum_data()


#
class TestSum:
    @pytest.mark.parametrize("a,b,c", get_sum_data())
    def test_sum(self, a, b, c):
        print("{}+{}={}".format(a, b, c))

        assert a + b == c
# if __name__ == '__main__':
#     pytest.main(["02_test_sum.py"])