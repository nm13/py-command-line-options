py_test () {
    echo "# $1"
    echo ''
    eval "$1"
    echo ''
    echo ''
}

py_test "python cmdopt_test_alt.py -o 1 --option=value -i 1 --float=0.4"
py_test 'python cmdopt_test_alt.py -o1 --option value --int="wrong value"'
# python cmdopt_test_alt.py -o1 --option value --int="wrong value"
py_test 'python cmdopt_test_alt.py -o1 --option value --custom=0xA'
py_test 'python cmdopt_test_alt.py -o1 --option value --custom=064'
py_test 'python cmdopt_test_alt.py -o1 --option value --custom="one more wrong value"'

