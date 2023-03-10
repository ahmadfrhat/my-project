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
    city = input( "please choose a city from (chicago , new york city , washington): ").lower()
    while True:
         if city not in CITY_DATA.keys():
            print("invaild city name please try again/n: ")
            city = input( "please choose a city from (chicago , new york city , washington): ").lower()
         else:
            print(city)
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input(" please choose and type a full month name or type all: ").lower()
    months = ['january' , 'faburay' , 'march' , 'april' , 'may' , 'june' , 'all' ]
    while True:
          if month not in months:
              print("invaild month name please try again")
              month = input(" please choose and type a full month name or type all: ").lower()
          else:
            print(month)
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("please add a week day name or type all: ").lower()
    days = ['saturday', 'sunday', 'monday' , 'tusday', 'wedensday','thrusday','friday','all']
    while True:
          if day not in days:
              print('invaild week day name please try again')
              day = input("please add a week day name or type all: ").lower()
          else:
            print(day)
            break
    print('-'*40)
    return city, month, day


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
    
# LOADING DATA FOR CITY
    df = pd.read_csv(CITY_DATA[city])
       # COVERTING START TIME COLUMN TO DATE TIME COLUMN
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
     
    #filter by month if applicable      
    if  month !='all':
        months = ['january' , 'faburay' , 'march' , 'april' , 'may' , 'june' , 'all' ]
        month = months.index(month) + 1
  #filter by month to create a new data frame
        df = df[df['month']== month]
        
   #filter by day of week if applicable      
    if day != 'all': 
   #filter by day of week to creat a new data frame
        df = df[df['day'] == day.title()]

    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
  # TO DO: display the most common month           
    most_common_month = df['month'].mode()[0]
    print('the most common month is : {} ' .format(most_common_month))
    
    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('the most common day of week is : {} '.format(most_common_day))
    
    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('the most common hour is : {} '.format(most_common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
  
    print("the most common start station is {}".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(' the most commonly used end station is {} :'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['start to end']=df['Start Station'] + "," + df['End Station']
                                                                        
    print(' the most common start to end line is :{} '.format(df['start to end'].mode()[0]))

   
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_drive_time = df['Trip Duration'].sum()
    print('total drive time is : {} '.format([total_drive_time]))

    # TO DO: display mean travel time
    average_travel_time= df['Trip Duration'].mean()
    print('average travel time: {}'.format([average_travel_time]))
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts().to_frame()
    print("the counts of user types are :{}".format(user_types))

    # TO DO: Display counts of gender
    try:
        gender = dg ['User Type'].value_counts()
        print('gender count is : {} ' .format())    
    except:
        print('no data for gender')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year =int(df['Birth Year'].min())
        print('earliest year of birth is: {}'.format(earliest_birth_year))
    except:
        print('no data for birth year')
        
    try:
        most_common =int(df['Birth Year'].mode()[0])
        print('the most common year of birth:{}'.format(most_common))
    except:
        print('no data for the most common year of birth')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def data_display(df):
    # making user apple to show some rows of data upon request.
    print('raw data is now available to check')
    
    rows = 0 
    ask_user = input('would you like to viwe 5 rows of the selected city data? , please enter yes or no' ).lower()
    if ask_user not in ['yes', 'no']:
        print('invaild choice please print yes or no')
        ask_user = input('would you like to viwe 5 rows of the selected city data? , please enter yes or no').lower()
    elif ask_user != 'yes':
        print('thanks')
    else:
         while rows+5 < df.shape[0]:
             print(df.iloc[rows:rows+5])
             rows += 5
             ask_user = input('would you like 5 more rows of raw data?')
             if ask_user != 'yes':
                 print('thank you')
                 break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    
# MY REFERENCES :
#https://www.resourcespace.com/
#https://github.com/Aritra96/bikeshare-project/blob/master/bikeshare.py
#https://pandas.pydata.org/pandas-docs/stable/index.html
