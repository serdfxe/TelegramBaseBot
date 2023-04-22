# from dependency_injector import containers, providers

# from 


# class ApplicationContainer(containers.DeclarativeContainer):

#     config = providers.Configuration()

#     movie = providers.Factory(entities.Movie)

#     csv_finder = providers.Singleton(
#         finders.CsvMovieFinder,
#         movie_factory=movie.provider,
#         path=config.finder.csv.path,
#         delimiter=config.finder.csv.delimiter,
#     )