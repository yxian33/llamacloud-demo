
```mermaid
flowchart LR
    A[Water making] --> B[Deposition]
    B --> C[Lithography]
    C --> D[Etch]
    D --> E[Deposition]
    E --> F[Planarization]
    F --> G[Assembly / Test]
    G --> H[Packaging]
    H --> I[Completed IC]
    
    F -.-> C
    
    classDef emphasized fill:#8B0000,color:#fff
    classDef normal fill:#FFB6C1,color:#000
    
    class A,B,E emphasized
    class C,D,F,G,H normal
```

**Repeat many times** (feedback loop from Planarization back to Lithography)

**WAFER FAB PROCESS** (encompasses the process from Deposition through Planarization)

**ASM FOCUS IS ON DEPOSITION** (highlighting the two Deposition steps)
