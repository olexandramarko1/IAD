import pandas as pd
from matplotlib import pyplot as plt


def choose_plot():
    print('Choose columns to plot: \n 1 - Temperature\n 2 - Dew Point\n 3 - Humidity\n 4 - Wind\n 5 - Wind Speed\n 6 '
          '- Wind Gust\n 7 - Pressure\n 8 - Precip.\n 9 - Precip. Accum\n 10 - Condition\n')
    choice = input().split()
    args = []
    for i in choice:
        if i == '1':
            args.append('Temperature')
        elif i == '2':
            args.append('Dew Point')
        elif i == '3':
            args.append('Humidity')
        elif i == '4':
            args.append('Wind')
        elif i == '5':
            args.append('Wind Speed')
        elif i == '6':
            args.append('Wind Gust')
        elif i == '7':
            args.append('Pressure')
        elif i == '8':
            args.append('Precip.')
        elif i == '9':
            args.append('Precip. Accum')
        elif i == '10':
            args.append('Condition')
        else:
            print('Wrong input ', i)
    print(args)
    return args


def display(dataf, args):
    for column in args:
        if dataf[column].dtype == object:
            plt.pie(dataf[column].value_counts(), labels=dataf[column].value_counts().to_frame().index)
            plt.show()
        else:
            dataf.reset_index().plot(x='DayTime', y=column)  # make day + time
            plt.show()
    return


def windSpeed_to_general(value):
    novel_value = value.replace(' mph', '')
    return int(novel_value)


def date_to_general(value):
    novel_value = (value + ".2019").replace('.', '-')
    return str(novel_value)


def pressure_to_general(value):
    novel_value = value.replace(',', '.')
    return float(novel_value)


def parser(dataframe):
    dataframe['Wind Speed'] = dataframe['Wind Speed'].apply(windSpeed_to_general)

    dataframe['Wind Gust'] = dataframe['Wind Gust'].apply(windSpeed_to_general)

    dataframe['Time'] = pd.to_datetime(dataframe['Time']).dt.strftime('%H:%M')

    dataframe['DayTime'] = pd.to_datetime(dataframe['day/month'] + '.2019' + ' ' + dataframe['Time'])

    dataframe['Pressure'] = dataframe['Pressure'].apply(pressure_to_general)

    dataframe['Humidity'] = dataframe['Humidity'].str.rstrip('%').astype('float')

    del dataframe['day/month'], dataframe['Time']

    print(dataframe.dtypes)
    return dataframe


dataframe = pd.read_csv('DATABASE.csv', sep=';')
dataframe = parser(dataframe)
dataframe.set_index('DayTime', inplace=True)
print(dataframe)

args = choose_plot()

display(dataframe, args)
