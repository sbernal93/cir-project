import pickle, json, argparse
import random
from random import seed
from random import randint

def generate_goals(path, dict_path):
    pickle_path = path
    txt_path = path.replace('pkl','txt')

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

    goals = []
    seed(1)
    for i in range(200):
        goal = {}
        removeKey = 'inform_slots'
        destCity = randint(0,7)
        originCity = destCity

        while originCity == destCity:
            originCity = randint(0,7)

        c = randint(0,4)
        if c < 3:
            goal = {'request_slots': {},
             'diaact': 'request',
             'inform_slots': {'destinationAirport': cities[destCity],
             'originAirport': cities[originCity],
             'outboundDate': dates[randint(0,6)],
             #'inboundDate': dates[randint(0,6)],
             #'inboundTime': times[randint(0,3)],
             'outboundTime': times[randint(0,3)],
             }}

        else:
            removeKey = 'request_slots'
            goal = {'request_slots':{
                'originAirport':'UNK',
                'outboundDate':'UNK',
                #'inboundDate':'UNK',
                #'inboundTime':'UNK',
                'outboundTime':'UNK'
            }, 'diaact':'request',
            'inform_slots':{'destinationAirport': cities[destCity]}}

        #removes random elements from the dict
        for x in range(randint(0,2)):
            choice = random.choice(list(goal[removeKey].keys()))
            if choice != 'destinationAirport':
                goal[removeKey].pop(choice)
        goals.append(goal)

    with open(pickle_path, 'wb') as handle:
        pickle.dump(goals, handle)

    with open(txt_path, 'w') as file:
         file.write(json.dumps(goals))


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

    generate_goals(constants['db_file_paths']['user_goals'],
        constants['db_file_paths']['dict'])
