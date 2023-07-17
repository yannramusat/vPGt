#!/bin/env python3

from app import App
from structures import InputRelation, InputSchema, TransformationRule, Scenario

if __name__ == "__main__":
    # app setup
    scheme = "bolt"
    hostname = "localhost"
    port = "7687"
    uri = f"{scheme}://{hostname}:{port}"
    app = App(uri, "neo4j", verbose=False)

    # common prefix for CSVs; the data has been generated by ibench
    prefix = "file:///home/yann/research/ibench/build/ibench/"

    # execute the scenario PersonAddress
    from scenarios.person_address import PersonAddressScenario
    results = []
    for i in [100, 200, 500, 1000, 2000]:
        scenario = PersonAddressScenario(prefix, size=i)
        results.append(scenario.run(app, launches=1, stats=True, index=True))
    print(results)

    # close connection
    app.close()
