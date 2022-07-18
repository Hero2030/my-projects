import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    CITY_NAMES = {'new york city': 1, 'chicago': 2, 'washington': 3}
    CITY = ''
    while True:
      print("\Choose your preferred city you want to view its data.washington,chicago,new York City.\n")
      CITY = input().strip().lower()
      if CITY not in CITY_NAMES.keys():
          print("Sorry,that\'s awrong attempt.Please enter acorrect city name and try again.")
          continue
      else:
          break

    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_NAMES = {'all': 0, 'january': 1, 'february': 2, 'march': 3,'april': 4, 'may': 5, 'june': 6}
    MONTH = ''
    while True:
      print("\nEnter the name of your favorite month whose data you want to view. january, february, march, april, may, june or  ENTER 'all' if you do not have any favorite month.\n")
      MONTH = input().strip().lower()
      if MONTH not in MONTH_NAMES.keys():
          print("Sorry,that\'s awrong attempt.Please enter acorrect month name and try again.")
          continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_NAMES = {'all': 0, 'sunday': 1, 'saturday': 2, 'monday': 3, 'tuesday': 4, 'wednesday': 5, 'thursday': 6, 'friday': 7}
    DAY = ''
    while True:
      print("\nEnter the name of your favorite day whose data you want to view. sunday, monday, tuesday, wednesday, thursday, friday, saturday orENTER 'all' if you do not have any favorite day.\n")
      DAY = input().strip().lower()
      if DAY not in DAY_NAMES.keys():
          print("Sorry,that\'s awrong attempt.Please enter acorrect day name and try again.")
          continue
      else:
           break
     
    print('*'*80)
    return CITY, MONTH, DAY


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

   # loading data file into a dataframe
    print("\nplease wait....")
    df = pd.read_csv(CITY_DATA[city])

    # converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracting month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filtering by month 
    if month != 'all':
    # useing the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # filtering by month to create the new dataframe
        df = df[df['month'] == month]

        # filtering by day of week 
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    Most_frequent_month = df['month'].mode()[0]
    print('Most frequent month:', Most_frequent_month)
    # TO DO: display the most common day of week
    Most_frequent_day = df['day_of_week'].mode()[0]
    print('Most frequent day:', Most_frequent_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    Most_frequent_hour = df['hour'].mode()[0]
    print('Most frequent hour:', Most_frequent_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Most_frequent_Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most frequent Start Station:', Most_frequent_Start_Station)

    # TO DO: display most commonly used end station
    Most_frequent_End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost frequent End_Station:', Most_frequent_End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    recurring_track=df.groupby(['Start Station','End Station'])
    Most_recurring_track = recurring_track.size().sort_values(ascending=False).head(1)
    print(' The Most recurring track is:\n', Most_recurring_track)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*80)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Time_value=60*60*24*30
    Total_Travel_Time = df['Trip Duration'].sum()
    print('Total travel time by monthe is:', Total_Travel_Time/Time_value, " month")

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time is:', Mean_Travel_Time/60, " Minute")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*80)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    Counts_Of_User_Types = df['User Type'].value_counts().to_frame()
    print('\nCounts Of User Types:\n', Counts_Of_User_Types)

    # TO DO: Display counts of gender
    try:
      sex_type = df['Gender'].value_counts()
      print('\nSex type is:\n',  sex_type)
    except:
      print("\nsex data does not exist for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
 
    try:
      EARLIEST_YEAR = df['Birth Year'].min()
      print('\nEARLIEST YEAR IS:',  EARLIEST_YEAR)
    except:
      print("\nBirth Year data does not exist for this month.")

    try:
      RECENT_YEAR = df['Birth Year'].max()
      print('\nRECENT YEAR:', RECENT_YEAR)
    except:
      print("\n Birth Year data does not exist for this month.")

    try:
      COMMON_YEAR = int(df['Birth Year'].mode()[0])
      print('\nCOMMON Year is:', COMMON_YEAR)
    except:
      print("\nBirth Year data does not exist for this month")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*80)
def display_data(df):
       #Displays 5 rows of data from the csv file for the selected city.
       Possible_answers = ['Yes', 'No']
       DATA_RAWS = ''
       #Counter variable is only used  to show acertain data.
       counter = 0
       while  DATA_RAWS not in Possible_answers:
        print("\nDo you want to view the data?\nType Yes or NO")
        DATA_RAWS = input().lower()
        #Showing data according to the user's input.
        if  DATA_RAWS == "yes":
            print(df.head())
        elif  DATA_RAWS not in Possible_answers:
            print("Your answer is not correct.please ENTER aright one.")
            print("\nThank you.\n")
            break
       #Another while loop Displays another 5 rows.
       while DATA_RAWS == 'yes':
        print("Do you want to view more data?\nType Yes or NO?")
        counter += 5
        DATA_RAWS = input().lower()
        #Displays another 5 rows of data from the csv file for the selected city.
        if DATA_RAWS == "yes":
             print(df[counter:counter+5])
        elif DATA_RAWS != "yes":
             break
        
               
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
