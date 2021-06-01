import article_api as ap
import matplotlib.pyplot as plt

def main():
    aricles_from_2020 = ap.get_articles(2000, '01/01/2020', '12/31/2020')
    aricles_from_2020_subjects = ap.subject_from_articles(aricles_from_2020)
    print(ap.found_most_tags(aricles_from_2020_subjects))
    with open('results/tags.txt', 'w') as file:
        file.write('Облако тегов для 5 самых используемых тематик в 2020 году\n')
        for tag in ap.found_most_tags(aricles_from_2020_subjects):
            file.write(f'{tag[0]} - всетилось {tag[1]} раз\n')


    diffrent_articles_years = []
    diffrent_articles = ap.get_articles(1000, page=100)
    diffrent_articles_years.extend(ap.get_years_of_articles(diffrent_articles))
    diffrent_articles = ap.get_articles(1000, page=1000)
    diffrent_articles_years.extend(ap.get_years_of_articles(diffrent_articles))
    diffrent_articles = ap.get_articles(1000, page=4000)
    diffrent_articles_years.extend(ap.get_years_of_articles(diffrent_articles))
    diffrent_articles = ap.get_articles(1000, page=6000)
    diffrent_articles_years.extend(ap.get_years_of_articles(diffrent_articles))
    diffrent_articles = ap.get_articles(1000, page=7000)
    diffrent_articles_years.extend(ap.get_years_of_articles(diffrent_articles))

    diffrent_articles_years_counter = ap.get_years_counter(diffrent_articles_years)
    print(diffrent_articles_years_counter)

    fig, ax = plt.subplots()

    ax.bar(list(diffrent_articles_years_counter.keys()), list(diffrent_articles_years_counter.values()))

    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)  # ширина Figure
    fig.set_figheight(6)  # высота Figure

    fig.savefig('results/years.png')

if __name__ == '__main__':
    main()

