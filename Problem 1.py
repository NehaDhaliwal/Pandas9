# Game Play Analysis I

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby('player_id')['event_date'].min().reset_index()
    df.rename(columns={'event_date': 'first_login'}, inplace=True)
    print(df)
    return df

data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-05-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})

game_analysis(activity)