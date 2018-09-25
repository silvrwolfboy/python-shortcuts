import argparse
import os.path

import shortcuts


def convert_shortcut(input_filepath, out_filepath):
    input_format = _get_format(input_filepath)
    out_format = _get_format(out_filepath)

    with open(input_filepath, 'rb') as f:
        sc = shortcuts.Shortcut.load(f, file_format=input_format)
    with open(out_filepath, 'wb') as f:
        sc.dump(f, file_format=out_format)


def _get_format(filepath):
    _, ext = os.path.splitext(filepath)
    ext = ext.strip('.')
    if ext in ('shortcut', 'plist'):
        return 'plist'
    elif ext == 'toml':
        return 'toml'

    raise RuntimeError(f'Unsupported file format: {filepath}: "{ext}"')


def main():
    parser = argparse.ArgumentParser(description='Shortcuts: Siri shortcuts creator')
    parser.add_argument('file', nargs='?', help='Input file: *.(toml|shortcut|itunes url)')
    parser.add_argument('output', nargs='?', help='Output file: *.(toml|shortcut)')
    parser.add_argument('--version', action='store_true', help='Version information')

    args = parser.parse_args()

    if not any([args.version, args.file, args.output]):
        parser.error('the following arguments are required: file, output')

    if args.version:
        print(f'Shortcuts v{shortcuts.VERSION}')
        return

    convert_shortcut(args.file, args.output)


if __name__ == '__main__':
    main()
