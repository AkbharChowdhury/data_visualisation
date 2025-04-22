# !pip install hvplot
# import statistics
# import ssl
# import pandas as pd
# import numpy as np
# from collections import Counter
# from itertools import chain
# from matplotlib import pyplot as plt
# from matplotlib import pyplot
#
# ssl._create_default_https_context = ssl._create_stdlib_context
# plt.style.use("fivethirtyeight")


class Diagram:
    plt.style.use("fivethirtyeight")
    lang_responses_url: str = 'https://raw.githubusercontent.com/AkbharChowdhury/data_visualisation/refs/heads/main/programming_lang_responses.csv'
    age_responses_url: str = 'https://raw.githubusercontent.com/AkbharChowdhury/data_visualisation/refs/heads/main/age_responses.csv'

    @staticmethod
    def dynamic_most_popular_programming_lang(top: int = 15):
        lang_csv = pd.read_csv(Diagram.lang_responses_url)
        languages = lang_csv['LanguagesWorkedWith']
        language_counter = Counter(list(chain.from_iterable([language.split(';') for language in languages])))
        languages_data: dict[str, int] = {item[0]: item[1] for item in language_counter.most_common(top)}
        languages_data = dict(reversed(list(languages_data.items())))
        df = pd.DataFrame({
            'tech-stack': languages_data.keys(),
            'popularity': languages_data.values()
        })
        return df.hvplot.barh(x='tech-stack',
                              y='popularity',
                              title='Most popular programming languages'.title(),
                              xlabel='Programming Languages'.title(), ylabel="Number of People Who Use",
                              height=400,
                              width=600)

    @staticmethod
    def hist_demo(is_random_age=False):
        age_df = pd.read_csv(Diagram.age_responses_url)
        ages = age_df['Age'] if not is_random_age else np.random.randint(low=99, size=len(age_df.index))
        bins = np.arange(start=10, stop=100 + 1, step=10)
        plt.hist(ages, bins=bins, edgecolor='black', log=True)
        median_age = statistics.median(ages)
        BLUE = '#fc4f30'
        plt.axvline(median_age, color=BLUE, label='Age Median', linewidth=2)
        plt.legend()
        plt.title('Ages of Respondents')
        plt.xlabel('Ages')
        plt.ylabel('Total Respondents')
        plt.tight_layout()
        return plt

    @staticmethod
    def most_popular_programming_lang(top: int = 15):
        data = pd.read_csv(Diagram.lang_responses_url)
        languages = data['LanguagesWorkedWith']
        language_counter = Counter(list(chain.from_iterable([language.split(';') for language in languages])))
        languages_data: dict[str, int] = {item[0]: item[1] for item in language_counter.most_common(top)}
        languages_data = dict(reversed(list(languages_data.items())))
        plt.barh(languages_data.keys(), languages_data.values(), align='center')
        plt.title("Most Popular Languages")
        plt.ylabel("Programming Languages")
        plt.xlabel("Number of People Who Use")
        plt.tight_layout()
        return plt

    @staticmethod
    def free_time():
        hobbies: dict[str, int] = {
            'coding': 46,
            'exercising': 54,
            'shopping': 30,
            'socialising': 25,
            'media consumption': 40,
            'reading': 28
        }

        slices = list(hobbies.values())
        labels = [hobby.title() for hobby in hobbies.keys()]
        longest_hobby = max(hobbies.items(), key=lambda x: x[1])
        explode = [0 if i != longest_hobby[1] else 0.1 for i in hobbies.values()]
        plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%',
                wedgeprops={'edgecolor': 'black'})
        plt.title('How I Spend My Free Time')
        plt.tight_layout()
        return plt

    @staticmethod
    def show(diagram: pyplot):
        diagram.show()
