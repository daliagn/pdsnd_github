import time
import pandas
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
    city = input("Choose a city please (chicago, new york city, washington)").lower()
    #print ("You chose: " + city)
    while city not in ('chicago', 'new york city', 'washington'):
        print("Sorry, I didn't catch that. Enter again:")
        print("Please enter one of the cities (chicago, new york city, washington)")
        city = input("Choose a city please (chicago, new york city, washington)")


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("please choose a month (all, january, february, ... , june)").lower()
    while month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september','october','november','december'):
        print("Sorry, I didn't catch that. Enter again:")
        print("Please enter one of the months")
        month = input("please choose a month (all, january, february, ... , june)")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("please choose a day (all, monday, tuesday, ... sunday)").lower()
    while day not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
        print("Sorry, I didn't catch that. Enter again:")
        print("Please enter one of the days")
        day = input("please choose a day (all, monday, tuesday, ... sunday)")


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
    #load data for the city
    df = pandas.read_csv(CITY_DATA[city])

    #convert start time to datetime
    df['Start Time'] = pandas.to_datetime(df['Start Time'])

    #extract month from start time
    df['month'] = df['Start Time'].dt.month

    #extract day from the start time
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #filter by month
    if month != 'all':
        #getting the number of the month
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september','october','november','december']
        month = months.index(month) + 1
        #create a new dataframe
        df = df[df['month'] == month]

    #filter by day
    if day != 'all':
        #create a new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("the most popular month is: " , popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("the most popular day is: " , popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("the most popular hour is: " , popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("the most commonly used start station is: ",common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("the most commonly used end station is: ",common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start End'].mode()[0]


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print("total travel time is: " , total_duration)


    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print("mean travel time is: " , mean_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("the types of users by their number are: " , user_type)


    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("the gender of users by its number is: " , gender)
    except:
        print("the gender is not exists")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print("the earliest year of birth is: ", earliest)
        print("the most recent year of birth is: " , recent)
        print("the most common year of birth is: " , common_year)
    except:
        print("the birth year is not exists")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #displaying data depending on user request
        response_data= ''
        counter = 0
        while response_data not in ['yes','no']:
            print("do you want to see raw data? Enter yes or no")
            response_data = input().lower()
        #if user write yes
            if response_data == "yes":
                print(df.head())
            elif response_data not in ['yes','no']:
                print("please enter an accpted response (yes or no)")


    #ask user to show 5 more rows
        while response_data == 'yes':
            print("do you want to see 5 more rows?")
            counter += 5
            response_data = input().lower()
            #If yes, display data
            if response_data == "yes":
                print(df[counter:counter+5])
            #if not, stop
            elif response_data != "yes":
                break

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
