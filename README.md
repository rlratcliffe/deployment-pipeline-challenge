# deployment-pipeline-challenge
For the 'The Anatomy of a Deployment Pipeline' course by Continuous Delivery Ltd

## Overview
This is a dashboard that will show the status of the orders for customers (like in a lobby). Imagine that there is a different system that's actually processing the food orders, and it is creating logs of the food orders. The logs are what will be used to populate the dashboard. 

Overall objective is to learn about walking skeletons/vertical slicing by building a dashboard in an iterative way. And experiencing what having a pipeline from the start for a UI could solve with being able to pivot quickly.

## Local Unit Tests & Running

```
docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up
docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml down
```

## Local Acceptance Tests

```
robot -d results acceptance-tests/robot-framework/Tests/UI/Test_Dashboard.robot
robot -d results acceptance-tests/robot-framework/Tests/API/Test_API.robot

or run all tests at once with

robot -d results acceptance-tests/robot-framework/Tests
```

## Slicing
### Current focus/use case:
Customer can identify when food order has started processing

### Current vertical slice:
- Simplest UI: Table showing
- Simplest logic: API that transforms the logs into a list that the table can show easily
- Simplest storage: Logs as a CSV

### Questions
**Current Big Picture**

*What Is Your Objective?*
To complete the acceptance test stage.

*How Will You Know If You Have Succeeded?*

When these things are complete and working:
- automated configuration of the test environment
- automated deploy of release candidate
- automated smoke test/health check
- acceptance tests running in test environment
- record of results with release candidate id as key

**Current Details**

*Where Do You Think You Are Now?*
Finished setting up robot framework UI tests to work locally

*What Is Your Objective?*
Finish setting up API acceptance tests

*What Is Your Next Step?*
Setup robot framework API tests

*How Will You Know If You Have Succeeded?*
Failing API tests return as failure, passing API tests return as success


## Other Todos
- Create actual external db (sqllite?) with init scripts
- Connect API to db