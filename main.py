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
    # the following is for a Neo4j community edition running locally
    #prefix = "file://"+os.path.join(os.getcwd(), "output-ibench-data/")
    # the following is for a Neo4j Docker image running locally, and configured that way:
    # sudo docker run --name neo4jVol -p 7474:7474 -p 7687:7687 -v ~/research/vPGt/output-ibench-data:/var/lib/neo4j/import --env NEO4J_AUTH=none neo4j:5.16.0-community
    prefix = "file:///"
    # then sudo chown -R yann:yann output-ibench-data if necessary
    nbLaunches = 5
    showStats = True
    nodeIndexes = True
    relIndexes = True
    w = [100, 200, 500, 1_000, 2_000, 5_000, 10_000, 20_000]#, 50_000]
    x = [100, 200, 500, 1_000]#, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000]
    y = [100, 200, 500, 1_000, 2_000, 5_000, 10_000]#, 20_000, 50_000]
    z = [100, 200, 500, 1_000, 2_000, 5_000]
    
    # temporary testing playground for scale
    #from scenarios.a1ta3scale import *
    #scenario = Amalgam1ToAmalgam3PlainScale(prefix, size=5000, scale=20)
    #scenario.run(app, launches=1, stats=showStats, nodeIndex=True, relIndex=False)

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
    from figures.overheadCD import *
    from figures.gtb import *
    from figures.flighthotelrand import *
    from figures.personaddressrand import *
    from figures.persondatarand import *
    from figures.gtbrand import *
    from figures.dta1rand import *
    from figures.a1ta3rand import *
    from figures.flighthotelscale import *
    from figures.personaddressscale import *
    from figures.persondatascale import *
    from figures.gtbscale import *
    from figures.dta1scale import *
    from figures.a1ta3scale import *
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
        #FigureComparisonAlternativeApproachesDTA1(app, prefix=prefix, values=y, nbLaunches=20, showStats=showStats),

        #FigureComparisonIndexesA1TA3(app, prefix=prefix, values=x, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonAlternativeApproachesA1TA3(app, prefix=prefix, values=y, nbLaunches=20, showStats=showStats),

        #FigureComparisonBaselineFlightHotel(app, prefix=prefix, values=z, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonBaselinePersonAddress(app, prefix=prefix, values=z, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonBaselinePersonData(app, prefix=prefix, values=z, nbLaunches=nbLaunches, showStats=showStats),

        #FigureOverheadCD(app, prefix=prefix, values=w, nbLaunches=nbLaunches, showStats=showStats),
        #FigureOverheadCDGTB(app, prefix=prefix, values=w, nbLaunches=nbLaunches, showStats=showStats),
        
        #FigureComparisonIndexesGTB(app, prefix=prefix, values=x, nbLaunches=nbLaunches, showStats=showStats),
        #FigureComparisonAlternativeApproachesGTB(app, prefix=prefix, values=y, nbLaunches=20, showStats=showStats),

        #FigureFlightHotelRandomConflicts(app, prefix=prefix, values=[10000], nbLaunches=20, showStats=showStats, probs=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
        #FigurePersonAddressRandomConflicts(app, prefix=prefix, values=[10000], nbLaunches=20, showStats=showStats, probs=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
        #FigurePersonDataRandomConflicts(app, prefix=prefix, values=[10000], nbLaunches=20, showStats=showStats, probs=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
        #FigureGTBRandomConflicts(app, prefix=prefix, values=[10000], nbLaunches=20, showStats=showStats, probs=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
        #FigureDTA1RandomConflicts(app, prefix=prefix, values=[10000], nbLaunches=20, showStats=showStats, probs=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
        #FigureA1TA3RandomConflicts(app, prefix=prefix, values=[10000], nbLaunches=20, showStats=showStats, probs=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),

        #FigureFlightHotelScale(app, prefix=prefix, values=[5000], nbLaunches=nbLaunches, showStats=showStats, scale=[1, 2, 5, 10, 20, 50]),
        #FigurePersonAddressScale(app, prefix=prefix, values=[5000], nbLaunches=nbLaunches, showStats=showStats, scale=[1, 2, 5, 10, 20, 50]),
        #FigurePersonDataScale(app, prefix=prefix, values=[5000], nbLaunches=nbLaunches, showStats=showStats, scale=[1, 2, 5, 10, 20, 50]),
        #FigureGTBScale(app, prefix=prefix, values=[5000], nbLaunches=nbLaunches, showStats=showStats, scale=[1, 2, 5, 10, 20]),
        #FigureDTA1Scale(app, prefix=prefix, values=[5000], nbLaunches=nbLaunches, showStats=showStats, scale=[1, 2, 5, 10]),
        #FigureA1TA3Scale(app, prefix=prefix, values=[5000], nbLaunches=nbLaunches, showStats=showStats, scale=[1, 2, 5, 10]),
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
