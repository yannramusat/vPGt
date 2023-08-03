#!/bin/env python3

from app import App

if __name__ == "__main__":
    # app setup
    scheme = "bolt"
    hostname = "localhost"
    port = "7687"
    uri = f"{scheme}://{hostname}:{port}"
    app = App(uri, "neo4j", verbose=False)

    # common prefix for CSVs; the data has been generated by iBench
    prefix = "file:///home/yann/research/ibench/build/ibench/"
    nbLaunches = 1
    showStats = True
    useIndexes = True
    x = [100, 200, 500, 1_000, 2_000, 5_000] #, 10_000, 20_000, 50_000, 100_000]

    # execute the Optimized alternative implementation of the scenario FlightHotel
    from scenarios.flighthotel import FlightHotelScenarioWithIndexes
    resultsOptiFH = []
    for i in x:
        scenario = FlightHotelScenarioWithIndexes(prefix, size=i)
        resultsOptiFH.append(scenario.run(app, launches=nbLaunches, stats=showStats, index=True))

    # execute the Optimized alternative implementation of the scenario FlightHotel (without Indexes!)
    resultsNoIndexFH = []
    for i in x:
        scenario = FlightHotelScenarioWithIndexes(prefix, size=i)
        resultsNoIndexFH.append(scenario.run(app, launches=nbLaunches, stats=showStats, index=False))

    # optional print in console
    if showStats:
        print(resultsOptiFH)
        print(resultsNoIndexFH)
   
    #####
    # TEMPORARY PLOTTING
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots(layout="constrained")
    ax.plot(x, resultsOptiFH, label="Optimized")
    ax.plot(x, resultsNoIndexFH, label="Without indexes")
    ax.set_title("$\mathtt{FlightHotel}$ scenario")
    ax.set_xlabel("cardinality of input relations")
    ax.set_ylabel("time [ms]")
    ax.set_yscale("log")
    ax.legend()
    plt.show()

    # TEMPORARY BREAK POINT
    exit()
    #####

    # execute the Optimized alternative implementation of the scenario PersonAddress
    from scenarios.personaddress import PersonAddressScenarioWithIndexes
    resultsOpti = []
    for i in x:
        scenario = PersonAddressScenarioWithIndexes(prefix, size=i)
        resultsOpti.append(scenario.run(app, launches=nbLaunches, stats=showStats, index=useIndexes))

    # execute the Naive alternative implementation of the scenario PersonAddress
    from scenarios.personaddress import PersonAddressScenarioNaive
    resultsNaive = []
    for i in []:
        scenario = PersonAddressScenarioNaive(prefix, size=i)
        resultsNaive.append(scenario.run(app, launches=nbLaunches, stats=showStats, index=False))

    # execute the dummy version of the Naive alternative implementation of the scenario PersonAddress
    resultsDummy = []
    for i in x:
        scenario = PersonAddressScenarioNaive(prefix, size=i)
        resultsDummy.append(scenario.run(app, launches=nbLaunches, stats=showStats, index=True))

    # execute the alternative implementation with Conflict Detection of the scenario PersonAddress
    from scenarios.personaddress import PersonAddressScenarioWithConflictDetection
    resultsCD = []
    for i in x:
        scenario = PersonAddressScenarioWithConflictDetection(prefix, size=i)
        resultsCD.append(scenario.run(app, launches=nbLaunches, stats=showStats, index=useIndexes))

    # optional print in console
    if showStats:
        print(resultsOpti)
        print(resultsNaive)
        print(resultsDummy)
        print(resultsCD)

    # plot results using matplotlib
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots(layout="constrained")
    ax.plot(x, resultsOpti, label="Optimized")
    #ax.plot(x, resultsNaive, label="Naive")
    ax.plot(x, resultsDummy, label="Dummy")
    ax.plot(x, resultsCD, label="Conflict Detection")
    ax.set_title("$\mathtt{PersonAddress}$ scenario")
    ax.set_xlabel("cardinality of input relations")
    ax.set_ylabel("time [ms]")
    ax.set_yscale("log")
    ax.legend()
    plt.show()

    # close connection
    app.close()
