## Navigating Logs in Terminal

### E2 Termination logs
To view the output of the RIC E2 termination service, to which RAN nodes connect over SCTP
```bash
  kubectl logs -f -n ricplt -l app=ricplt-e2term-alpha
```

To view the output of the RIC E2 manager service, which shows information about connected RAN nodes
```bash
kubectl logs -f -n ricplt -l app=ricplt-e2mgr
```
### xApp related logs: Application subscriptions and routing
To view the output of the RIC subscription manager service, which aggregates xApp subscription requests and forwards them to target RAN nodes
```bash
 kubectl logs -f -n ricplt -l app=ricplt-submgr
```

To view the output of the RIC route manager, which manages RMR routes across the RIC components

```bash
kubectl logs -f -n ricplt -l app=ricplt-rtmgr
```

## Navigating Logs on Headlamp dasboard.

These logs can also be viewed over our deployed [***Kubernetes Cluster Dashboard***](localhost:8080/c/main/map?group=namespace).

The headlamp dashboard provides a neat visualization for deployed clusters, you further click on each namespace to see further mapping.
<img src="{{"/assets/img/docs/oran/headlamp-dashboard.png"  | relative_url }}" 
       alt="Headlamp-Dashboard" 
       style="max-width: 100%; height: auto;" />

From the dashboard page goto the [***Workloads***](localhost:8080/c/main/workloads) tab from left pane and click on the specific service deployment you wish to view logs of as shown in image below.

<img src="{{"/assets/img/docs/oran/headlamp-logs.png"  | relative_url }}" 
       alt="Headlamp-Dashboard" 
       style="max-width: 100%; height: auto;" />