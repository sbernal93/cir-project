# IMPORTANT NOTE: If you get an error unpickling these files in train and test then run this!


def run(orig, dest):
    content = ''
    outsize = 0
    with open(orig, 'rb') as infile:
        content = infile.read()
    with open(dest, 'wb') as output:
        for line in content.splitlines():
            outsize += len(line) + 1
            output.write(line + str.encode('\n'))

    print("Done. Saved %s bytes." % (len(content) - outsize))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--constants_path', dest='constants_path', type=str, default='')
    args = parser.parse_args()
    params = vars(args)

    # Load constants json into dict
    CONSTANTS_FILE_PATH = 'constants.json'
    if len(params['constants_path']) > 0:
        constants_file = params['constants_path']
    else:
        constants_file = CONSTANTS_FILE_PATH

    with open(constants_file) as f:
        constants = json.load(f)


    original = constants['db_file_paths']['database']
    destination = constants['db_file_paths']['database']
    run(original, destination)

    original = constants['db_file_paths']['dict']
    destination = constants['db_file_paths']['dict']
    run(original, destination)

    original = constants['db_file_paths']['user_goals']
    destination = constants['db_file_paths']['user_goals']
    run(original, destination)
