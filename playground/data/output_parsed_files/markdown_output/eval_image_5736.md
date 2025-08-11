

2023

# High-speed optics enable large AI clusters

```mermaid
flowchart TD
    A[GPU to GPU Switch<br/>800G<br/>~10G Ballops] 
    B[ALLSTAR<br/>GALS<br/>800G<br/>~10G Ballops]
    C[Switch<br/>Clustering<br/>800G<br/>~50,000G GALS<br/>~10G Ballops]
    
    A ---|Scale up| B
    B ---|Scale out| C
    
    style A fill:#4A90E2
    style B fill:#666666
    style C fill:#2ECC71
```

| Network Layer     | Function               | Speed | Capacity                      |
| ----------------- | ---------------------- | ----- | ----------------------------- |
| GPU to GPU Switch | Scale up               | 800G  | \~10G Ballops                 |
| ALLSTAR GALS      | Intermediate switching | 800G  | \~10G Ballops                 |
| Clustering Switch | Scale out              | 800G  | \~50,000G GALS, \~10G Ballops |



