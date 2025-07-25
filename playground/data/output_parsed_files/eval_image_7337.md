
# Traditional Data Center Network Topology

The traditional data center network topology shows a hierarchical three-tier architecture:

- **Core Layer**: Multiple core switches at the top level interconnected with each other
- **Aggregate Layer**: Aggregate switches in the middle tier, with each aggregate switch connected to multiple core switches above
- **Edge Layer**: Edge switches at the bottom tier connecting to servers, with each edge switch connected to multiple aggregate switches above

The servers are grouped under each edge switch, forming a tree-like structure where traffic flows up and down through the hierarchy.

# Fat Tree Network Topology

The fat tree network topology presents a more complex but scalable architecture organized into pods:

- **Core Layer**: Core switches (labeled as Agg1, Agg2, Agg3, Agg4) providing full connectivity across all pods
- **Aggregate Layer**: Aggregate switches within each pod, fully connected to core switches above and edge switches below
- **Edge Layer**: Edge switches connecting directly to servers within each pod

The topology is organized into four pods (Pod 1, Pod 2, Pod 3, Pod 4), where:
- Each pod contains multiple aggregate and edge switches
- Servers are distributed across the edge switches within each pod
- The core layer provides full bisection bandwidth between all pods
- Each aggregate switch in a pod connects to all core switches
- Each edge switch in a pod connects to all aggregate switches in the same pod

This fat tree design provides multiple paths between any two servers, offering better bandwidth utilization and fault tolerance compared to the traditional hierarchical approach.
