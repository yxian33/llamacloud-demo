

# Complement System Pathways

```mermaid
flowchart TD
    A["(Auto)antibodies"] --> B[Classical]
    M[Microorganisms] --> L[Lectin]
    M --> Alt[Alternative]
    
    B --> IgG[IgG]
    B --> IgM[IgM]
    L --> MS[Mannose sugar]
    Alt --> FS[Foreign surface]
    
    IgG --> C1[C1qrs]
    IgM --> C1
    MS --> MBL[MBL]
    FS --> C3_alt[C3]
    
    C1 --> C4[C4]
    MBL --> MASPs[MASPs]
    C3_alt --> CFB[CFB]
    C3_alt --> CFD[CFD]
    
    C4 --> C2[C2]
    MASPs --> C2
    CFB --> C3conv[C3 convertase]
    CFD --> C3conv
    
    C2 --> C3conv
    C3conv --> C3[C3]
    C3 --> C3a[C3a]
    C3 --> C3b[C3b]
    
    C3a --> C3aR[C3a-R]
    C3b --> C5conv[C5 convertase]
    C5conv --> C5[C5]
    C5 --> C5a[C5a]
    C5 --> C5bC9[C5b-C9 MAC]
    
    C5a --> C5aR[C5a-R]
    C5bC9 --> SubMAC[Sublytic MAC]
    
    C3aR --> Inflammation[Inflammation]
    C5aR --> Inflammation
    SubMAC --> MemDamage[Membrane damage]
    
    C3b --> Clearance[Clearance by macrophages]
    
    %% Intervention points
    Circle1[1] --> Target1[Target upstream of C5 to shut down all effector functions]
    Circle2[2] --> Target2[Intact alternative pathway to reduce infection risk]
    Circle3[3] --> Target3[Crossroad of classical & lectin pathways<br/>Manageable C2 levels in circulation<br/>Benign C2-deficiency phenotype]
    
    %% Company logo
    Logo[argenx]
```

## Key Therapeutic Intervention Points

**1.** Target upstream of C5 to shut down all effector functions

**2.** Intact alternative pathway to reduce infection risk  

**3.** Crossroad of classical & lectin pathways
- Manageable C2 levels in circulation
- Benign C2-deficiency phenotype

## Pathway Components

### Classical Pathway
- Triggered by: (Auto)antibodies
- Components: IgG, IgM → C1qrs → C4 → C2

### Lectin Pathway  
- Triggered by: Microorganisms
- Components: Mannose sugar → MBL → MASPs → C2

### Alternative Pathway
- Triggered by: Microorganisms  
- Components: Foreign surface → C3 → CFB, CFD

## Downstream Effects

- **C3 convertase** → C3 → C3a, C3b
- **C5 convertase** → C5 → C5a, C5b-C9 MAC
- **C3a-R, C5a-R** → Inflammation
- **C3b** → Clearance by macrophages  
- **Sublytic MAC** → Membrane damage

argenx

