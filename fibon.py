def fibonachi(n=5):

    def inner(a, b, nn):
        if nn > 0:
            return inner(b, a + b, nn - 1)

        return a + b

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n < 0:
        return ((n + 1) % 2 == 0) and inner(1, 1, abs(n) - 3) or inner(1, 1, abs(n) - 3) * (-1)
    else:
        return inner(1, 1, n - 3)

if __name__ == '__main__': # pragma no cover
    import coverage, os, unittest

    cov = coverage.coverage(branch=True,omit='__init__')
    cov.start()
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print "Coverage Summary:"
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'coverage')
    cov.html_report(directory=covdir)
    cov.erase()