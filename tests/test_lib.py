import base # noqa: F401
from lib import plot, plot_with_std

test_title = "test_title"
test_label = "test_label"
test_var1 = [1]
test_var2 = [2]
test_var3 = [3]
test_var4 = [4]


def test_plot():
    assert plot(test_var1, test_var2, test_var3, test_title,
                test_label, debug=True) == 'plot completed!'


def test_plot_with_std():
    assert plot_with_std(test_var1, test_var2, test_var3, \
        test_var4, test_title, test_label, debug=True) \
        == 'plot_with_std completed!'


if __name__ == "__main__":
    test_plot()
    test_plot_with_std()
    print("all tests in test_lib passed!")
