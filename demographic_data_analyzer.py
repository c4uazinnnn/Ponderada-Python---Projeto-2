import pandas as pd

df = pd.read_csv('adult.data.csv')

def calculate_demographic_data(print_data=True):
    race_count = df['race'].value_counts()
    
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
    
    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_edu]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[~higher_edu]['salary'] == '>50K').mean() * 100, 1)
    
    min_work_hours = df['hours-per-week'].min()
    
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    rich_percentage = round(
        (df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0] / num_min_workers) * 100,
        1
    )
    
    country_earn = df[df['salary'] == '>50K'].groupby('native-country').size() / df.groupby('native-country').size() * 100
    highest_earning_country = country_earn.idxmax()
    highest_earning_country_percentage = round(country_earn.max(), 1)
    
    india_top_occ = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts().idxmax()
    
    if print_data:
        print("Number of each race:")
        print(race_count.to_string())
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", india_top_occ)
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': india_top_occ
    }
