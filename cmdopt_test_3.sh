# python cmdopt_test_3.py -- 1 2 3
# python cmdopt_test_3.py -- -o1
# python cmdopt_test_3.py -o1
# python cmdopt_test_3.py --option "'True'"

py_test () {
    cmd="$*"
    echo "# $cmd"
    echo ''
    eval "$cmd"
    echo ''
    echo ''
}

{
py_test 'python cmdopt_test_3.py --option "True"'
py_test 'python cmdopt_test_3.py --option True'
py_test 'python cmdopt_test_3.py --option 2.5'
py_test "python cmdopt_test_3.py --option '{1:2}'"
# test eval() failure
py_test "python cmdopt_test_3.py --option 'fuzzy'"
# python cmdopt_test_3.py --option '"fuzzy"'
py_test 'python cmdopt_test_3.py --option ' "'" '"fuzzy"' "'"
} 2>&1 | less
