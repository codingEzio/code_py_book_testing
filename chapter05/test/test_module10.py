
actually = " It's nothing here! "

some_cmds_u_might_use = """
    -h              help
    -x              stop the execution of tests after the 1st failure
    --maxfail=N     stop execution after N failures
    --durations=N   show the N slowest tests 
"""

export_test_result = """
    py.test {
        --junitxml=BASENAME.xml     .xml
        --resultlog=BASENAME.log    .log
        -v --pastebin=all           export to an online service (pastebin)
    }
"""
