# deployment-pipeline-challenge
For the 'The Anatomy of a Deployment Pipeline' course by Continuous Delivery Ltd

## Overview
This is a dashboard that will show the status of the orders for customers (like in a lobby). Imagine that there is a different system that's actually processing the food orders, and it is creating logs of the food orders. The logs are what will be used to populate the dashboard. 

Overall objective is to build a dashboard in an iterative way and experience what having a pipeline from the start for a UI could solve with being able to pivot quickly.

## Local Tests & Running

```
docker-compose build
docker-compose up
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
At the end of the commit stage

*What Is Your Objective?*
To ensure the artifacts built work

*What Is Your Next Step?*
Move onto the acceptance stage

*How Will You Know If You Have Succeeded?*
Not sure yet
