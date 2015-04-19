import nose
import os


def nose_env():
    env = os.environ.copy()
    env['NOSE_NOCAPTURE'] = 1
    env['NOSE_WITH_COVERAGE'] = 1
    env['NOSE_COVER_PACKAGE'] = 'scribe_logger'
    env['NOSE_COVER_BRANCHES'] = 1
    return env


def main():
    nose.main(env=nose_env())

if __name__ == '__main__':
    main()
