import pickle, json, argparse

def generate_dict(path):
    pickle_path = path
    txt_path = path.replace('pkl', 'txt')

    cities = ["Barcelona" , "London", "Milan", "Frankfurt", "Copenhague", "Paris", "Lisbon", "Zurich"]
    dates = ["Monday", "Tuesday", "Wednesday", "Friday", "Thursday", "Saturday", "Sunday"]
    times = ["Evening", "Noon", "Morning", "Afternoon"]
    carriers = ["Vueling", "Iberia", "RyanAir", "AirEuropa"]

    dict = {'destinationAirport': cities,
    'originAirport': cities,
    'carrier': carriers,
    'outboundDate': dates,
    #'inboundDate':dates,
    'outboundTime': times}
    #'inboundTime':times}

    with open(pickle_path, 'wb') as handle:
        pickle.dump(dict, handle)

    with open(txt_path, 'w') as file:
         file.write(json.dumps(dict))

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

    generate_dict(constants['db_file_paths']['dict'])
