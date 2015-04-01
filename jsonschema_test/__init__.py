import sys
import os
import json
from jsonschema import validate


def load_json(path):
    with open(path) as fp:
        return json.load(fp)


def load_json_suite(path):
    schema = test_schema()
    suite = load_json(path)

    try:
        validate(suite, schema)
    except Exception as e:
        print('{} is not a valid test file.'.format(path))
        print(e)
        exit(2)

    return suite


def print_ansi(code, text):
    print('\033[{}m{}\x1b[0m'.format(code, text))


print_bold = lambda text: print_ansi(1, text)
print_green = lambda text: print_ansi(32, text)
print_red = lambda text: print_ansi(31, text)


def test_schema():
    path = os.path.join(os.path.dirname(__file__), 'schema.json')
    return load_json(path)


def test(schema_path, suite_paths):
    schema = load_json(schema_path)
    suites = map(load_json_suite, suite_paths)

    passes = 0
    failures = 0

    for suite in suites:
        for case in suite:
            print_bold('-> {}'.format(case['description']))

            for test in case['tests']:
                success = True

                try:
                    validate(test['data'], schema)
                except Exception as e:
                    if test['valid']:
                        success = False
                else:
                    if not test['valid']:
                        success = False

                if success:
                    passes += 1
                    print_green('  -> {}'.format(test['description']))
                else:
                    failures += 1
                    print_red('  -> {}'.format(test['description']))
                    print('    Expected data to validate as: {}'.format(test['valid']))
                    print('    ' + json.dumps(test['data']))
                    print('')

            print('')

    print('{} passes, {} failures'.format(passes, failures))

    if failures:
        exit(1)


def usage():
    print('Usage: {} <schema> [test suites, ...]'.format(sys.argv[0]))


def validate_json(filename):
    if not os.path.isfile(filename):
        print('{} does not exist.'.format(filename))
        exit(2)

    with open(filename) as fp:
        try:
            json.load(fp)
        except Exception as e:
            print('{} does not contain valid JSON.'.format(filename))
            exit(2)


def main():
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            validate_json(filename)

        schema = sys.argv[1]
        suites = sys.argv[2:]

        if len(suites) > 0:
            test(schema, suites)
    else:
        usage()


if __name__ == '__main__':
    main()

