import pickle, json, argparse
from random import seed
from random import randint

def generate_db(path, dict_path):

    with open(dict_path.replace('pkl','txt')) as f:
        values = json.load(f)

    cities = values['destinationAirport']
    carriers = values['carrier']
    dates = values['outboundDate']
    times = values['outboundTime']

    #cities = ["Barcelona" , "Londres", "Milan", "Frankfurt", "Copenhague", "Paris", "Lisboa", "Zurich"]
    #countries = ["Spain", "UK", "Italy", "Germany", "France", "Portugal"]
    #carriers = ["Vueling", "Iberia", "RyanAir", "AirEuropa"]
    #dates = ["Monday", "Tuesday", "Wednesday", "Friday", "Thursday", "Saturday", "Sunday"]
    #times = ["Evening", "Noon", "Morning", "Afternoon"]


    seed(1)

    quotes = {}
    for i in range(5000):
        destCity = randint(0,7)
        originCity = destCity

        while originCity == destCity:
            originCity = randint(0,7)

        quote = {
            'destinationAirport': cities[destCity],
            'originAirport': cities[originCity],
            'carrier': carriers[randint(0,3)],
            'outboundDate': dates[randint(0,6)],
            #'inboundDate': dates[randint(0,6)],
            'outboundTime': times[randint(0,3)],
            #'inboundTime': times[randint(0,3)],
            'quote': randint(0, 300)
        }

        quotes[i] = quote

    pickle_path = path
    txt_path = path.replace('pkl','txt')
    with open(pickle_path, 'wb') as handle:
        pickle.dump(quotes, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open(txt_path, 'w') as file:
         file.write(json.dumps(quotes))


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

    generate_db(constants['db_file_paths']['database'],
        constants['db_file_paths']['dict'])
