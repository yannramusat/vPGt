#!/bin/env python3
from app import App
import matplotlib.pyplot as plt
import numpy as np
import os

if __name__ == "__main__":
    # app setup
    scheme = "bolt"
    hostname = "localhost"
    port = "7687"
    uri = f"{scheme}://{hostname}:{port}"
    app = App(uri, "neo4j", verbose=False)

    # common prefix for CSVs; the data has been generated by iBench
    prefix = "file://"+os.path.join(os.getcwd(), "output-ibench-data/")
    nbLaunches = 5
    showStats = True
    nodeIndexes = True
    relIndexes = True
    x = [100, 200, 500, 1_000]#, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000]
    y = [100, 200, 500, 1_000, 2_000, 5_000, 10_000]#, 20_000, 50_000]
    z = [100, 200, 500, 1_000, 2_000, 5_000]
    
    # temporary testing playground for the baseline of PA
    #from scenarios.personaddress import *
    #scenario = PersonAddressScenarioPlain(prefix, size=2000)
    #scenario.run(app, launches=nbLaunches, stats=showStats, nodeIndex=True, relIndex=False)
    #scenario = PersonAddressScenarioBaseline(prefix, size=2000)
    #scenario.run(app, launches=nbLaunches, stats=showStats, nodeIndex=False, relIndex=False)
    #scenario = PersonAddressScenarioBaseline(prefix, size=2000)
    #scenario.run(app, launches=nbLaunches, stats=showStats, nodeIndex=True, relIndex=False)

    # choose the experiments to run, and their parameters
    from figures.personaddress import *
    from figures.flighthotel import *
    from figures.flighthoteluc import *
    from figures.personaddressm1 import *
    from figures.personaddressm2 import *
    from figures.personaddressrev import *
    from figures.flighthotelsplit import *
    from figures.persondata import *
    from figures.dta1 import *
    from figures.a1ta3 import *
    figures = [
        #FigureComparisonIndexesPersonAddress(app, prefix=prefix, values=x, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonAlternativeApproachesPersonAddress(app, prefix=prefix, values=y, nbLaunches=nbLaunches, showStats=showStats),

        #FigureComparisonIndexesFlightHotel(app, prefix=prefix, values=x, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonAlternativeApproachesFlightHotel(app, prefix=prefix, values=y, nbLaunches=nbLaunches, showStats=showStats),

        #FigureComparisonConstraintsFlightHotelUC(app, prefix=prefix, values=x, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonAlternativeApproachesFlightHotelUC(app, prefix=prefix, values=y, nbLaunches=nbLaunches, showStats=showStats, withConflicts=False),

        #FigureComparisonIndexesPersonAddressM1(app, prefix=prefix, values=x, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonAlternativeApproachesPersonAddressM1(app, prefix=prefix, values=y, nbLaunches=nbLaunches, showStats=showStats),
        
        #FigureComparisonIndexesPersonAddressM2(app, prefix=prefix, values=x, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonAlternativeApproachesPersonAddressM2(app, prefix=prefix, values=y, nbLaunches=nbLaunches, showStats=showStats),
        
        #FigureComparisonIndexesPersonAddressRev(app, prefix=prefix, values=x, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonAlternativeApproachesPersonAddressRev(app, prefix=prefix, values=y, nbLaunches=nbLaunches, showStats=showStats),

        #FigureComparisonFlightHotelSplit(app, prefix=prefix, values=y, nbLaunches=nbLaunches, showStats=showStats),
        
        #FigureComparisonIndexesPersonData(app, prefix=prefix, values=x, nbLaunches=nbLaunches, showStats=showStats),
        #FigureLongRunPersonData(app, prefix=prefix, values=y, nbLaunches=nbLaunches, showStats=showStats),

        #FigureComparisonIndexesDTA1(app, prefix=prefix, values=x, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonAlternativeApproachesDTA1(app, prefix=prefix, values=y, nbLaunches=nbLaunches, showStats=showStats),

        FigureComparisonIndexesA1TA3(app, prefix=prefix, values=x, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonAlternativeApproachesA1TA3(app, prefix=prefix, values=y, nbLaunches=nbLaunches, showStats=showStats),

        #FigureComparisonBaselineFlightHotel(app, prefix=prefix, values=z, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonBaselinePersonAddress(app, prefix=prefix, values=z, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonBaselinePersonData(app, prefix=prefix, values=z, nbLaunches=nbLaunches, showStats=showStats),
    ]
    
    # compute results    
    for fig in figures:
        fig.compute()
    
    # (optional) print results to the terminal
    if showStats:
        for fig in figures:
            fig.print_cmd()
    
    # generate figures
    for fig in figures:
        fig.plot()
    
    # show figures
    plt.show()

    # close connection
    app.close()
