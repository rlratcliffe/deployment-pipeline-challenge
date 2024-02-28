# deployment-pipeline-challenge
For the 'The Anatomy of a Deployment Pipeline' course by Continuous Delivery Ltd

## Overview
This is a dashboard that will show the status of the orders for customers (like in a lobby). Imagine that there is a different system that's actually processing the food orders, and it is creating logs of the food orders. The logs are what will be used to populate the dashboard. 

Overall objective is to learn about walking skeletons/vertical slicing by building a dashboard in an iterative way. And experiencing what having a pipeline from the start for a UI could solve with being able to pivot quickly.

## Local Tests & Running

```
docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up
docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml down
```

## Slicing
### Current focus/use case:
Customer can identify when food order has started processing

### Current vertical slice:
- Simplest UI: Table showing
- Simplest logic: API that transforms the logs into a list that the table can show easily
- Simplest storage: Logs as a CSV

### Questions
*Where Do You Think You Are Now?*
At the end of the Commit stage, onto the Acceptance stage

*What Is Your Objective?*
To build the next stage

*What Is Your Next Step?*
Watch the acceptance test stage videos

*How Will You Know If You Have Succeeded?*
Not sure yet
