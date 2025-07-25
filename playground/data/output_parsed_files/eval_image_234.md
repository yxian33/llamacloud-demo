

# Network Architecture Overview

## Product Categories and Models

| Fronthaul Gateway | Cell Site Router | Cell Site Router | Cell Site Router | Metro Access |
| ----------------- | ---------------- | ---------------- | ---------------- | ------------ |
| Monterey          | Qumran2c         | QumranAX         | QumranUX         | Jericho2     |


## Network Topology

```mermaid
graph LR
    A[Fronthaul] --> B[Router]
    B --> C[Router]
    C --> D[Router]
    D --> E[Backhaul Router]
    
    F[Enterprise Access] --> G[Router]
    G --> H[Router]
    
    E --> I[Metro Aggregation Cloud]
    H --> I
    
    I --> J[Metro Core Cloud]
    J --> K[Router]
    K --> L[Core Router]
    L --> M[Core Router]
    M --> N[Core Router]
    N --> O[DCI Router]
    O --> P[Data Center]
    
    J --> Q[Router]
    Q --> R[Core Router]
    R --> S[Core Router]
    S --> T[DCI Router]
    T --> P
```

## Component Mapping by Network Function

| uCPE        | OLT      | vBNG      | Metro Edge | Metro Core | DCI      | Data Center Spine | Data Center Leaf |
| ----------- | -------- | --------- | ---------- | ---------- | -------- | ----------------- | ---------------- |
| Trident3-X3 | QumranAX | Jericho2c | Jericho2   | Jericho2   | Jericho2 | Tomahawk4         | Trident3         |
| Trident3-X2 |          |           |            | Ramon      |          |                   | Trident4         |



