py_test () {
    cmd="$1"
    echo "$cmd # :"
    $cmd
    echo ''
}

py_test "python cmdopt_test.py -o 1 --option=value - arg1 -- arg2 arg3"
py_test "python cmdopt_test.py -o1 --option value -- --other-option arg1 arg2 arg3"

