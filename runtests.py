import nose
import os


def main():
    nose.main(env=env)

if __name__ == '__main__':
    env = os.environ.copy()
    env['NOSE_NOCAPTURE'] = 1     # Don't capture output, print to STDOUT
    main()
